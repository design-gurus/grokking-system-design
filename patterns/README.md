# Patterns: the building blocks of system design

Learn these once and you can assemble an answer to almost any design question. Each file is a short, practical cheat sheet: what the pattern is, when to use it, the trade-offs, and how to talk about it in an interview.

| Pattern | What it solves | Status |
|---------|----------------|--------|
| [Caching](caching.md) | Read latency and load on the data store | Written |
| [Load balancing](load-balancing.md) | Distributing traffic across servers | Written |
| [Sharding and partitioning](sharding-partitioning.md) | Scaling data beyond one machine | Written |
| [Replication](replication.md) | Availability and read scaling | Written |
| [Consistency models](consistency-models.md) | Correctness under concurrency | Written |
| [CAP theorem](cap-theorem.md) | Reasoning about trade-offs under partitions | Written |
| [Consistent hashing](consistent-hashing.md) | Even distribution with minimal reshuffling | Written |
| [Message queues](message-queues.md) | Decoupling and async processing | Written |
| [Rate limiting](rate-limiting.md) | Protecting services from overload | Written |
| [CDN](cdn.md) | Serving static content close to users | Written |
| [Database indexing](database-indexing.md) | Fast lookups | Written |
| [Bloom filters](bloom-filters.md) | Cheap "definitely not present" checks | Written |
| [Proxies](proxies.md) | Intermediaries for routing, security, and caching | Written |
| [API gateway](api-gateway.md) | One entry point for auth, rate limiting, and routing | Written |
| [Long polling vs WebSockets vs SSE](long-polling-websockets-sse.md) | Pushing real-time updates to clients | Written |
| [Quorum](quorum.md) | Consistent reads and writes across replicas | Written |
| [Leader election](leader-election.md) | Agreeing on one node in charge, surviving failover | Written |
| [Heartbeats](heartbeats.md) | Detecting failed servers | Written |
| [Checksums](checksums.md) | Detecting corrupted data | Written |
| [Idempotency](idempotency.md) | Making retries safe, no duplicate effects | Written |
| [Distributed locking](distributed-locking.md) | Mutual exclusion across machines | Written |
| [Write-ahead log](write-ahead-log.md) | Durability and crash recovery | Written |
| [Circuit breaker](circuit-breaker.md) | Stopping cascading failures | Written |
| [Batch vs stream processing](batch-vs-stream-processing.md) | Computing over big data, on a schedule or in real time | Written |

## Add a new pattern

1. Copy [_template.md](_template.md) to `patterns/your-pattern.md`.
2. Fill in each section.
3. Add a row above and, if it is a core pattern, to the table in the root [README](../README.md).

For the full, in-depth treatment of every pattern with interactive diagrams, see the [course](https://www.designgurus.io/course/grokking-the-system-design-interview).