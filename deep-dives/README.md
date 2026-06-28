# Deep dives: real distributed systems

Case studies of landmark distributed systems, the kind of "how does X work" question that shows up in senior interviews and in [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii). Each file summarizes the key design ideas in plain language. For the full treatment, see the course.

| System | What it is | Status |
|--------|------------|--------|
| [Dynamo](dynamo-key-value-store.md) | Distributed key-value store (availability first) | Written |
| [Cassandra](cassandra-wide-column-db.md) | Wide-column NoSQL database | Written |
| [BigTable](bigtable-wide-column-store.md) | Wide-column storage on GFS | Written |
| [Kafka](kafka-distributed-messaging.md) | Distributed messaging and commit log | Written |
| [Chubby](chubby-distributed-locking.md) | Distributed locking and coordination | Written |
| [GFS](gfs-distributed-file-system.md) | Distributed file system for large files | Written |
| [HDFS](hdfs-file-storage.md) | Open-source distributed file storage | Written |

## How these relate to the patterns

These systems are where the [patterns](../patterns/) come together: Dynamo and Cassandra use [consistent hashing](../patterns/consistent-hashing.md) and [replication](../patterns/replication.md) with [tunable consistency](../patterns/consistency-models.md); BigTable runs on GFS and uses Chubby; Kafka is a [message queue](../patterns/message-queues.md) built as a replicated log.

## Add a new deep dive

1. Copy [_template.md](_template.md) to `deep-dives/your-system.md`.
2. Fill in each section in your own words (do not copy paid or paper content verbatim).
3. Add a row above.