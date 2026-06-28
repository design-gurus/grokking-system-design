# Design a distributed cache (like Redis)

> An in-memory key-value cache spread across many nodes, for fast reads and reduced load on the data store.

## Requirements

- Fast get and set by key.
- Scale beyond one machine's memory.
- Handle node failures without losing the whole cache.
- An eviction policy when memory is full.

## Key ideas

- Partitioning: spread keys across nodes with [consistent hashing](../patterns/consistent-hashing.md) so adding or removing a node moves few keys.
- Replication: replicate each shard so a node failure does not lose its data (see [replication](../patterns/replication.md)).
- Eviction: LRU is the common default; also support TTL expiry.
- Consistency: caches are usually best-effort, so plan invalidation (see [caching](../patterns/caching.md)) and accept brief staleness.

## Go deeper

- Read more (free): [Ultimate Guide to Redis in System Design](https://www.designgurus.io/blog/redis-guide)
- Quick, focused prep: [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)