# Study assistant — a local, offline AI tutor for this repo

> Ask questions about system design and get answers grounded in *this* repository, with citations — running entirely on your own machine. No API keys, no data leaves your laptop.

This is a small [retrieval-augmented generation](../../questions/design-rag-pipeline.md) (RAG) tool. It indexes every markdown page in the repo, finds the sections most relevant to your question, and asks a **local** LLM (via [Ollama](https://ollama.com)) to answer using only those sections — citing the source files so you can read the full page. It can also quiz you from the [flashcards deck](../../cheat-sheets/flashcards.md).

## How it works

```mermaid
flowchart LR
    subgraph Offline["100% local — nothing leaves your machine"]
      MD[Repo markdown] -->|build: chunk + embed| IDX[(index.json)]
      Q[Your question] -->|embed| R[Retrieve top-k]
      IDX --> R
      R -->|context| LLM[Local LLM via Ollama]
      LLM -->|grounded answer + citations| A[Answer]
    end
```

1. **build** — walks every `.md` file, splits it into heading-sized chunks, and (if Ollama is running) embeds each chunk with `nomic-embed-text`. The result is saved to `index.json` (git-ignored).
2. **ask / chat** — embeds your question, retrieves the most similar chunks (cosine similarity), and streams an answer from `llama3.2` constrained to that context, with `[file.md]` citations.
3. **quiz** — turns the flashcards into an interactive drill and (with Ollama) grades your answers.

**Graceful degradation:** no Ollama? The tool still works — it builds a keyword index and `ask` shows you the most relevant sections via TF-IDF search. Install Ollama later and rebuild for synthesized answers.

## Setup

### 1. Install Ollama (for AI answers — optional but recommended)

Download from [ollama.com](https://ollama.com), then pull the two small models:

```bash
ollama pull nomic-embed-text   # ~275 MB, for embeddings
ollama pull llama3.2           # ~2 GB, for answering (use llama3.2:1b for less RAM)
```

Ollama runs a local server at `127.0.0.1:11434`; the assistant talks only to that.

### 2. (Optional) install numpy for faster math

```bash
pip install -r requirements.txt
```

Everything works without it — pure-Python cosine similarity is the fallback.

## Usage

From this folder (`tools/study-assistant/`):

```bash
# 1. Build the index (re-run whenever the content changes)
python3 study_assistant.py build

# 2. Ask a one-off question
python3 study_assistant.py ask "when should I shard instead of adding read replicas?"

# 3. Interactive session
python3 study_assistant.py chat

# 4. Quiz yourself (optionally by topic)
python3 study_assistant.py quiz
python3 study_assistant.py quiz caching
```

### Example

```
$ python3 study_assistant.py ask "why must queue consumers be idempotent?"

Answer (semantic retrieval, llama3.2)

Most message queues deliver at-least-once, so the same message can arrive more
than once (retries, redelivery after a consumer crash). If processing isn't
idempotent, a duplicate delivery causes duplicate side effects — e.g. charging
a card twice. Making consumers idempotent (dedupe keys, upserts) means handling
a message twice has the same effect as once. [fundamentals/asynchronism.md]
[patterns/idempotency.md]

Sources:
  • fundamentals/asynchronism.md — What to watch for
  • patterns/idempotency.md — What it is
```

## Configuration

Override defaults with environment variables:

| Variable | Default | Purpose |
|----------|---------|---------|
| `OLLAMA_HOST` | `http://127.0.0.1:11434` | Where Ollama is listening |
| `SDA_EMBED_MODEL` | `nomic-embed-text` | Embedding model |
| `SDA_CHAT_MODEL` | `llama3.2` | Answering model (try `llama3.2:1b`, `qwen2.5:3b`, `phi3`) |

Add `--top-k N` to any command to change how many sections are retrieved.

## Privacy

Everything is local. The tool reads files from this repo and makes HTTP calls **only** to your Ollama server on `127.0.0.1`. There are no external API calls, no telemetry, and no API keys. The generated `index.json` stays on your disk and is git-ignored.

## Notes and limits

- It answers from repo content only — it's a study aid, not a general chatbot. If the repo doesn't cover something, it will say so.
- Answer quality tracks the local model you choose. `llama3.2` is a good default; smaller models are faster but terser.
- This mirrors the architecture taught in [Design a RAG pipeline](../../questions/design-rag-pipeline.md) and [Design semantic search](../../questions/design-semantic-search.md) — so the tool is also a worked example of the pattern.
