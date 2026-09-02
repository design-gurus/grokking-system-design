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
| [Distributed transactions (2PC vs sagas)](distributed-transactions.md) | One operation across many services, correctly | Written |
| [Event sourcing and CQRS](event-sourcing-cqrs.md) | State as an event log, plus purpose-built read views | Written |
| [Outbox pattern](outbox-pattern.md) | Publishing events reliably alongside database writes | Written |
| [Backpressure](backpressure.md) | Pushing back on producers instead of buffering without limit | Written |
| [Gossip protocol](gossip-protocol.md) | Cluster membership and health without a coordinator | Written |
| [Logical clocks (Lamport and vector)](logical-clocks.md) | Ordering events when wall clocks cannot be trusted | Written |

## Add a new pattern

1. Copy [_template.md](_template.md) to `patterns/your-pattern.md`.
2. Fill in each section.
3. Add a row above and, if it is a core pattern, to the table in the root [README](../README.md).

For the full, in-depth treatment of every pattern with interactive diagrams, see [System Design Patterns: From Fundamentals to Real Systems](https://www.designgurus.io/course/system-design-patterns?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=patterns-readme), the course built around exactly these building blocks.