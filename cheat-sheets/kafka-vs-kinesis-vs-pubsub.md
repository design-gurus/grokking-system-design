# Kafka vs Kinesis vs Pub/Sub

How to choose an event streaming platform when the realistic answer is a managed cloud service as often as it is running Kafka. The three are cousins, not clones: Kafka is a partitioned log you operate (or pay someone to), Kinesis is AWS's shard-based stream, and Pub/Sub is Google's global topic service with no partitions to manage at all.

## Quick comparison

| Dimension | Kafka | Kinesis | Pub/Sub |
|-----------|-------|---------|---------|
| Model | Partitioned [commit log](../deep-dives/kafka-distributed-messaging.md); consumers track their own offsets | Sharded stream; consumers checkpoint per shard | Global topic and subscriptions; the service tracks acks |
| Capacity management | You size partitions and brokers, or use managed (MSK, Confluent) | Provisioned shards you split and merge, or on-demand mode | None; scales automatically |
| Ordering | Per partition, by key | Per shard, by partition key | Opt-in, per ordering key |
| Replay | Rewind to any offset within retention | Rewind to a timestamp within retention | Seek to a timestamp or snapshot within retention |
| Retention | Yours to configure: days to forever (compacted topics) | 24 hours by default, extendable to a year | Seven days by default, configurable to 31 |
| Throughput | Very high; add partitions | Per-shard limits (roughly 1 MB/s in, 2 MB/s out, shared across consumers unless you pay for enhanced fan-out) | High; ordering keys throttle to per-key limits |
| Ecosystem | Largest by far: Connect, Streams, and everything integrates with it | AWS-native: Lambda triggers, Firehose into S3 | GCP-native: Dataflow, BigQuery subscriptions |
| Portability | Runs anywhere; the API is an industry standard | AWS only | GCP only |
| Operations | Heaviest self-run; moderate managed | Low | Lowest |

## The one-question shortcut

Ask: do you need the log itself (replay, compaction, stream processing, portability), or just reliable delivery of events at scale?

- The log itself → Kafka, self-run or managed.
- Just delivery, on AWS → Kinesis. (If it is single-consumer work distribution, that is a queue: see [Kafka vs RabbitMQ vs SQS](kafka-vs-rabbitmq-vs-sqs.md).)
- Just delivery, on GCP → Pub/Sub.

## How to choose

1. Event backbone feeding many independent systems, event sourcing, stateful stream processing → Kafka. The retained log and the ecosystem are the product.
2. AWS shop moving clickstream or telemetry into the AWS analytics stack → Kinesis. Lambda and Firehose integrations do most of the work for you.
3. GCP shop, or you never want to think about capacity again → Pub/Sub. There are no shards to size, and it scales while you sleep.
4. Multi-cloud today, or exit cost matters → Kafka. Both clouds will host it, and your code moves with you.
5. Strict global ordering → none of them at scale. Order is per partition, per shard, or per key. Design keys so order only matters within one.

## What interviewers probe

- Hot shards and hot keys: one loud key concentrates traffic on one partition or shard; the [sharding](../patterns/sharding-partitioning.md) trade-offs apply unchanged.
- Falling behind: what the signal is (consumer lag in Kafka, iterator age in Kinesis, oldest unacked message age in Pub/Sub) and what absorbs the backlog while you catch up.
- Exactly-once claims: all three are at-least-once by default. End-to-end exactly-once still requires [idempotent](../patterns/idempotency.md) consumers, whatever the marketing page says.
- Resharding: what happens to ordering and to in-flight consumers when a Kinesis shard splits, or when adding Kafka partitions changes the key-to-partition mapping.
- Cost shape: Kafka bills for infrastructure whether or not events flow, Kinesis bills per shard-hour plus payload, Pub/Sub bills per byte. A workload that is idle most of the day changes the answer.

## How to talk about it in an interview

Do not say "I would use Kafka because it handles streaming". Say "we are on AWS and the clickstream feeds Firehose into S3, so Kinesis on-demand is the least machinery for the job. If multiple downstream teams needed replayable history and stream processing, I would take on Kafka and its operational cost." Name the cloud, name the consumers, then justify the operational spend.

## Go deeper

- [Kafka deep dive](../deep-dives/kafka-distributed-messaging.md) and the [message queues pattern](../patterns/message-queues.md)
- Choosing a queue instead of a stream? [Kafka vs RabbitMQ vs SQS](kafka-vs-rabbitmq-vs-sqs.md)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)
