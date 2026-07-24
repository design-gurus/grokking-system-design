#!/usr/bin/env python3
"""
Grokking System Design — local study assistant.

A 100%-offline retrieval-augmented (RAG) study buddy over this repository's
markdown. It indexes every `.md` file, retrieves the most relevant sections for
your question, and (optionally) has a local LLM answer using only that context,
citing the source files. Nothing leaves your machine: the only network calls go
to a local Ollama server at 127.0.0.1:11434.

Commands
--------
    build            Index the repo (embeds chunks if Ollama is running).
    ask "question"   Answer one question with citations.
    chat             Interactive Q&A loop.
    quiz [topic]     Flashcard quiz from cheat-sheets/flashcards.md.

Design goals
------------
- Zero required third-party packages: the standard library is enough, and it
  degrades gracefully. `numpy` is used automatically if present (faster math).
- Works with no LLM at all: without Ollama it falls back to keyword retrieval
  and just shows you the most relevant sections.

See the README in this folder for setup.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Iterable

# --------------------------------------------------------------------------- #
# Configuration (override via environment variables)
# --------------------------------------------------------------------------- #

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434").rstrip("/")
EMBED_MODEL = os.environ.get("SDA_EMBED_MODEL", "nomic-embed-text")
CHAT_MODEL = os.environ.get("SDA_CHAT_MODEL", "llama3.2")

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent  # tools/study-assistant/ -> repo root
INDEX_PATH = SCRIPT_DIR / "index.json"
FLASHCARDS_PATH = REPO_ROOT / "cheat-sheets" / "flashcards.md"

# Directories we never index.
SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__"}

DEFAULT_TOP_K = 5
CHUNK_TARGET_CHARS = 1200  # aim for chunks around this size

SYSTEM_PROMPT = (
    "You are a precise system design study assistant for the 'Grokking System "
    "Design' repository. Answer the question using ONLY the provided context "
    "sections. If the context does not contain the answer, say so plainly and "
    "point to the page that looks most relevant. Be concise and concrete. When "
    "you use a fact, cite its source file in square brackets, e.g. "
    "[patterns/caching.md]. Prefer the repo's own vocabulary."
)

# Optional numpy acceleration.
try:  # pragma: no cover - trivial import guard
    import numpy as _np
except Exception:  # noqa: BLE001
    _np = None


# --------------------------------------------------------------------------- #
# Small terminal helpers
# --------------------------------------------------------------------------- #

def _supports_color() -> bool:
    return sys.stdout.isatty() and os.environ.get("NO_COLOR") is None


def c(text: str, code: str) -> str:
    if not _supports_color():
        return text
    return f"\033[{code}m{text}\033[0m"


def bold(t: str) -> str:
    return c(t, "1")


def dim(t: str) -> str:
    return c(t, "2")


def cyan(t: str) -> str:
    return c(t, "36")


def green(t: str) -> str:
    return c(t, "32")


def yellow(t: str) -> str:
    return c(t, "33")


# --------------------------------------------------------------------------- #
# Ollama client (via stdlib urllib; no third-party deps)
# --------------------------------------------------------------------------- #

def _post(path: str, payload: dict, timeout: float = 120.0):
    req = urllib.request.Request(
        f"{OLLAMA_HOST}{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    return urllib.request.urlopen(req, timeout=timeout)


def list_models() -> list[str] | None:
    """Return installed Ollama model names, or None if the server is unreachable."""
    try:
        req = urllib.request.Request(f"{OLLAMA_HOST}/api/tags", method="GET")
        with urllib.request.urlopen(req, timeout=2.0) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return [m.get("name", "") for m in data.get("models", [])]
    except Exception:  # noqa: BLE001
        return None


def ollama_available() -> bool:
    """True if a local Ollama server answers quickly."""
    return list_models() is not None


def model_present(name: str, models: list[str] | None = None) -> bool:
    """True if `name` (with or without a :tag) is installed."""
    if models is None:
        models = list_models() or []
    base = name.split(":")[0]
    return any(m == name or m.split(":")[0] == base for m in models)


def embed(text: str) -> list[float] | None:
    """Return an embedding vector for `text`, or None on failure."""
    try:
        with _post("/api/embeddings", {"model": EMBED_MODEL, "prompt": text}) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        vec = data.get("embedding")
        return vec if vec else None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(yellow(
                f"  Model '{EMBED_MODEL}' not found. Run: ollama pull {EMBED_MODEL}"
            ))
        return None
    except Exception:  # noqa: BLE001
        return None


def generate_stream(prompt: str, system: str = SYSTEM_PROMPT) -> Iterable[str]:
    """Yield response fragments from the chat model as they arrive."""
    payload = {
        "model": CHAT_MODEL,
        "prompt": prompt,
        "system": system,
        "stream": True,
        "options": {"temperature": 0.2},
    }
    try:
        with _post("/api/generate", payload, timeout=300.0) as resp:
            for raw in resp:
                line = raw.decode("utf-8").strip()
                if not line:
                    continue
                obj = json.loads(line)
                if obj.get("response"):
                    yield obj["response"]
                if obj.get("done"):
                    break
    except urllib.error.HTTPError as e:
        if e.code == 404:
            yield (
                f"\n[Model '{CHAT_MODEL}' not found. Run: ollama pull {CHAT_MODEL}]"
            )
        else:
            yield f"\n[Ollama error: {e}]"
    except Exception as e:  # noqa: BLE001
        yield f"\n[Could not reach Ollama: {e}]"


# --------------------------------------------------------------------------- #
# Markdown chunking
# --------------------------------------------------------------------------- #

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
_WORD_RE = re.compile(r"[a-z0-9]+")

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "is", "it", "for", "on",
    "as", "at", "by", "be", "are", "with", "that", "this", "you", "your", "how",
    "what", "when", "why", "which", "do", "does", "can", "vs", "from", "if",
    "into", "not", "but", "so", "we", "they", "them", "one", "each", "than",
}


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def chunk_markdown(path: Path, text: str) -> list[dict]:
    """Split a markdown file into heading-delimited chunks, merging tiny ones
    and splitting oversized ones on paragraph boundaries."""
    rel = str(path.relative_to(REPO_ROOT))
    lines = text.splitlines()

    # First title (# ...) becomes the document title for context/citation.
    doc_title = rel
    for ln in lines:
        m = _HEADING_RE.match(ln)
        if m and len(m.group(1)) == 1:
            doc_title = m.group(2).strip()
            break

    # Group lines under their nearest heading.
    sections: list[tuple[str, list[str]]] = []
    current_heading = doc_title
    buf: list[str] = []
    in_code = False
    for ln in lines:
        if ln.strip().startswith("```"):
            in_code = not in_code
        m = _HEADING_RE.match(ln) if not in_code else None
        if m:
            if buf:
                sections.append((current_heading, buf))
                buf = []
            current_heading = m.group(2).strip()
        else:
            buf.append(ln)
    if buf:
        sections.append((current_heading, buf))

    # Build chunks, merging small adjacent sections.
    chunks: list[dict] = []
    pending_heading = None
    pending_text: list[str] = []

    def flush():
        if pending_text:
            body = "\n".join(pending_text).strip()
            if body:
                chunks.append({
                    "file": rel,
                    "title": doc_title,
                    "heading": pending_heading or doc_title,
                    "text": body,
                })

    for heading, body_lines in sections:
        body = "\n".join(body_lines).strip()
        if not body:
            continue
        candidate = ("\n".join(pending_text) + "\n" + body).strip() if pending_text else body
        if pending_text and len(candidate) > CHUNK_TARGET_CHARS:
            flush()
            pending_heading, pending_text = heading, [body]
        else:
            if not pending_text:
                pending_heading = heading
            pending_text.append(body)
        # Split a single oversized section on blank lines.
        while len("\n".join(pending_text)) > CHUNK_TARGET_CHARS * 2:
            joined = "\n".join(pending_text)
            cut = joined.rfind("\n\n", 0, CHUNK_TARGET_CHARS * 2)
            if cut <= 0:
                break
            head, tail = joined[:cut], joined[cut:]
            chunks.append({
                "file": rel, "title": doc_title,
                "heading": pending_heading or doc_title, "text": head.strip(),
            })
            pending_text = [tail.strip()]
    flush()
    return chunks


def tokenize(text: str) -> list[str]:
    return [w for w in _WORD_RE.findall(text.lower()) if w not in STOPWORDS and len(w) > 1]


# --------------------------------------------------------------------------- #
# Index build
# --------------------------------------------------------------------------- #

def build_index() -> None:
    print(bold("Building index over"), cyan(str(REPO_ROOT)))
    models = list_models()
    have_ollama = models is not None
    have_embeddings = have_ollama and model_present(EMBED_MODEL, models)
    if have_embeddings:
        print(green(f"  Ollama detected — embedding with '{EMBED_MODEL}'."))
    elif have_ollama:
        print(yellow(
            f"  Ollama is running but '{EMBED_MODEL}' isn't installed — building a\n"
            f"  keyword-only index. For semantic search run: ollama pull {EMBED_MODEL}"
        ))
    else:
        print(yellow(
            "  Ollama not detected — building a keyword-only index.\n"
            "  (Install Ollama and re-run `build` for semantic search + answers.)"
        ))

    chunks: list[dict] = []
    files = list(iter_markdown_files(REPO_ROOT))
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        chunks.extend(chunk_markdown(path, text))

    print(f"  {len(files)} files -> {len(chunks)} chunks")

    embedded = 0
    for i, ch in enumerate(chunks):
        ch["tokens"] = tokenize(ch["heading"] + "\n" + ch["text"])
        if have_embeddings:
            vec = embed(ch["heading"] + "\n" + ch["text"])
            if vec:
                ch["embedding"] = vec
                embedded += 1
            _progress(i + 1, len(chunks))
    if have_embeddings:
        sys.stdout.write("\n")

    # Document frequencies for the keyword-fallback scorer.
    df: dict[str, int] = {}
    for ch in chunks:
        for tok in set(ch["tokens"]):
            df[tok] = df.get(tok, 0) + 1

    index = {
        "version": 1,
        "repo_root": str(REPO_ROOT),
        "embed_model": EMBED_MODEL if embedded else None,
        "num_chunks": len(chunks),
        "doc_freq": df,
        "chunks": chunks,
    }
    INDEX_PATH.write_text(json.dumps(index), encoding="utf-8")
    size_mb = INDEX_PATH.stat().st_size / 1e6
    print(green(f"  Wrote {INDEX_PATH.name} ({size_mb:.1f} MB), {embedded} embedded chunks."))
    if not embedded:
        print(dim("  Retrieval will use keyword matching until you rebuild with Ollama."))


def _progress(done: int, total: int) -> None:
    width = 30
    filled = int(width * done / max(total, 1))
    bar = "#" * filled + "-" * (width - filled)
    sys.stdout.write(f"\r  embedding [{bar}] {done}/{total}")
    sys.stdout.flush()


# --------------------------------------------------------------------------- #
# Retrieval
# --------------------------------------------------------------------------- #

def load_index() -> dict:
    if not INDEX_PATH.exists():
        sys.exit(yellow(
            f"No index found at {INDEX_PATH}.\n"
            "Run:  python3 study_assistant.py build"
        ))
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def _cosine(a: list[float], b: list[float]) -> float:
    if _np is not None:
        va, vb = _np.asarray(a), _np.asarray(b)
        denom = (_np.linalg.norm(va) * _np.linalg.norm(vb)) or 1.0
        return float(va.dot(vb) / denom)
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a)) or 1.0
    nb = math.sqrt(sum(y * y for y in b)) or 1.0
    return dot / (na * nb)


def retrieve(index: dict, query: str, top_k: int, can_embed: bool) -> tuple[list[dict], str]:
    """Return (top chunks, mode) where mode is 'semantic' or 'keyword'."""
    chunks = index["chunks"]
    has_vectors = any("embedding" in ch for ch in chunks)

    if can_embed and has_vectors:
        qvec = embed(query)
        if qvec:
            scored = [
                (_cosine(qvec, ch["embedding"]), ch)
                for ch in chunks if "embedding" in ch
            ]
            scored.sort(key=lambda t: t[0], reverse=True)
            return [ch for _, ch in scored[:top_k]], "semantic"

    # Keyword fallback: TF-IDF-ish overlap score.
    n_docs = max(index.get("num_chunks", len(chunks)), 1)
    df = index.get("doc_freq", {})
    q_tokens = tokenize(query)
    if not q_tokens:
        return chunks[:top_k], "keyword"

    scored = []
    for ch in chunks:
        tf: dict[str, int] = {}
        for tok in ch["tokens"]:
            tf[tok] = tf.get(tok, 0) + 1
        score = 0.0
        for tok in q_tokens:
            if tok in tf:
                idf = math.log((n_docs + 1) / (df.get(tok, 0) + 1)) + 1.0
                score += (1 + math.log(tf[tok])) * idf
        if score > 0:
            scored.append((score, ch))
    scored.sort(key=lambda t: t[0], reverse=True)
    return [ch for _, ch in scored[:top_k]], "keyword"


def format_context(chunks: list[dict]) -> str:
    parts = []
    for ch in chunks:
        parts.append(f"### Source: {ch['file']} — {ch['heading']}\n{ch['text']}")
    return "\n\n".join(parts)


# --------------------------------------------------------------------------- #
# Commands: ask / chat / quiz
# --------------------------------------------------------------------------- #

def answer_question(index: dict, question: str, top_k: int) -> None:
    models = list_models()
    can_embed = models is not None and model_present(EMBED_MODEL, models)
    can_generate = models is not None and model_present(CHAT_MODEL, models)
    chunks, mode = retrieve(index, question, top_k, can_embed)

    if not chunks:
        print(yellow("No relevant sections found. Try rephrasing, or rebuild the index."))
        return

    sources = []
    for ch in chunks:
        tag = f"{ch['file']} — {ch['heading']}"
        if tag not in sources:
            sources.append(tag)

    if can_generate:
        prompt = (
            f"Context sections from the repo:\n\n{format_context(chunks)}\n\n"
            f"Question: {question}\n\n"
            "Answer using only the context above, and cite source files in "
            "square brackets."
        )
        print(bold("\nAnswer ") + dim(f"({mode} retrieval, {CHAT_MODEL})") + "\n")
        for frag in generate_stream(prompt):
            sys.stdout.write(frag)
            sys.stdout.flush()
        print("\n")
    else:
        reason = (
            f"the '{CHAT_MODEL}' model isn't installed (run: ollama pull {CHAT_MODEL})"
            if models is not None
            else "Ollama isn't running"
        )
        print(yellow(
            f"\n{reason}, so here are the most relevant sections "
            f"({mode} search).\nEnable the local model for synthesized answers.\n"
        ))
        for ch in chunks:
            print(bold(f"— {ch['file']} · {ch['heading']}"))
            snippet = ch["text"].strip()
            if len(snippet) > 600:
                snippet = snippet[:600].rstrip() + " …"
            print(snippet + "\n")

    print(dim("Sources:"))
    for s in sources:
        print(dim(f"  • {s}"))


def chat_loop(index: dict, top_k: int) -> None:
    print(bold("Study assistant — interactive mode."))
    print(dim("Ask anything about the repo. Type 'exit' or Ctrl-D to quit.\n"))
    while True:
        try:
            q = input(cyan("you › ")).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n" + dim("bye!"))
            return
        if not q:
            continue
        if q.lower() in {"exit", "quit", ":q"}:
            print(dim("bye!"))
            return
        answer_question(index, q, top_k)


_CARD_Q_RE = re.compile(r"^\*\*Q:\*\*\s*(.*)$")
_CARD_A_RE = re.compile(r"^\*\*A:\*\*\s*(.*)$")
_TOPIC_RE = re.compile(r"^##\s+(.*)$")


def parse_flashcards() -> list[dict]:
    if not FLASHCARDS_PATH.exists():
        return []
    cards: list[dict] = []
    topic = "General"
    q_lines: list[str] = []
    a_lines: list[str] = []
    state: str | None = None

    def flush():
        nonlocal q_lines, a_lines, state
        if q_lines and a_lines:
            cards.append({"topic": topic, "q": " ".join(q_lines).strip(),
                          "a": " ".join(a_lines).strip()})
        q_lines, a_lines, state = [], [], None

    for ln in FLASHCARDS_PATH.read_text(encoding="utf-8").splitlines():
        tm = _TOPIC_RE.match(ln)
        if tm:  # a new topic heading ends the current card
            flush()
            topic = tm.group(1).strip()
            continue
        qm, am = _CARD_Q_RE.match(ln), _CARD_A_RE.match(ln)
        if qm:  # a new question ends the previous card
            flush()
            q_lines, state = [qm.group(1)], "q"
        elif am:
            a_lines, state = [am.group(1)], "a"
        elif ln.strip() and state == "q":
            q_lines.append(ln.strip())
        elif ln.strip() and state == "a":
            a_lines.append(ln.strip())
    flush()
    return cards


def quiz(topic: str | None) -> None:
    cards = parse_flashcards()
    if not cards:
        sys.exit(yellow(f"No flashcards found at {FLASHCARDS_PATH}."))
    if topic:
        t = topic.lower()
        cards = [c_ for c_ in cards if t in c_["topic"].lower()]
        if not cards:
            topics = sorted({c_["topic"] for c_ in parse_flashcards()})
            sys.exit(yellow(f"No cards for '{topic}'. Topics: " + ", ".join(topics)))

    import random
    random.shuffle(cards)
    have_ollama = model_present(CHAT_MODEL)
    print(bold(f"Quiz — {len(cards)} card(s)") +
          (dim(f" · topic: {topic}") if topic else "") + "\n")

    for i, card in enumerate(cards, 1):
        print(bold(f"Q{i}. ") + card["q"])
        try:
            ans = input(cyan("your answer › ")).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n" + dim("stopping quiz."))
            return
        if have_ollama and ans:
            prompt = (
                f"Question: {card['q']}\nReference answer: {card['a']}\n"
                f"Student answer: {ans}\n\n"
                "Grade the student answer as Correct, Partially correct, or "
                "Incorrect, in one line, then give a one-sentence tip. Be encouraging."
            )
            print(bold("grade › "), end="")
            for frag in generate_stream(prompt, system="You are a fair, encouraging quiz grader."):
                sys.stdout.write(frag)
                sys.stdout.flush()
            print()
        print(green("model answer › ") + card["a"] + "\n")
        print(dim("-" * 60))


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="study_assistant.py",
        description="Local, offline study assistant for the Grokking System Design repo.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python3 study_assistant.py build\n"
            "  python3 study_assistant.py ask \"how does consistent hashing reduce reshuffling?\"\n"
            "  python3 study_assistant.py chat\n"
            "  python3 study_assistant.py quiz caching\n"
        ),
    )
    sub = p.add_subparsers(dest="command")
    sub.add_parser("build", help="index the repo's markdown")
    a = sub.add_parser("ask", help="answer a single question")
    a.add_argument("question", nargs="+", help="your question")
    a.add_argument("--top-k", type=int, default=DEFAULT_TOP_K,
                   help=f"sections to retrieve (default {DEFAULT_TOP_K})")
    ch = sub.add_parser("chat", help="interactive Q&A loop")
    ch.add_argument("--top-k", type=int, default=DEFAULT_TOP_K,
                    help=f"sections to retrieve (default {DEFAULT_TOP_K})")
    q = sub.add_parser("quiz", help="flashcard quiz")
    q.add_argument("topic", nargs="?", help="optional topic filter (e.g. caching)")
    return p


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)

    if args.command == "build":
        build_index()
    elif args.command == "ask":
        answer_question(load_index(), " ".join(args.question), args.top_k)
    elif args.command == "chat":
        chat_loop(load_index(), args.top_k)
    elif args.command == "quiz":
        quiz(args.topic)
    else:
        build_parser().print_help()


if __name__ == "__main__":
    main()
