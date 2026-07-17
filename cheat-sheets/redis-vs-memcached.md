# Redis vs Memcached

How to choose an in-memory store, and how to justify it in an interview. Short version: Memcached is a pure [cache](../patterns/caching.md); Redis is a data-structure server that also caches. If the answer is not obvious, ask whether you need anything besides GET and SET.

## Quick comparison

| Dimension | Redis | Memcached |
|-----------|-------|-----------|
| Data model | Strings, hashes, lists, sets, sorted sets, streams, pub/sub | Strings (bytes) only |
| Threading | Mostly single-threaded event loop (I/O threads in newer versions) | Multi-threaded; scales up on one box |
| Persistence | Optional (RDB snapshots, AOF log) | None; a restart is a cold cache |
| Replication / HA | Built in ([replication](../patterns/replication.md), Sentinel, Redis Cluster) | None built in; clients shard with [consistent hashing](../patterns/consistent-hashing.md) |
| Eviction | Configurable policies, TTL per key | LRU with slab allocation; TTL per key |
| Atomic operations | Rich: INCR, compare-ops via Lua scripts, transactions | INCR/DECR, CAS |
| Memory efficiency for plain strings | Good | Slightly better (simpler allocator, less metadata) |

## How to choose

1. Pure look-aside cache for serialized blobs, biggest possible throughput per node, simplest ops → Memcached. This is the [Facebook use case](../deep-dives/memcached-at-facebook.md).
2. You need the data structures → Redis, and name the mapping: sorted sets for leaderboards, INCR with expiry for [rate limiting](../patterns/rate-limiting.md), lists/streams for lightweight queues, sets for presence.
3. Cache that must survive restarts, or cache plus source-of-truth-ish state (sessions you cannot lose) → Redis with persistence and replicas.
4. Distributed locks → Redis (SET NX with expiry), with the caveats in [distributed locking](../patterns/distributed-locking.md).
5. Both are RAM-priced: if the working set does not fit in memory, neither is the answer; fix the data model or use a disk store.

## What interviewers probe

- Cache invalidation: delete-on-write vs TTL-only, and what staleness window the product tolerates.
- Thundering herd on hot-key expiry: request coalescing, jittered TTLs, or leases (Memcached's lease trick).
- Redis single-threaded caveat: one slow command (KEYS, huge SMEMBERS) stalls everything; big values and scan-style commands are the classic self-inflicted outage.
- Failure semantics: Memcached loss is a performance event (cold cache, database takes the misses); Redis-as-state loss is a correctness event. Decide which one you are running.

## How to talk about it in an interview

Do not say "I would add Redis because it is fast". Say "this is a read-heavy feed; I need a look-aside cache for rendered cards keyed by post id, TTL plus delete-on-write, and nothing fancier, so Memcached (or Redis used as a plain cache) behind consistent hashing. Separately, the leaderboard needs sorted sets, so that specific feature runs on Redis." Choosing per workload, not per brand, is the senior signal.

## Go deeper

- [Caching pattern](../patterns/caching.md) and the [Memcached at Facebook deep dive](../deep-dives/memcached-at-facebook.md)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)