# Snowflake: system design interview

> How Snowflake actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Snowflake runs it.** Distributed data systems with database-internals depth: storage formats, query execution, caching tiers, and multi-tenant resource isolation, in the architecture the company itself pioneered (storage separated from compute).

## Signature questions

- Design a data warehouse's storage/compute separation
- Design query scheduling with multi-tenant resource isolation
- Design a caching hierarchy for analytical workloads

## What interviewers probe

- Columnar and execution fundamentals for engine-adjacent teams
- Data-twist follow-ups: exceeds memory, arrives as streams, contains duplicates
- Cost and elasticity reasoning

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [caching](../patterns/caching.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md), [consistency models](../patterns/consistency-models.md)
- Practice questions: [Design distributed cache](../questions/design-distributed-cache.md), [Design ad click aggregator](../questions/design-ad-click-aggregator.md)
- Full company guide: [Snowflake system design interview](https://www.designgurus.io/answers/detail/what-are-the-top-system-design-interview-questions-for-snowflake-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
