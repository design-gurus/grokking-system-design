# Kafka: a distributed messaging system

> A distributed, replicated commit log that moves huge streams of events between systems with high throughput.

## What it is

Kafka is a durable, partitioned, append-only log. Producers append events to topics; consumers read them at their own pace. It is the backbone of many event-driven and streaming architectures, and a common answer when a design needs a [message queue](../patterns/message-queues.md) at scale.

## The problem it solves

Decoupling producers from consumers while handling millions of events per second durably, with replay (consumers can re-read history) and ordering within a partition.

## Key design ideas

| Idea | How it works |
|------|--------------|
| Topics and partitions | A topic is split into partitions; each partition is an ordered, append-only log |
| Offsets | Each message has a position; consumers track their own offset, so reads are independent |
| Consumer groups | Partitions are divided among a group, so consumers scale horizontally |
| Replication | Each partition has a leader and follower replicas for durability and failover |

## Notable techniques

- Sequential disk writes plus zero-copy transfer make it extremely fast despite using disk.
- Pull-based consumers (consumers fetch) let slow consumers fall behind without backpressure on producers.
- Retention by time or size lets the log act as a replayable source of truth.
- Ordering is guaranteed within a partition, not across partitions, so the partition key matters.

## Trade-offs

Very high throughput and durability, at the cost of per-partition ordering only and the operational weight of running a cluster.

## Go deeper

- Read more (free): [RabbitMQ vs Kafka vs ActiveMQ](https://www.designgurus.io/blog/rabbitmq-kafka-activemq-system-design)
- For the full deep dive: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)