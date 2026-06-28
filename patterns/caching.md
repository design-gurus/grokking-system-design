# Caching

> Store the results of expensive work close to where they are needed, so repeated reads are fast and cheap.

## What it is

A cache is a fast, usually in-memory store that holds copies of data so that future requests can be served without hitting the slower source of truth (a database, a downstream service, or a computation). Caching trades a small amount of memory and some risk of staleness for large gains in read latency and throughput.

## When to use it

- Read-heavy workloads where the same data is requested often.
- Expensive reads (complex queries, downstream calls, heavy computation).
- Data that tolerates being slightly stale (profiles, product catalogs, feeds).
- Hot keys that would otherwise overload the data store.

## Where caches live

- Client side (browser, app memory).
- CDN or edge (static assets, see [CDN](cdn.md)).
- Application or service layer (in-process or a shared cache like Redis or Memcached).
- Database layer (query and buffer caches).

## Caching strategies

| Strategy | How it works | Best for |
|----------|--------------|----------|
| Cache-aside (lazy) | App reads cache, on miss reads the DB and populates the cache | General read-heavy workloads |
| Read-through | The cache itself loads from the DB on a miss | Simpler app code, cache library handles loads |
| Write-through | Writes go to the cache and the DB together | Read-after-write consistency, slower writes |
| Write-back (write-behind) | Writes go to the cache, flushed to the DB later | Write-heavy, can tolerate some loss risk |

## Eviction policies

When the cache is full, something must go. Common policies: LRU (least recently used), LFU (least frequently used), FIFO, and TTL-based expiry. LRU is the common default.

## Trade-offs

| Pro | Con |
|-----|-----|
| Much lower read latency | Risk of serving stale data |
| Less load on the data store | Cache invalidation is hard |
| Cheap to scale reads | Extra moving part to operate and monitor |

## The hard parts to mention in an interview

- Invalidation: how do you keep the cache fresh? (TTLs, write-through, explicit invalidation on update.)
- The thundering herd or cache stampede: when a hot key expires, many requests hit the DB at once. Mitigations: request coalescing, staggered TTLs, locks.
- Consistency: what is the staleness budget for this data? State it explicitly.

## Go deeper

- Read more (free): [Caching in System Design Interviews](https://www.designgurus.io/blog/caching-system-design-interview)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)