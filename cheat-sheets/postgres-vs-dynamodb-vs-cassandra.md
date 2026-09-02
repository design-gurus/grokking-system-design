# PostgreSQL vs DynamoDB vs Cassandra

How to choose between the three stores that cover most interview answers: a relational database, a managed key-value service, and a write-optimized wide-column store. This is [SQL vs NoSQL](sql-vs-nosql.md) made concrete.

## Quick comparison

| Dimension | PostgreSQL | DynamoDB | Cassandra |
|-----------|------------|----------|-----------|
| Data model | Relational: tables, joins, constraints | Key-value / document; access by key ([deep dive](../deep-dives/dynamodb-managed-nosql.md)) | Wide-column; partition key plus clustering columns ([deep dive](../deep-dives/cassandra-wide-column-db.md)) |
| Query flexibility | Highest: ad hoc SQL, joins, aggregates, indexes | Low: design keys per access pattern, GSIs help | Low-medium: queries must follow the partition key |
| Consistency | ACID transactions, strong by default | Tunable per read; transactions cost extra | Tunable [quorums](../patterns/quorum.md); eventual by default |
| Scaling writes | Vertical first, then read replicas; [sharding](../patterns/sharding-partitioning.md) is on you | Automatic partitioning, effectively unbounded | Linear: add nodes, no leader ([replication](../patterns/replication.md) peer-to-peer) |
| Multi-region writes | Hard (single primary, or extensions) | Global tables (last-writer-wins) | Native multi-datacenter |
| Operations | Managed options everywhere; still needs tuning | Zero ops, AWS only | Heaviest self-op; managed versions exist |
| Cost shape | Cheap at small scale | Pay per request; predictable, can get expensive at high volume | Hardware plus expertise |

## How to choose

1. Default to PostgreSQL. Relational data, transactions, flexible queries, and decades of tooling cover the majority of systems, and a single beefy instance with read replicas goes further than candidates think (state the number: tens of thousands of transactions per second).
2. Access is by key, scale is huge or spiky, and you want zero operations → DynamoDB. Sessions, carts, user profiles, anything shaped like "get item by id" ([shopping cart](../questions/design-amazon-shopping-cart.md) territory).
3. Write volume is the defining load (time series, events, messages fan-in) and you can shape queries around a partition key → Cassandra. Its LSM write path absorbs write floods that would drown a B-tree.
4. Mixed needs → polyglot: PostgreSQL for the core relational entities, DynamoDB/Cassandra for the high-volume append-shaped data. Most real answers land here.

## What interviewers probe

- Key design: for DynamoDB and Cassandra, they will ask "how do you query X?" for an access pattern your key does not support. Enumerate access patterns before choosing keys; a missed one means a table redesign or an index.
- Hot partitions: a celebrity user or a monotonically increasing key concentrates load on one partition in both NoSQL stores; salt or spread the key.
- The join question: in key-value stores you denormalize; who updates the copies, and what happens when one update fails ([idempotency](../patterns/idempotency.md), background repair)?
- The Postgres ceiling: what breaks first (write IOPS on the primary, connection counts, table bloat) and what you do then (partitioning, sharding by tenant, or offloading the write-heavy table to Cassandra).

## How to talk about it in an interview

Do not say "Postgres does not scale, so NoSQL". Say "orders and payments need transactions and flexible queries: PostgreSQL. The clickstream is 500K writes per second, append-only, queried by (user, day): that is a Cassandra table with user id as partition key and time as clustering column. I am accepting eventual consistency on clicks because analytics tolerates it." Name the access pattern, then the store, then the consistency you gave up.

## Go deeper

- Deep dives: [DynamoDB](../deep-dives/dynamodb-managed-nosql.md), [Cassandra](../deep-dives/cassandra-wide-column-db.md), [Dynamo](../deep-dives/dynamo-key-value-store.md)
- Weighing a document store instead? [DynamoDB vs MongoDB](dynamodb-vs-mongodb.md)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=cheat-sheets-postgres-vs-dynamodb-vs-cassandra)