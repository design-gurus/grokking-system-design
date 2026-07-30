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
# Web UI: browse resources one by one, chat with the LLM, and self-quiz
# --------------------------------------------------------------------------- #

import html as _html
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

UI_DIR = SCRIPT_DIR / "ui"

# The guided learning path: directories, in the order a learner should walk them.
SECTION_ORDER = [
    ("Fundamentals", "fundamentals"),
    ("Guides", "guides"),
    ("Patterns", "patterns"),
    ("Questions", "questions"),
    ("Low-level design", "low-level-design"),
    ("Cheat sheets", "cheat-sheets"),
    ("Deep dives", "deep-dives"),
]

# Fundamentals has a deliberate reading order; everything else is README-first
# then alphabetical.
FUNDAMENTALS_ORDER = [
    "README.md", "performance-vs-scalability.md", "latency-vs-throughput.md",
    "availability-vs-consistency.md", "consistency-patterns.md",
    "availability-patterns.md", "dns.md", "reverse-proxy-vs-load-balancer.md",
    "application-layer.md", "databases.md", "asynchronism.md",
    "communication.md", "security.md",
]

_INDEX_CACHE: dict | None = None


def get_index() -> dict:
    global _INDEX_CACHE
    if _INDEX_CACHE is None:
        if not INDEX_PATH.exists():
            raise FileNotFoundError(str(INDEX_PATH))
        _INDEX_CACHE = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return _INDEX_CACHE


def _page_title(path: Path) -> str:
    try:
        for ln in path.read_text(encoding="utf-8").splitlines():
            m = _HEADING_RE.match(ln)
            if m and len(m.group(1)) == 1:
                return m.group(2).strip()
    except Exception:  # noqa: BLE001
        pass
    return path.stem.replace("-", " ").title()


def build_toc() -> list[dict]:
    sections = []
    for label, dirname in SECTION_ORDER:
        d = REPO_ROOT / dirname
        if not d.is_dir():
            continue
        names = [p.name for p in d.glob("*.md") if p.name != "_template.md"]
        if dirname == "fundamentals":
            order = [n for n in FUNDAMENTALS_ORDER if n in names] + \
                    sorted(n for n in names if n not in FUNDAMENTALS_ORDER)
        else:
            order = (["README.md"] if "README.md" in names else []) + \
                    sorted(n for n in names if n != "README.md")
        pages = [{"path": f"{dirname}/{n}", "title": _page_title(REPO_ROOT / dirname / n)}
                 for n in order]
        sections.append({"label": label, "dir": dirname, "pages": pages})
    return sections


def _flat_pages(toc: list[dict]) -> list[str]:
    return [p["path"] for s in toc for p in s["pages"]]


# --- Minimal, dependency-free Markdown -> HTML (for the repo's markdown) ----- #

_INLINE_CODE_RE = re.compile(r"`([^`]+)`")
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_ITALIC_RE = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
_ITEM_RE = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")


def _resolve_internal_link(base_rel: str, target: str) -> tuple[str, bool]:
    """Return (target, is_internal_md_page)."""
    if target.startswith(("http://", "https://", "mailto:", "#", "tel:")):
        return target, False
    path_part = target.split("#")[0]
    if not path_part:
        return target, False
    if path_part.endswith("/"):
        path_part += "README.md"
    norm = os.path.normpath(os.path.join(os.path.dirname(base_rel), path_part))
    full = (REPO_ROOT / norm).resolve()
    try:
        full.relative_to(REPO_ROOT)
    except ValueError:
        return target, False
    if norm.endswith(".md") and full.exists():
        return norm.replace(os.sep, "/"), True
    return target, False


