# Flashcards: rapid-fire review

> Spaced-repetition-style Q&A over the [fundamentals](../fundamentals/) and [patterns](../patterns/). Cover the answer, quiz yourself, repeat the ones you miss. The [local study assistant](../tools/study-assistant/) can quiz you from this deck (`quiz <topic>`) and grade your answers.

**Format:** each card is a `**Q:**` / `**A:**` pair under a topic heading. Topic headings match the argument to the assistant's `quiz` command (e.g. `quiz caching`).

## Fundamentals

**Q:** What's the difference between performance and scalability?
**A:** Performance is how fast the system is for one user right now; scalability is whether it stays fast and affordable as load grows. Slow with one user = performance problem; fast for one but falls over under many = scalability problem.

**Q:** Vertical vs horizontal scaling?
**A:** Vertical (scale up) = a bigger machine: simple but has a ceiling, costs more, and is a single point of failure. Horizontal (scale out) = more machines behind a load balancer: no hard ceiling and fault tolerant, but requires stateless services and data partitioning.

**Q:** Latency vs throughput?
**A:** Latency is the time to serve one request; throughput is how many requests per unit time. Highway analogy: latency is trip time, throughput is cars per hour. You can raise throughput (more lanes) without lowering latency.

**Q:** Why report latency as percentiles instead of averages?
**A:** Averages hide the tail. If one request in a hundred takes 2s, the average looks fine but that slow tail is what users feel — especially at scale, where a page making 100 backend calls hits a p99-slow call on most loads. Report p50, p95, p99, p99.9.

**Q:** State the CAP theorem.
**A:** During a network partition, a distributed system can guarantee consistency or availability, not both. Since partitions are unavoidable, the real choice is CP (refuse/block rather than serve stale) vs AP (keep serving, reconcile later).

**Q:** What does PACELC add to CAP?
**A:** Even with no partition (Else), there's still a trade-off between Latency and Consistency: keeping replicas strongly consistent costs coordination latency on every write. PACELC = "if Partition then A or C, Else L or C."

**Q:** Weak vs eventual vs strong consistency?
**A:** Weak = reads may never see a write, no guarantee (live video). Eventual = replicas converge if writes stop; reads may be briefly stale (feeds, DNS). Strong = every read sees the latest write, requiring coordination (money, bookings).

**Q:** What does 99.99% availability allow in downtime per year?
**A:** About 52.6 minutes per year (four nines). 99.9% (three nines) ≈ 8.77 hours/year; 99.999% (five nines) ≈ 5.26 minutes/year.

**Q:** How does availability combine for components in sequence vs in parallel?
**A:** In sequence (both must work), availabilities multiply, so total is lower than either (99.9% × 99.9% ≈ 99.8%). In parallel (either works), the failure gaps multiply, so total is higher (redundancy buys nines).

**Q:** Active-passive vs active-active failover?
**A:** Active-passive: one node serves, a hot standby takes over on failure (simple, but idle standby and a brief gap). Active-active: both serve traffic and absorb each other's load on failure (no idle capacity, but shared state and each must handle full load).

## DNS

**Q:** What does DNS do and why does its latency matter?
**A:** It resolves a human name (www.example.com) to an IP address. It runs at the start of essentially every request, so an uncached lookup adds a round trip before the real request begins — hence caching by TTL.

**Q:** How can DNS be used for traffic management?
**A:** Round-robin (spread across IPs), geo/latency-based routing (nearest region), health-checked failover (stop returning a dead endpoint, bounded by TTL), and weighted routing for canaries.

## Load balancing

**Q:** Layer 4 vs Layer 7 load balancing?
**A:** Layer 4 routes on IP/port without reading the request — fast, any protocol. Layer 7 terminates the connection and routes on URL/headers/cookies — enables content-based routing, sticky sessions, and TLS termination.

**Q:** Reverse proxy vs load balancer?
**A:** A load balancer spreads traffic across many identical backends. A reverse proxy is a smart front door for your services (TLS termination, caching, security, routing) even with one backend. One piece of software often does both.

**Q:** Why must app servers be stateless to scale horizontally?
**A:** With multiple servers behind a load balancer, a request can land on any server. If session state lives in one server's memory, other servers can't serve that user. Pushing state to a shared store or the client lets any server handle any request.

## Caching

**Q:** Explain cache-aside.
**A:** The app checks the cache first; on a miss it reads the database and populates the cache, then returns. Simple and the default for read-heavy workloads.

**Q:** Write-through vs write-back caching?
**A:** Write-through writes to cache and DB together (read-after-write consistency, slower writes). Write-back writes to cache and flushes to the DB later (fast writes, risk of loss if the cache dies before flush).

