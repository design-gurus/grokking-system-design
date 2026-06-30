# System design in one page

> The whole framework, the key patterns, and the numbers, condensed. Bookmark this. Expand any line through the links.

## The framework (45-minute round)

| # | Step | Time |
|---|------|------|
| 1 | Requirements and scope: functional and non-functional, confirm scope | 5 min |
| 2 | Estimation: QPS, storage, read-to-write ratio | 3 min |
| 3 | API: the core endpoints | 4 min |
| 4 | Data model: entities and the store that fits the access patterns | 5 min |
| 5 | High-level design: boxes and arrows, one request end to end | 10 min |
| 6 | Deep dive: one or two components | 13 min |
| 7 | Bottlenecks and trade-offs | 5 min |

Full version: [interview framework](interview-framework.md).

## Numbers to know

| Operation | Time |
|-----------|------|
| Memory reference | ~100 ns |
| SSD random read | ~100 us |
| Round trip in a data center | ~500 us |
| Disk seek | ~10 ms |
| Round trip between continents | ~150 ms |

- Powers of two: 2^10 is ~1 KB, 2^20 ~1 MB, 2^30 ~1 GB, 2^40 ~1 TB.
- 1 day is ~86,400 seconds (use 100,000). "X per day" / 100,000 is roughly "X per second".
- Availability: 99.9% is ~8.7 hours of downtime per year; 99.99% is ~52 minutes.

Full version: [estimation](estimation.md), [non-functional requirements](non-functional-requirements.md).

## Patterns, one line each

- [Caching](../patterns/caching.md): keep hot data in memory to cut read latency. Mind invalidation.
- [Load balancing](../patterns/load-balancing.md): spread traffic across servers, health-check and remove failed ones.
- [Sharding](../patterns/sharding-partitioning.md): split data across nodes by a shard key to scale writes and storage.
- [Replication](../patterns/replication.md): copy data to multiple nodes for availability and read scaling. Mind lag.
- [Consistency models](../patterns/consistency-models.md): pick the weakest the product tolerates (strong to eventual).
- [CAP](../patterns/cap-theorem.md): during a partition, choose consistency or availability.
- [Consistent hashing](../patterns/consistent-hashing.md): map keys to a ring so adding or removing a node moves few keys.
- [Message queues](../patterns/message-queues.md): decouple producers and consumers, absorb spikes, process async.
- [Rate limiting](../patterns/rate-limiting.md): cap requests per client (token bucket), return 429.
- [CDN](../patterns/cdn.md): cache content at the edge, close to users.
- [Database indexing](../patterns/database-indexing.md): speed reads by key at the cost of slower writes.
- [Bloom filter](../patterns/bloom-filters.md): a cheap "definitely not present" check before an expensive lookup.

## Key trade-offs

- Strong vs eventual consistency: strong for money and inventory, eventual for feeds and counts.
- Sync vs async: keep the request path synchronous only for what the user needs now.
- Push vs pull (fan-out): push for most users, pull for celebrities (hybrid).
- SQL vs NoSQL: choose by access pattern, justify from the requirements.
- Monolith vs microservices: start monolithic, split when scale and team size demand it.

Full version: [trade-offs](trade-offs.md).

## Pick a data store

- Key-value: sessions, caches, simple high-volume lookups.
- Document: catalogs, profiles, flexible content.
- Wide-column: time series, very high write volume.
- Graph: social graphs and relationship queries.
- Relational (SQL): transactions, joins, strong consistency.
- Object store: large blobs (images, video, files).
- Search index: full-text search and autocomplete.

Full version: [core components](core-components.md), [SQL vs NoSQL](sql-vs-nosql.md).

## Do not

- Jump into design before clarifying requirements.
- Skip estimation, or design in silence.
- Over-engineer, or add components nothing needs.
- Pick tech by buzzword without justifying it.
- Forget trade-offs, bottlenecks, and failure.

Full version: [common mistakes](common-mistakes.md), [communication tips](communication-tips.md).

## Go deeper

- Practice live: [mock interviews with ex-FAANG engineers](https://www.designgurus.io/mock-interviews)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)