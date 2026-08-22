# Kafka vs RabbitMQ vs SQS

How to choose a messaging system, and how to justify it in an interview. They are not three brands of the same thing: Kafka is a replicated log, RabbitMQ is a smart broker, SQS is a managed queue. Start from what the consumer needs.

## Quick comparison

| Dimension | Kafka | RabbitMQ | SQS |
|-----------|-------|----------|-----|
| Model | Distributed [commit log](../deep-dives/kafka-distributed-messaging.md); consumers track their own offset | Broker routes messages to queues; broker tracks delivery | Fully managed queue; at-least-once, near-unlimited scale |
| Message after consumption | Retained until retention expires (replayable) | Deleted once acked | Deleted once acked (within retention) |
| Ordering | Per partition | Per queue (weaker with concurrent consumers) | FIFO queues: per group; standard: best effort |
| Fan-out | Cheap: many consumer groups read the same log | Exchanges (fanout/topic routing) | Combine with SNS for fan-out |
| Throughput | Very high (sequential disk I/O, batching) | High, drops with routing complexity and large queues | High, per-queue quotas; FIFO much lower |
| Latency | Low ms, batching adds a little | Lowest of the three at modest scale | Higher (HTTP polling) |
| Operations | Heaviest (cluster, partitions), or managed | Moderate (broker, clustering) | Zero (fully managed) |
| Delayed / scheduled delivery | Not built in | Plugins, TTL tricks | Native delay up to 15 min |

## The one-question shortcut

Ask: do messages need to be replayed or consumed by multiple independent readers?

- Yes → Kafka (it is a log; consumption does not destroy data).
- No, it is work to be done once → a queue: RabbitMQ if you need routing, priorities, or per-message acks with low latency; SQS if you are on AWS and want zero operations.

## How to choose

1. Event stream feeding multiple systems (analytics, search indexing, caches) → Kafka. Consumer groups replay independently; retention is your safety net.
2. Task/job distribution (emails, thumbnails, work items) → a queue. SQS on AWS, RabbitMQ when you need routing keys, priorities, or dead-letter flows you control.
3. Event sourcing or audit trail → Kafka; the retained, ordered log is the feature.
4. Request buffering in front of a slow service → any of the three; pick by ops budget. Managed beats self-hosted unless you have a platform team.
5. Strict global ordering → none of them at scale. Ordering is per partition / per FIFO group; design keys so order matters only within a key.

## What interviewers probe

- Delivery semantics: all three are at-least-once by default; exactly-once needs [idempotent](../patterns/idempotency.md) consumers (dedup keys), not a checkbox on the broker.
- Backpressure: what happens when consumers fall behind? Kafka: lag grows, storage absorbs it. RabbitMQ: queues bloat and the broker degrades. SQS: messages age out after retention.
- Poison messages: dead-letter queues and max receive counts, or one bad message blocks a FIFO group.
- Hot partitions: Kafka ordering is per key; a celebrity key concentrates load ([sharding](../patterns/sharding-partitioning.md) logic applies to partitions too).

## How to talk about it in an interview

Do not say "I would use Kafka because it is scalable". Say "order events must be consumed by billing, analytics, and search independently, and I want replay when a consumer has a bug, so a retained log fits: Kafka. For the thumbnail worker pool, consumption is destructive work distribution, so a plain queue is simpler: SQS." Tie the choice to consumption semantics, then name the failure modes you are accepting.

## Go deeper

- [Kafka deep dive](../deep-dives/kafka-distributed-messaging.md) and the [message queues pattern](../patterns/message-queues.md)
- Choosing a managed cloud stream instead? [Kafka vs Kinesis vs Pub/Sub](kafka-vs-kinesis-vs-pubsub.md)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)