# SQL vs NoSQL

How to choose a data store, and how to justify it in an interview. The right answer is always "it depends on the access patterns", so state the patterns first.

## Quick comparison

| Dimension | SQL (relational) | NoSQL |
|-----------|------------------|-------|
| Schema | Fixed, enforced | Flexible or schemaless |
| Joins and transactions | Strong, ACID | Limited; often [eventual consistency](../patterns/consistency-models.md) |
| Scaling | Vertical first; [sharding](../patterns/sharding-partitioning.md) is harder | Designed to scale horizontally |
| Best for | Complex queries, strong consistency, relationships | High write volume, simple lookups, flexible data |

## NoSQL families

| Family | Example use |
|--------|-------------|
| [Key-value](../deep-dives/dynamo-key-value-store.md) | Sessions, caches, simple lookups |
| Document | Catalogs, user profiles, content |
| [Wide-column](../deep-dives/cassandra-wide-column-db.md) | Time series, large-scale writes |
| Graph | Social graphs, recommendations |

## How to choose

1. Describe the access patterns: read vs write ratio, query shapes, consistency needs, scale.
2. If you need multi-row transactions, complex joins, and strong consistency, lean SQL.
3. If you need to scale writes horizontally with simple access patterns and flexible schema, lean NoSQL.
4. Many real systems use both: SQL for the core relational data, NoSQL for high-volume or flexible data.

## How to talk about it in an interview

Do not say "I would use NoSQL because it scales". Say "the access pattern is a key lookup by user id at high write volume with no joins, so a [wide-column store](../deep-dives/cassandra-wide-column-db.md) fits, and I accept eventual consistency here because the data tolerates it". Tie the choice to the requirements.

## Go deeper

See the data storage lessons in the [course](https://www.designgurus.io/course/grokking-the-system-design-interview).