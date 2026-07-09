# Microsoft: system design interview

> How Microsoft actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Microsoft runs it.** Design rounds are structured and rubric-driven like the rest of the loop: enterprise-scale services, collaboration and productivity systems, and Azure-flavored infrastructure, with clear communication scored alongside architecture.

## Signature questions

- Design a collaboration service (documents, presence, comments) at enterprise scale
- Design cloud storage or a file-sharing system
- Design a notification or activity-feed system across a product suite

## What interviewers probe

- Structured narration: requirements, estimates, API, data model, deep dive, in visible order
- Enterprise concerns raised unprompted: tenancy, compliance, hybrid deployments
- Tradeoffs tied to user and business impact

## Prepare

- Patterns to review: [replication](../patterns/replication.md), [caching](../patterns/caching.md), [message queues](../patterns/message-queues.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design dropbox](../questions/design-dropbox.md), [Design google docs](../questions/design-google-docs.md)
- Full company guide: [Microsoft system design interview](https://www.designgurus.io/answers/detail/what-are-top-system-design-questions-for-microsoft-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
