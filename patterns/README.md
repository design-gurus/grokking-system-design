# Patterns: the building blocks of system design

> The 30 reusable pieces that system designs are assembled from. Learn these once and they apply to every question you are asked.

Interview questions look different from each other on the surface. The pieces you build them from do not. A URL shortener, a news feed, and a ride-hailing service all need the same small set of building blocks, arranged differently.

Each page here is short and practical: what the pattern is, when to use it, the trade-offs, and how to talk about it in an interview.

## Start here

If you learn only five, learn these. They appear in almost every design.

1. [Caching](caching.md), the most-read page in this directory and the first answer to most latency problems.
2. [Load balancing](load-balancing.md), how traffic reaches more than one machine.
3. [Sharding and partitioning](sharding-partitioning.md), how data grows past one machine.
4. [Replication](replication.md), how the system survives a machine dying.
5. [Consistency models](consistency-models.md), the vocabulary for what a read is allowed to return.

## Find the pattern by the problem

| What you are trying to do | Start with |
|---------------------------|-----------|
| Make reads faster | [Caching](caching.md), [CDN](cdn.md), [database indexing](database-indexing.md) |
| Handle more traffic than one machine can | [Load balancing](load-balancing.md), [sharding](sharding-partitioning.md), [replication](replication.md) |
| Decide what a read is allowed to return | [Consistency models](consistency-models.md), [CAP theorem](cap-theorem.md), [quorum](quorum.md) |
| Connect services without coupling them | [Message queues](message-queues.md), [outbox](outbox-pattern.md), [event sourcing and CQRS](event-sourcing-cqrs.md) |
| Survive a machine or a dependency failing | [Heartbeats](heartbeats.md), [circuit breaker](circuit-breaker.md), [leader election](leader-election.md) |
| Make a retry safe | [Idempotency](idempotency.md), [write-ahead log](write-ahead-log.md) |
| Protect a service from overload | [Rate limiting](rate-limiting.md), [backpressure](backpressure.md) |
| Push updates to a client in real time | [Long polling, WebSockets, and SSE](long-polling-websockets-sse.md) |
| Change data in two places at once | [Distributed transactions](distributed-transactions.md), [distributed locking](distributed-locking.md) |

## Serving reads fast

| Pattern | What it solves |
|---------|----------------|
| [Caching](caching.md) | Read latency and load on the data store |
| [CDN](cdn.md) | Serving static content close to users |
| [Database indexing](database-indexing.md) | Fast lookups |
| [Bloom filters](bloom-filters.md) | Cheap "definitely not present" checks |
| [Proxies](proxies.md) | Intermediaries for routing, security, and caching |

## Spreading load across machines

| Pattern | What it solves |
|---------|----------------|
| [Load balancing](load-balancing.md) | Distributing traffic across servers |
| [Sharding and partitioning](sharding-partitioning.md) | Scaling data beyond one machine |
| [Consistent hashing](consistent-hashing.md) | Even distribution with minimal reshuffling |
| [Replication](replication.md) | Availability and read scaling |
| [API gateway](api-gateway.md) | One entry point for auth, rate limiting, and routing |

## Agreeing on state

| Pattern | What it solves |
|---------|----------------|
| [Consistency models](consistency-models.md) | Correctness under concurrency |
| [CAP theorem](cap-theorem.md) | Reasoning about trade-offs under partitions |
| [Quorum](quorum.md) | Consistent reads and writes across replicas |
| [Leader election](leader-election.md) | Agreeing on one node in charge, surviving failover |
| [Logical clocks (Lamport and vector)](logical-clocks.md) | Ordering events when wall clocks cannot be trusted |
| [Distributed locking](distributed-locking.md) | Mutual exclusion across machines |
| [Gossip protocol](gossip-protocol.md) | Cluster membership and health without a coordinator |

## Moving work around

| Pattern | What it solves |
|---------|----------------|
| [Message queues](message-queues.md) | Decoupling and async processing |
| [Batch vs stream processing](batch-vs-stream-processing.md) | Computing over big data, on a schedule or in real time |
| [Backpressure](backpressure.md) | Pushing back on producers instead of buffering without limit |
| [Long polling vs WebSockets vs SSE](long-polling-websockets-sse.md) | Pushing real-time updates to clients |

## Staying correct when things fail

| Pattern | What it solves |
|---------|----------------|
| [Idempotency](idempotency.md) | Making retries safe, no duplicate effects |
| [Write-ahead log](write-ahead-log.md) | Durability and crash recovery |
| [Checksums](checksums.md) | Detecting corrupted data |
| [Heartbeats](heartbeats.md) | Detecting failed servers |
| [Circuit breaker](circuit-breaker.md) | Stopping cascading failures |
| [Rate limiting](rate-limiting.md) | Protecting services from overload |
| [Distributed transactions (2PC vs sagas)](distributed-transactions.md) | One operation across many services, correctly |
| [Event sourcing and CQRS](event-sourcing-cqrs.md) | State as an event log, plus purpose-built read views |
| [Outbox pattern](outbox-pattern.md) | Publishing events reliably alongside database writes |

## How these fit with the rest of the repo

A pattern page explains the mechanism. A [cheat sheet](../cheat-sheets/) is the decision: when a pattern has several common options, the sheet tells you which to pick and why. [Caching](caching.md) explains how a cache works, and [caching strategies](../cheat-sheets/caching-strategies.md) picks between cache-aside, write-through, and the rest.

The [questions](../questions/) apply the patterns end to end, and the [deep dives](../deep-dives/) show real systems that made these same choices.

## Add a new pattern

1. Copy [_template.md](_template.md) to `patterns/your-pattern.md`.
2. Fill in each section, including the one-line summary directly under the title.
3. Add a row to the right table above and, if it is a core pattern, to the table in the root [README](../README.md).

## Go deeper

- Every pattern in depth, with interactive diagrams: [System Design Patterns: From Fundamentals to Real Systems](https://www.designgurus.io/course/system-design-patterns?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=patterns-readme)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=patterns-readme)
