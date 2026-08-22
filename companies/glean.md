# Glean: system design interview

> How Glean actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Glean runs it.** Enterprise search is the entire question space, and permission-aware retrieval is the signature problem. Expect about 60 minutes inside the onsite loop covering indexing content from many workplace tools, keeping that index fresh under per-app rate limits, and mixing keyword matching with embeddings before a rerank. A design that could leak one document fails, so the deny-by-default rule and permission filtering ahead of ranking belong early in your answer.

## Signature questions

- Design permission-aware enterprise search
- Design federated indexing across chat, documents, and tickets
- Design incremental ingestion so edits appear within minutes
- Design hybrid ranking that merges keyword and embedding results
- Design the layer that lets an AI assistant call search and other tools

## What interviewers probe

- Safety first: deny by default, and filter by permission before anything is ranked
- Realistic connectors: per-app rate limits, partial failures, and retries per source
- Ranking literacy: working knowledge of keyword search plus embeddings, not research depth
- Numbers: document counts, query latency targets, and index update delay, stated and defended

## Prepare

- Patterns to review: [database indexing](../patterns/database-indexing.md), [message queues](../patterns/message-queues.md), [rate limiting](../patterns/rate-limiting.md), [sharding partitioning](../patterns/sharding-partitioning.md), [caching](../patterns/caching.md)
- Practice questions: [Design semantic search](../questions/design-semantic-search.md), [Design google search](../questions/design-google-search.md), [Design web crawler](../questions/design-web-crawler.md), [Design rag pipeline](../questions/design-rag-pipeline.md)
- Full company guide: [Glean system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-glean-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
