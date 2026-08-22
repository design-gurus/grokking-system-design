# Elastic: system design interview

> How Elastic actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Elastic runs it.** One concept sits under almost every question: the inverted index, and you should be able to draw it and explain it in plain words. The round runs about an hour by video and you lead it, with a workable split of ten minutes on requirements, fifteen on the high-level design, and twenty five on details and failures. Elastic engineers run large clusters daily, so node loss, replica promotion, and growing queue depth get real scrutiny rather than a passing mention.

## Signature questions

- Design a log search system for thousands of services
- Design full-text search with ranked, relevant results
- Design a metrics and alerting pipeline
- Design autocomplete that responds in milliseconds
- Design cluster sharding and replication that survives node failure

## What interviewers probe

- Volume, query rate, and latency numbers estimated before any design
- Recognizing that logs are write-heavy and time-ordered, and using time-based indices for it
- Failure paths described unprompted: dead node, slow indexer, traffic spike, recovery
- Explaining the inverted index or sharding so a non-specialist could follow

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [replication](../patterns/replication.md), [database indexing](../patterns/database-indexing.md), [message queues](../patterns/message-queues.md), [leader election](../patterns/leader-election.md)
- Practice questions: [Design typeahead autocomplete](../questions/design-typeahead-autocomplete.md), [Design google search](../questions/design-google-search.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design distributed message queue](../questions/design-distributed-message-queue.md)
- Full company guide: [Elastic system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-elastic-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
