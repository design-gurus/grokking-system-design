# Confluent: system design interview

> How Confluent actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Confluent runs it.** Follow ups go past the component diagram and into guarantees: what a client sees when a node dies mid write, and whether ordering survives it. The round runs about an hour on distributed data systems, and the signature prompt is a message queue or event log that mirrors Kafka itself. Retention and replay belong in the answer, and a casual promise of exactly once delivery costs credibility fast.

## Signature questions

- Design a message queue or event log
- Design a real time analytics pipeline that feeds dashboards within seconds
- Design a durable, queryable audit trail
- Design event driven microservices that communicate through streams

## What interviewers probe

- Scale, ordering needs, and retention asked about before any boxes are drawn
- Precise use of partition, replication, leader and follower, and delivery guarantee
- Failure reasoning per component: what breaks, and what the client sees
- Honest trade-offs on durability against latency and ordering against parallelism

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [replication](../patterns/replication.md), [leader election](../patterns/leader-election.md), [write ahead log](../patterns/write-ahead-log.md), [idempotency](../patterns/idempotency.md)
- Practice questions: [Design distributed message queue](../questions/design-distributed-message-queue.md), [Design ad click aggregator](../questions/design-ad-click-aggregator.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md)
- Full company guide: [Confluent system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-confluent-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