**Q:** What is the thundering herd / cache stampede and how do you prevent it?
**A:** When a hot key expires, many requests miss and hit the DB at once. Mitigations: request coalescing (one loader, others wait), staggered TTLs, and locks.

## Consistency and replication

**Q:** Leader-follower vs multi-leader replication?
**A:** Leader-follower: one node takes writes, followers serve reads (scales reads; leader is a bottleneck/SPOF). Multi-leader: multiple nodes accept writes and sync (scales writes, survives node loss, but must resolve write conflicts).

**Q:** What is a quorum and the R + W > N rule?
**A:** A quorum is the minimum nodes that must acknowledge a read/write. With N replicas, if read quorum R + write quorum W > N, reads and writes overlap on at least one node, guaranteeing you read the latest write.

**Q:** What is replication lag and why does it matter?
**A:** The delay before a write reaches read replicas. During the lag, replicas serve stale data (eventual consistency for reads) — so a user might not see their own just-made write unless you read from the primary.

## Sharding

**Q:** What problem does consistent hashing solve?
**A:** With plain modulo hashing, adding/removing a node remaps almost all keys. Consistent hashing maps nodes and keys onto a ring so only keys near the changed node move — minimizing reshuffling. Virtual nodes even out the distribution.

**Q:** What is a hot spot in sharding and how do you avoid it?
**A:** When one shard gets disproportionate traffic because of a bad shard key (e.g. sharding by a celebrity's user ID). Avoid it by choosing a high-cardinality, evenly-distributed key, or by hashing/salting hot keys.

## Databases

**Q:** Name the four NoSQL families and a use for each.
**A:** Key-value (caches, sessions), document (catalogs, profiles), wide-column (time series, feeds — huge write throughput), graph (social graphs, recommendations — relationship traversal).

**Q:** When lean SQL vs NoSQL?
**A:** SQL for strong transactions, complex joins/ad-hoc queries, naturally relational data. NoSQL for massive scale/write throughput, flexible schema, or simple key-based access that tolerates eventual consistency. Real systems use both (polyglot persistence).

**Q:** What is denormalization and its trade-off?
**A:** Deliberately duplicating/precomputing data so reads hit one place instead of joining. Trades write complexity and storage for read speed — used on read-heavy paths, especially across shards where joins are expensive.

## Asynchronism and messaging

**Q:** Why put work on a message queue?
**A:** Decoupling (services don't call each other directly), spike absorption (the queue buffers bursts), retries (failed jobs go back on the queue), and independent scaling of producers and consumers.

**Q:** What is back pressure?
**A:** The system pushing back when producers outpace consumers so the queue doesn't grow unbounded: bound the queue and shed load (429/503), rate-limit producers, autoscale consumers on queue depth. Monitor queue depth and consumer lag.

**Q:** Why must queue consumers be idempotent?
**A:** Most queues deliver at-least-once, so a message can arrive more than once (retries, redelivery). Idempotent consumers make processing the same message twice have the same effect as once — no double charges.

## Communication

**Q:** TCP vs UDP — when to use each?
**A:** TCP is reliable, ordered, connection-oriented — use when you can't lose data (web, APIs, DBs). UDP is best-effort and low-overhead — use when fresh-but-lossy beats reliable-but-late (live video/voice, gaming, DNS).

**Q:** Which HTTP methods are idempotent, and why does it matter?
**A:** GET, PUT, and DELETE are idempotent; POST and PATCH are not. Idempotent requests are safe to retry — which is why retried POSTs cause double-charges and need an idempotency key.

**Q:** RPC vs REST?
**A:** RPC models actions (createUser, charge) — tighter coupling, great for internal high-performance service calls (gRPC). REST models resources (/users, /orders/42) with standard verbs — uniform, cacheable, evolves well, the default for public/cross-team APIs.

## Rate limiting and resilience

**Q:** How does a token bucket rate limiter work?
**A:** Tokens refill at a fixed rate up to a bucket capacity; each request consumes a token, and requests with no token are rejected or delayed. Allows short bursts (up to bucket size) while capping the sustained rate.

**Q:** What does a circuit breaker do?
**A:** It stops calling a failing dependency after errors cross a threshold (open state), fails fast for a cooldown, then tries a few requests (half-open) before closing again — preventing cascading failures and giving the dependency time to recover.

## Go deeper

- Turn these into an interactive quiz with the [local study assistant](../tools/study-assistant/): `quiz caching`.
- Read the full explanations in [fundamentals](../fundamentals/) and [patterns](../patterns/).
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)
