# Databricks: system design interview

> How Databricks actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Databricks runs it.** Prompts start standard and then expand, layer after layer, until the interviewer finds where your understanding ends. Product-aware answers earn real credit: connecting your reasoning to how Spark or Delta Lake solves the same problem demonstrates depth no generic answer can.

## Signature questions

- A deceptively simple product prompt that expands (reported example: a cheapest-book-finder aggregating flaky distributor APIs)
- Design a large-scale ETL or streaming pipeline with exactly-once semantics and backpressure
- Design a versioned table store or metadata service (transaction logs, snapshot isolation, compaction)
- Design multi-tenant compute with noisy-neighbor control and fair scheduling

## What interviewers probe

- Depth on demand: do not draw boxes you cannot open
- Data correctness under failure: recomputable work, idempotent writes, honest exactly-once talk
- Performance mechanics: what gets shuffled, what is CPU versus I/O bound, what you would measure

## Prepare

- Patterns to review: [batch vs stream processing](../patterns/batch-vs-stream-processing.md), [sharding partitioning](../patterns/sharding-partitioning.md), [write ahead log](../patterns/write-ahead-log.md), [consistency models](../patterns/consistency-models.md)
- Practice questions: [Design ad click aggregator](../questions/design-ad-click-aggregator.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md)
- Full company guide: [Databricks system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-databricks-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
