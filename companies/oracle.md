# Oracle: system design interview

> How Oracle actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Oracle runs it.** Loops vary by organization: OCI runs a modern distributed-systems interview (multi-tenant cloud services, replication, consistency), while application orgs lean toward practical enterprise design. Find out which Oracle you are interviewing with before preparing.

## Signature questions

- Design a multi-tenant cloud service with isolation and quota enforcement
- Design replicated storage with explicit consistency tradeoffs
- Design enterprise data pipelines or reporting systems

## What interviewers probe

- Consistency and durability reasoning at database-company depth
- Multi-tenancy as the first constraint
- Enterprise reliability: upgrades, backwards compatibility, and audit

## Prepare

- Patterns to review: [replication](../patterns/replication.md), [consistency models](../patterns/consistency-models.md), [sharding partitioning](../patterns/sharding-partitioning.md), [quorum](../patterns/quorum.md)
- Practice questions: [Design amazon s3](../questions/design-amazon-s3.md), [Design distributed cache](../questions/design-distributed-cache.md)
- Full company guide: [Oracle system design interview](https://www.designgurus.io/answers/detail/what-are-the-top-system-design-interview-questions-for-oracle-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