def render_inline(text: str, base_rel: str) -> str:
    codes: list[str] = []

    def _stash(m):
        codes.append(f"<code>{_html.escape(m.group(1))}</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = _INLINE_CODE_RE.sub(_stash, text)
    text = _html.escape(text)

    def _link(m):
        label, target = m.group(1), m.group(2)
        resolved, internal = _resolve_internal_link(base_rel, target)
        if internal:
            return f'<a href="#/{resolved}" data-nav="{_html.escape(resolved, quote=True)}">{label}</a>'
        return f'<a href="{_html.escape(target, quote=True)}" target="_blank" rel="noopener">{label}</a>'

    text = _MD_LINK_RE.sub(_link, text)
    text = _BOLD_RE.sub(r"<strong>\1</strong>", text)
    text = _ITALIC_RE.sub(r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)
    return text


def _render_list(lines: list[str], base_rel: str) -> str:
    root: list[dict] = []
    stack: list[tuple[int, list[dict]]] = [(-1, root)]
    for ln in lines:
        m = _ITEM_RE.match(ln)
        if not m:
            continue
        indent = len(m.group(1))
        ordered = bool(re.match(r"\d+\.", m.group(2)))
        node = {"text": m.group(3), "ordered": ordered, "children": []}
        while len(stack) > 1 and stack[-1][0] >= indent:
            stack.pop()
        stack[-1][1].append(node)
        stack.append((indent, node["children"]))

    def emit(items: list[dict]) -> str:
        if not items:
            return ""
        tag = "ol" if items[0]["ordered"] else "ul"
        out = f"<{tag}>"
        for it in items:
            out += "<li>" + render_inline(it["text"], base_rel) + emit(it["children"]) + "</li>"
        return out + f"</{tag}>"

    return emit(root)


def markdown_to_html(md_text: str, rel_path: str) -> str:
    lines = md_text.splitlines()
    out: list[str] = []
    para: list[str] = []
    i, n = 0, len(lines)

    def flush_para():
        if para:
            out.append("<p>" + render_inline(" ".join(para).strip(), rel_path) + "</p>")
            para.clear()

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_para()
            lang = stripped[3:].strip()
            body: list[str] = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            i += 1
            code = "\n".join(body)
            if lang == "mermaid":
                out.append('<div class="mermaid">' + _html.escape(code) + "</div>")
            else:
                cls = f' class="language-{_html.escape(lang)}"' if lang else ""
                out.append(f"<pre><code{cls}>" + _html.escape(code) + "</code></pre>")
            continue

        if not stripped:
            flush_para()
            i += 1
            continue

        m = _HEADING_RE.match(line)
        if m:
            flush_para()
            level = len(m.group(1))
            raw = m.group(2).strip()
            anchor = re.sub(r"[^a-z0-9]+", "-", raw.lower()).strip("-")
            out.append(f'<h{level} id="{anchor}">{render_inline(raw, rel_path)}</h{level}>')
            i += 1
            continue

        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", stripped):
            flush_para()
            out.append("<hr>")
            i += 1
            continue

        # GitHub pipe table: header row + separator row of dashes/pipes/colons
        if "|" in line and i + 1 < n and re.match(r"^[\s|:-]+$", lines[i + 1].strip()) \
                and "-" in lines[i + 1] and "|" in lines[i + 1]:
            flush_para()
            header = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            body_rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                body_rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            thead = "".join(f"<th>{render_inline(h, rel_path)}</th>" for h in header)
            tbody = "".join(
                "<tr>" + "".join(f"<td>{render_inline(c, rel_path)}</td>" for c in row) + "</tr>"
                for row in body_rows
            )
            out.append(f'<div class="table-wrap"><table><thead><tr>{thead}</tr></thead>'
                       f"<tbody>{tbody}</tbody></table></div>")
            continue

        if stripped.startswith(">"):
            flush_para()
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            out.append("<blockquote>" + render_inline(" ".join(quote), rel_path) + "</blockquote>")
            continue

        if _ITEM_RE.match(line):
            flush_para()
            items = []
            while i < n and _ITEM_RE.match(lines[i]):
                items.append(lines[i])
                i += 1
            out.append(_render_list(items, rel_path))
            continue

        para.append(stripped)
        i += 1

    flush_para()
    return "\n".join(out)


# --- HTTP request handler --------------------------------------------------- #

class _StudyHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.0"  # close after each response; simplest for streaming

    def log_message(self, *args):  # keep the console quiet
        pass

    # -- helpers --
    def _json(self, code: int, obj) -> None:
        self._bytes(code, json.dumps(obj).encode("utf-8"), "application/json; charset=utf-8")

    def _bytes(self, code: int, data: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        try:
            self.wfile.write(data)
        except Exception:  # noqa: BLE001
            pass

    def _stream_open(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "application/x-ndjson; charset=utf-8")
        self.end_headers()

    def _stream(self, obj) -> None:
        try:
            self.wfile.write((json.dumps(obj) + "\n").encode("utf-8"))
            self.wfile.flush()
        except Exception:  # noqa: BLE001
            pass

    def _read_json(self) -> dict:
        length = int(self.headers.get("Content-Length", 0) or 0)
        if not length:
            return {}
        try:
            return json.loads(self.rfile.read(length) or b"{}")
        except Exception:  # noqa: BLE001
            return {}

    # -- routing --
    def do_GET(self):
        u = urlparse(self.path)
        route, qs = u.path, parse_qs(u.query)
        if route in ("/", "/index.html"):
            self._serve_index()
        elif route == "/api/status":
            self._api_status()
        elif route == "/api/toc":
            self._json(200, {"sections": build_toc()})
        elif route == "/api/page":
            self._api_page(qs.get("path", [""])[0])
        elif route == "/api/quiz":
            self._api_quiz(qs.get("topic", [None])[0], qs.get("path", [None])[0])
        else:
            self._json(404, {"error": "not found"})

    def do_POST(self):
        route = urlparse(self.path).path
        body = self._read_json()
        if route == "/api/ask":
            self._api_ask(body)
        elif route == "/api/grade":
            self._api_grade(body)
        elif route == "/api/gen-question":
            self._api_gen_question(body)
        elif route == "/api/interview":
            self._api_interview(body)
        elif route == "/api/interview-score":
            self._api_interview_score(body)
        else:
            self._json(404, {"error": "not found"})

    # -- endpoints --
    def _serve_index(self):
        f = UI_DIR / "index.html"
        if not f.exists():
            self._bytes(500, b"UI file missing (tools/study-assistant/ui/index.html)", "text/plain")
            return
        self._bytes(200, f.read_bytes(), "text/html; charset=utf-8")

    def _api_status(self):
        models = list_models()
        self._json(200, {
            "ollama": models is not None,
            "chat_model": CHAT_MODEL,
            "embed_model": EMBED_MODEL,
            "can_generate": models is not None and model_present(CHAT_MODEL, models),
            "can_embed": models is not None and model_present(EMBED_MODEL, models),
            "index": INDEX_PATH.exists(),
        })

    def _valid_page(self, path: str) -> Path | None:
        if not path or not path.endswith(".md") or ".." in path.split("/"):
            return None
        full = (REPO_ROOT / path).resolve()
        try:
            full.relative_to(REPO_ROOT)
        except ValueError:
            return None
        return full if full.exists() else None

    def _api_page(self, path: str):
        full = self._valid_page(path)
        if not full:
            self._json(404, {"error": "page not found"})
            return
        toc = build_toc()
        flat = _flat_pages(toc)
        prev = nxt = None
        if path in flat:
            idx = flat.index(path)
            prev = flat[idx - 1] if idx > 0 else None
            nxt = flat[idx + 1] if idx < len(flat) - 1 else None
        self._json(200, {
            "path": path,
            "title": _page_title(full),
            "html": markdown_to_html(full.read_text(encoding="utf-8"), path),
            "prev": prev,
            "next": nxt,
        })

    def _api_quiz(self, topic, path):
        cards = parse_flashcards()
        if topic:
            t = topic.lower()
            cards = [c for c in cards if t in c["topic"].lower()]
        elif path:
            full = REPO_ROOT / path
            title = _page_title(full).lower() if full.exists() else ""
            words = set(re.findall(r"[a-z]+", title)) - STOPWORDS
            match = [c for c in cards if words & set(re.findall(r"[a-z]+", c["topic"].lower()))]
            cards = match or cards
        self._json(200, {"cards": cards})

    def _api_ask(self, body):
        question = (body.get("question") or "").strip()
        page = body.get("path")
        if not question:
            self._json(400, {"error": "empty question"})
            return
        try:
            index = get_index()
        except FileNotFoundError:
            self._stream_open()
            self._stream({"type": "error",
                          "message": "No index yet. Run: python3 study_assistant.py build"})
            return
        models = list_models()
        can_embed = models is not None and model_present(EMBED_MODEL, models)
        can_generate = models is not None and model_present(CHAT_MODEL, models)

        query = question
        if page and (REPO_ROOT / page).exists():
            query = f"{_page_title(REPO_ROOT / page)} {question}".strip()
        chunks, mode = retrieve(index, query, DEFAULT_TOP_K, can_embed)

        self._stream_open()
        seen, sources = set(), []
        for ch in chunks:
            key = (ch["file"], ch["heading"])
            if key not in seen:
                seen.add(key)
                sources.append({"file": ch["file"], "heading": ch["heading"]})
        self._stream({"type": "sources", "mode": mode, "sources": sources,
                      "can_generate": can_generate})

        if can_generate and chunks:
            prompt = (
                f"Context sections from the repo:\n\n{format_context(chunks)}\n\n"
                f"Question: {question}\n\n"
                "Answer using only the context above, and cite source files in square brackets."
            )
            for frag in generate_stream(prompt):
                self._stream({"type": "token", "text": frag})
        else:
            for ch in chunks:
                snip = ch["text"].strip()
                if len(snip) > 700:
                    snip = snip[:700].rstrip() + " …"
                self._stream({"type": "section", "file": ch["file"],
                              "heading": ch["heading"], "text": snip})
        self._stream({"type": "done"})

    def _api_grade(self, body):
        q, ref, ans = body.get("question", ""), body.get("reference", ""), body.get("answer", "")
        if not (model_present(CHAT_MODEL)):
            self._json(200, {"grade": None, "can_generate": False})
            return
        prompt = (
            f"Question: {q}\nReference answer: {ref}\nStudent answer: {ans}\n\n"
            "On the first line say Correct, Partially correct, or Incorrect. Then give one "
            "sentence of specific, encouraging feedback."
        )
        out = "".join(generate_stream(prompt, system="You are a fair, encouraging quiz grader."))
        self._json(200, {"grade": out.strip(), "can_generate": True})

    def _api_gen_question(self, body):
        full = self._valid_page(body.get("path", ""))
        if not full:
            self._json(400, {"error": "bad path"})
            return
        if not model_present(CHAT_MODEL):
            cards = parse_flashcards()
            title = _page_title(full).lower()
            words = set(re.findall(r"[a-z]+", title)) - STOPWORDS
            pick = next((c for c in cards
                         if words & set(re.findall(r"[a-z]+", c["topic"].lower()))), None)
            if pick:
                self._json(200, {"question": pick["q"], "reference": pick["a"], "generated": False})
            else:
                self._json(200, {"question": None, "can_generate": False})
            return
        text = full.read_text(encoding="utf-8")[:4000]
        prompt = (
            "Based on this study page, write ONE open-ended, interview-style question that tests "
            "real understanding (not trivia). Then on a new line write 'ANSWER:' followed by a "
            f"concise model answer.\n\nPage:\n{text}"
        )
        out = "".join(generate_stream(
            prompt, system="You write incisive system-design interview questions."))
        q, a = out, ""
        if "ANSWER:" in out:
            q, a = out.split("ANSWER:", 1)
        self._json(200, {"question": q.strip(), "reference": a.strip(), "generated": True})

    # -- interview mode: the LLM plays the interviewer --
    def _interview_topic(self, body) -> str:
        path = body.get("path")
        if path and (REPO_ROOT / path).exists():
            return _page_title(REPO_ROOT / path)
        return body.get("topic") or "system design"

    def _interview_context(self, topic: str) -> str:
        try:
            index = get_index()
        except FileNotFoundError:
            return ""
        chunks, _ = retrieve(index, topic, 4, model_present(EMBED_MODEL))
        return format_context(chunks)

    @staticmethod
    def _transcript_text(transcript: list, limit: int | None = None) -> str:
        turns = transcript[-limit:] if limit else transcript
        return "\n".join(
            ("Interviewer: " if t.get("role") == "interviewer" else "Candidate: ") + t.get("text", "")
            for t in turns
        )

    def _api_interview(self, body):
        transcript = body.get("transcript") or []
        topic = self._interview_topic(body)
        self._stream_open()
        self._stream({"type": "topic", "topic": topic})
        if not model_present(CHAT_MODEL):
            self._stream({"type": "error",
                          "message": f"Interview Mode needs a local model — run: ollama pull {CHAT_MODEL}"})
            self._stream({"type": "done"})
            return
        context = self._interview_context(topic)
        convo = self._transcript_text(transcript, limit=12)
        if not transcript:
            task = (f"Begin a mock system design interview on: {topic}. Give a one-line framing, "
                    "then ask your FIRST question (usually clarifying requirements/scope). "
                    "2-3 sentences total.")
        else:
            task = ("Continue as interviewer. Based on the candidate's last answer, ask ONE focused "
                    "follow-up that probes scale, a bottleneck, or a trade-off they glossed over. "
                    "Do not lecture or give the answer. 1-3 sentences. If the design is now "
                    "thoroughly covered, say you're wrapping up and to click 'Score me'.")
        system = ("You are a senior staff engineer running a rigorous but friendly system design "
                  "interview. Ask one question at a time. Never hand over the model answer; draw the "
                  "candidate out. Use the reference notes only to know what a strong answer covers.")
        prompt = (f"Reference notes (for your eyes only):\n{context}\n\n"
                  f"Transcript so far:\n{convo or '(none yet)'}\n\n{task}")
        for frag in generate_stream(prompt, system=system):
            self._stream({"type": "token", "text": frag})
        self._stream({"type": "done"})

    def _api_interview_score(self, body):
        transcript = body.get("transcript") or []
        topic = self._interview_topic(body)
        if not model_present(CHAT_MODEL):
            self._json(200, {"feedback": None, "can_generate": False})
            return
        context = self._interview_context(topic)
        prompt = (
            f"Reference notes:\n{context}\n\nTopic: {topic}\n\n"
            f"Full transcript:\n{self._transcript_text(transcript)}\n\n"
            "Write structured post-interview feedback using these exact markdown headers:\n"
            "### Verdict\n(Strong hire / Hire / Lean hire / No hire — plus one sentence)\n"
            "### Covered well\n(bullets, cite what they said)\n"
            "### Gaps and what to add\n(bullets tied to the framework: requirements, estimation, "
            "API, data model, high-level design, deep dive, bottlenecks/trade-offs)\n"
            "### Practice next\n(one concrete bullet)"
        )
        system = ("You are a fair, specific, encouraging system design interviewer writing "
                  "post-interview feedback grounded in what the candidate actually said.")
        out = "".join(generate_stream(prompt, system=system))
        self._json(200, {"feedback": out.strip(), "can_generate": True, "topic": topic})


def serve(host: str = "127.0.0.1", port: int = 8000, open_browser: bool = True) -> None:
    if not (UI_DIR / "index.html").exists():
        sys.exit(yellow(f"UI file missing: {UI_DIR / 'index.html'}"))
    note = "index ready" if INDEX_PATH.exists() else "no index yet — run 'build' for AI answers"
    models = list_models()
    llm = (green(f"Ollama up ({CHAT_MODEL})") if models is not None and model_present(CHAT_MODEL, models)
           else yellow("Ollama/model not detected — browse + keyword search still work"))
    url = f"http://{host}:{port}"
    try:
        httpd = ThreadingHTTPServer((host, port), _StudyHandler)
    except OSError as e:
        sys.exit(yellow(f"Could not bind {url} ({e}). Try a different --port."))
    print(bold("Study UI: ") + cyan(url) + dim(f"  ·  {note}  ·  ") + llm)
    print(dim("Press Ctrl-C to stop."))
    if open_browser:
        try:
            import threading
            import webbrowser
            threading.Timer(0.7, lambda: webbrowser.open(url)).start()
        except Exception:  # noqa: BLE001
            pass
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n" + dim("stopped."))
        httpd.shutdown()


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
            "  python3 study_assistant.py serve            # open the web UI\n"
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
    s = sub.add_parser("serve", help="launch the local web study UI")
    s.add_argument("--port", type=int, default=8000, help="port (default 8000)")
    s.add_argument("--host", default="127.0.0.1", help="bind host (default 127.0.0.1)")
    s.add_argument("--no-open", action="store_true", help="don't auto-open the browser")
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
    elif args.command == "serve":
        serve(args.host, args.port, not args.no_open)
    else:
        build_parser().print_help()


if __name__ == "__main__":
    main()
