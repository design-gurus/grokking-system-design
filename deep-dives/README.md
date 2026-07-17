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
| [Spanner](spanner-global-sql.md) | Globally consistent SQL (TrueTime) | Written |
| [Raft](raft-consensus.md) | Understandable consensus (replicated log) | Written |
| [MapReduce](mapreduce-batch-processing.md) | Batch processing on commodity clusters | Written |
| [ZooKeeper](zookeeper-coordination.md) | Coordination as a service (open-source Chubby) | Written |
| [Memcached at Facebook](memcached-at-facebook.md) | Look-aside caching at planet scale | Written |
| [Aurora](aurora-cloud-native-database.md) | Cloud-native relational storage (the log is the database) | Written |
| [DynamoDB](dynamodb-managed-nosql.md) | Managed NoSQL with predictable latency (2022 paper) | Written |

## How these relate to the patterns

These systems are where the [patterns](../patterns/) come together: Dynamo and Cassandra use [consistent hashing](../patterns/consistent-hashing.md) and [replication](../patterns/replication.md) with [tunable consistency](../patterns/consistency-models.md); BigTable runs on GFS and uses Chubby; Kafka is a [message queue](../patterns/message-queues.md) built as a replicated log. Raft is the consensus behind [leader election](../patterns/leader-election.md) in etcd and ZooKeeper's cousins; Spanner and Aurora are two different answers to replicating a [write-ahead log](../patterns/write-ahead-log.md); Memcached at Facebook is the [caching pattern](../patterns/caching.md) operated at its limit.

## Suggested reading order

1. Storage foundations: GFS → BigTable → Dynamo.
2. Open-source counterparts: HDFS, Cassandra, ZooKeeper.
3. Coordination and consensus: Chubby → ZooKeeper → Raft.
4. Modern managed databases: DynamoDB, Aurora, Spanner.
5. Infrastructure at scale: Kafka, MapReduce, Memcached at Facebook.

## Add a new deep dive

1. Copy [_template.md](_template.md) to `deep-dives/your-system.md`.
2. Fill in each section in your own words (do not copy paid or paper content verbatim).
3. Add a row above.