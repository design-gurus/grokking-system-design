"""Tests for the study assistant: markdown rendering, flashcard parsing,
retrieval, the resource TOC, search ranking, and a repo-wide Mermaid check.

Run from anywhere:  python -m pytest tools/study-assistant/tests -q
"""

import pathlib
import re
import sys

# Make `study_assistant` importable without installing anything.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import study_assistant as sa  # noqa: E402


# --------------------------------------------------------------------------- #
# Markdown -> HTML renderer
# --------------------------------------------------------------------------- #

def test_markdown_heading_bold_code():
    html = sa.markdown_to_html("# Title\n\nSome **bold** and `code`.", "patterns/x.md")
    assert '<h1 id="title">Title</h1>' in html
    assert "<strong>bold</strong>" in html
    assert "<code>code</code>" in html


def test_markdown_table():
    html = sa.markdown_to_html("| A | B |\n|---|---|\n| 1 | 2 |", "x.md")
    assert "<table>" in html
    assert "<th>A</th>" in html
    assert "<td>1</td>" in html


def test_markdown_mermaid_block_becomes_div():
    html = sa.markdown_to_html("```mermaid\nflowchart LR\n  A-->B\n```", "x.md")
    assert '<div class="mermaid">' in html
    assert "flowchart LR" in html


def test_markdown_code_block_is_escaped():
    html = sa.markdown_to_html("```python\nprint('<hi>')\n```", "x.md")
    assert '<pre><code class="language-python">' in html
    assert "&lt;hi&gt;" in html


def test_markdown_nested_list():
    html = sa.markdown_to_html("- a\n  - a1\n- b", "x.md").replace("\n", "")
    assert "<li>a<ul><li>a1</li></ul></li>" in html


def test_internal_md_link_is_rewritten_for_in_app_nav():
    html = sa.markdown_to_html("See [caching](../patterns/caching.md).", "fundamentals/x.md")
    assert 'data-nav="patterns/caching.md"' in html


def test_external_link_opens_new_tab():
    html = sa.markdown_to_html("[site](https://example.com)", "x.md")
    assert 'target="_blank"' in html
    assert 'href="https://example.com"' in html


def test_raw_html_in_text_is_escaped():
    html = sa.markdown_to_html("a <script>alert(1)</script> b", "x.md")
    assert "<script>" not in html
    assert "&lt;script&gt;" in html


# --------------------------------------------------------------------------- #
# Flashcards
# --------------------------------------------------------------------------- #

def test_flashcards_parse_cleanly():
    cards = sa.parse_flashcards()
    assert len(cards) >= 20
    assert all(c["q"] and c["a"] and c["topic"] for c in cards)
    # the "Go deeper" trailer must not leak in as a card/topic
    assert not any(c["topic"] == "Go deeper" for c in cards)


# --------------------------------------------------------------------------- #
# Resource TOC
# --------------------------------------------------------------------------- #

def test_build_toc_contains_expected_sections():
    toc = sa.build_toc()
    labels = [s["label"] for s in toc]
    assert "Fundamentals" in labels
    assert "Low-level design" in labels
    lld = next(s for s in toc if s["label"] == "Low-level design")
    files = [p["path"] for p in lld["pages"]]
    assert "low-level-design/parking-lot.md" in files
    assert all(p["title"] for p in lld["pages"])


def test_flat_pages_are_unique_and_plentiful():
    flat = sa._flat_pages(sa.build_toc())
    assert len(flat) > 100
    assert flat == list(dict.fromkeys(flat))  # no duplicates


# --------------------------------------------------------------------------- #
# Retrieval (keyword fallback path — no Ollama needed)
# --------------------------------------------------------------------------- #

def _mini_index(chunks):
    df = {}
    for ch in chunks:
        for tok in set(ch["tokens"]):
            df[tok] = df.get(tok, 0) + 1
    return {"num_chunks": len(chunks), "doc_freq": df, "chunks": chunks}


def test_retrieve_keyword_ranks_relevant_chunk_first():
    chunks = [
        {"file": "a.md", "title": "A", "heading": "Cache aside",
         "text": "cache aside reads the cache then the database",
         "tokens": sa.tokenize("cache aside reads the cache then the database")},
        {"file": "a.md", "title": "A", "heading": "Eviction",
         "text": "lru evicts the least recently used entry",
         "tokens": sa.tokenize("lru evicts the least recently used entry")},
    ]
    got, mode = sa.retrieve(_mini_index(chunks), "eviction lru", top_k=1, can_embed=False)
    assert mode == "keyword"
    assert got and got[0]["heading"] == "Eviction"


# --------------------------------------------------------------------------- #
# Search
# --------------------------------------------------------------------------- #

def test_search_ranks_title_match_first():
    res = sa.search("consistent hashing")
    assert res
    assert res[0]["file"] == "patterns/consistent-hashing.md"


def test_search_empty_query_returns_nothing():
    assert sa.search("") == []


# --------------------------------------------------------------------------- #
# Repo-wide Mermaid structural validation
# --------------------------------------------------------------------------- #

_DIAGRAM_TYPES = (
    "flowchart", "graph", "sequenceDiagram", "stateDiagram", "classDiagram",
    "erDiagram", "gantt", "pie", "journey", "mindmap", "gitGraph",
)


def _mermaid_blocks():
    root = pathlib.Path(sa.REPO_ROOT)
    for md in root.rglob("*.md"):
        if ".git" in md.parts or "node_modules" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for block in re.findall(r"```mermaid\n(.*?)```", text, re.S):
            yield md.relative_to(root), block


def test_every_mermaid_block_has_a_valid_header():
    bad = []
    for rel, block in _mermaid_blocks():
        first = block.strip().splitlines()[0].strip() if block.strip() else ""
        if not first.startswith(_DIAGRAM_TYPES):
            bad.append(f"{rel}: {first!r}")
    assert not bad, bad


def test_flowchart_subgraphs_are_balanced():
    bad = []
    for rel, block in _mermaid_blocks():
        if "subgraph" in block:
            opens = len(re.findall(r"(?m)^\s*subgraph\b", block))
            ends = len(re.findall(r"(?m)^\s*end\s*$", block))
            if opens != ends:
                bad.append(f"{rel}: {opens} subgraph vs {ends} end")
    assert not bad, bad
