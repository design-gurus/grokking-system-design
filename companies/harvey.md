# Harvey: system design interview

> How Harvey actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Harvey runs it.** Legal constraints are the grading rubric: results must respect matter-level permissions, and answers must cite the source text they came from. Reported themes are document ingestion pipelines, hybrid keyword and vector search, permission systems, collaborative editing, and high volume model-backed APIs. This is one of four onsite rounds, and candidates who raise confidentiality and citation accuracy before being asked do best.

## Signature questions

- Design search over a law firm's document set
- Design an ingestion pipeline that extracts, chunks, and indexes many file formats
- Design a permission system that keeps matters strictly separated
- Design collaborative editing and commenting for several lawyers on one document
- Design a high volume model-backed API with rate limits and predictable latency

## What interviewers probe

- Constraint thinking: permissions and accuracy raised first, not treated as optional features
- Permission filtering before ranking, since filtering after can leak that a document exists
- Trade-offs spoken aloud: keyword versus vector, latency versus quality, cost versus freshness
- Measurement: a test set of real questions, with citation accuracy tracked and not just relevance

## Prepare

- Patterns to review: [database indexing](../patterns/database-indexing.md), [sharding partitioning](../patterns/sharding-partitioning.md), [message queues](../patterns/message-queues.md), [caching](../patterns/caching.md), [rate limiting](../patterns/rate-limiting.md)
- Practice questions: [Design semantic search](../questions/design-semantic-search.md), [Design rag pipeline](../questions/design-rag-pipeline.md), [Design google docs](../questions/design-google-docs.md), [Design dropbox](../questions/design-dropbox.md)
- Full company guide: [Harvey system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-harvey-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
