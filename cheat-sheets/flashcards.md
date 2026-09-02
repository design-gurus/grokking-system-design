# System design flashcards

Rapid-fire question and answer cards over the core patterns. Use them to find the gaps in your recall before an interview.

## How to use this deck

1. Read the question. Say your answer out loud, in full sentences.
2. Then read the answer. Speaking first is the point, because the interview is spoken.
3. Mark every card you miss. Review only those the next day.
4. Each section links to the full explanation. Go there when a card does not make sense yet.

A good target: you can answer any card in under 30 seconds without notes.

## Scale and performance

See [non-functional requirements](non-functional-requirements.md).

**Q:** What is the difference between performance and scalability?
**A:** Performance is how fast the system is for one user today. Scalability is whether it stays fast and affordable as load grows. Slow for a single user is a performance problem. Fast for one user but failing under many is a scalability problem.

**Q:** Vertical or horizontal scaling: what is the difference?
**A:** Vertical scaling means a bigger machine. It is simple, but it has a hard ceiling and stays a single point of failure. Horizontal scaling means more machines behind a load balancer. It has no hard ceiling and survives node loss, but it needs stateless services and partitioned data.

**Q:** Latency or throughput: what is the difference?
**A:** Latency is the time to serve one request. Throughput is how many requests the system serves per second. They move independently. You can add capacity to raise throughput without making any single request faster.

**Q:** Why report latency as percentiles instead of averages?
**A:** An average hides the slow tail. If one request in a hundred takes two seconds, the average still looks healthy. Report p50, p95, and p99. At scale the tail matters more, because one page may make a hundred backend calls and wait for the slowest.

**Q:** What is a bottleneck, and how do you find one?
**A:** A bottleneck is the one component that limits the whole system. Find it by following the request path and asking which resource saturates first: CPU, memory, disk, network, or a lock. Adding capacity anywhere else changes nothing.

## Availability and reliability

**Q:** How much downtime does 99.99% availability allow per year?
**A:** About 53 minutes. For comparison, 99.9% allows about 8.8 hours per year, and 99.999% allows about 5 minutes.

**Q:** How does availability combine across components?
**A:** In sequence, where both must work, the numbers multiply and the total drops below either one. In parallel, where either one is enough, the failure rates multiply and the total rises. Redundancy adds availability, and dependency chains remove it.

**Q:** Active-passive or active-active failover: what is the difference?
**A:** Active-passive keeps one node serving and one standby idle. It is simpler, but capacity sits unused and there is a short gap during failover. Active-active has both nodes serving. There is no idle capacity, but each node must handle the full load alone, and shared state gets harder.

**Q:** What is a single point of failure?
**A:** Any component whose loss takes down the system, because nothing else can do its job. Common examples are one database primary, one load balancer, or one region.

**Q:** What is graceful degradation?
**A:** Serving a reduced version of the product instead of an error when a dependency fails. An example is hiding the recommendation row when the recommendation service is down, while checkout keeps working.

## CAP and consistency

See [CAP theorem](../patterns/cap-theorem.md) and [consistency models](../patterns/consistency-models.md).

**Q:** State the CAP theorem.
**A:** During a network partition, a distributed system can guarantee consistency or availability, but not both. Partitions are not optional, so the real choice is what to do during one. A CP system refuses the request rather than serve stale data. An AP system keeps serving and reconciles later.

**Q:** What does PACELC add to CAP?
**A:** It covers the normal case, when there is no partition. Even then you trade latency against consistency, because keeping replicas in agreement costs a round trip on every write. Read it as: if Partitioned, choose A or C; Else, choose L or C.

**Q:** Weak, eventual, or strong consistency: what is the difference?
**A:** Weak means a read may never see a given write, which is fine for live video. Eventual means replicas agree once writes stop, so reads can be briefly stale, which is fine for a feed. Strong means every read sees the latest write, which is required for money and for booking a seat.

**Q:** What is read-your-writes consistency?
**A:** A guarantee that a user always sees their own updates, even if other users see them later. Without it, a user edits a profile, gets routed to a lagging replica, and sees the old value.

**Q:** What is monotonic reads consistency?
**A:** A guarantee that a user never sees data move backward in time. Without it, two reads hitting replicas with different lag can show a comment appearing and then vanishing.

## Load balancing and proxies

See [load balancing](../patterns/load-balancing.md) and [proxies](../patterns/proxies.md).

**Q:** Layer 4 or Layer 7 load balancing: what is the difference?
**A:** Layer 4 routes on IP address and port without reading the request. It is fast and works for any protocol. Layer 7 reads the request and routes on path, header, or cookie. That enables content-based routing and TLS termination, at higher cost per request.

**Q:** Reverse proxy or load balancer: what is the difference?
**A:** A load balancer spreads traffic across many identical backends. A reverse proxy is a single entry point in front of your services, and it is useful even with one backend, for TLS termination, caching, and request filtering. One piece of software often does both jobs.

**Q:** Why must application servers be stateless to scale horizontally?
**A:** Behind a load balancer, a request can land on any server. If session data lives in one server's memory, the other servers cannot serve that user. Move state to a shared store or the client, and any server can handle any request.

**Q:** Name the common load balancing algorithms.
**A:** Round robin, weighted round robin, least connections, and hashing on a key such as client IP. Least connections handles uneven request costs better. Hashing gives stickiness, at the cost of even distribution.

**Q:** What do health checks do in a load balancer?
**A:** They test each backend on an interval and remove failing ones from rotation. Without them, the load balancer keeps sending traffic to a dead server.

## Caching

See [caching](../patterns/caching.md) and [Redis vs Memcached](redis-vs-memcached.md).

**Q:** Explain the cache-aside strategy.
**A:** The application checks the cache first. On a miss it reads the database, writes that value into the cache, and returns it. It is the default choice for read-heavy workloads, because only requested data is cached.

**Q:** Write-through or write-back caching: what is the difference?
**A:** Write-through writes to the cache and the database together. Reads after a write are correct, but writes are slower. Write-back writes to the cache and flushes to the database later. Writes are fast, but data is lost if the cache dies before the flush.

**Q:** What is a cache stampede, and how do you prevent it?
**A:** When a popular key expires, many requests miss at once and hit the database together. Prevent it by letting one request refill the key while the others wait, by spreading expiry times, or by refreshing hot keys before they expire.

**Q:** Name the common cache eviction policies.
**A:** Least recently used, least frequently used, first in first out, and plain time-to-live expiry. Least recently used is the usual default, because recent access predicts near-future access well.

**Q:** Why is cache invalidation hard?
**A:** The cache holds a copy, so every write creates two versions of the truth. You choose between expiring on a timer, which serves stale data for that window, and deleting on write, which is exact but has to reach every cache that holds the key.

**Q:** Redis or Memcached: how do you choose?
**A:** Memcached is a plain in-memory cache for strings, and it is simple and fast. Redis adds data structures, persistence, replication, and pub/sub. Choose Redis when you need more than a key and a blob.

## Content delivery

See [CDN](../patterns/cdn.md).

**Q:** What does a CDN do?
**A:** It stores copies of your content in many locations worldwide and serves each user from a nearby one. That cuts the network round trip, which no amount of server speed can fix, and it removes load from your origin.

**Q:** Push or pull CDN: what is the difference?
**A:** A pull CDN fetches content from your origin on the first request and caches it. It needs no upload step and suits large catalogs. A push CDN has you upload content ahead of time. It suits small, rarely changing sets and traffic spikes you know about in advance.

**Q:** How do you update a file that a CDN has cached?
**A:** Put a version in the filename or query string, so a change produces a new URL. That avoids waiting for expiry and avoids a manual purge across every edge location.

## Databases and indexing

See [SQL vs NoSQL](sql-vs-nosql.md) and [database indexing](../patterns/database-indexing.md).

**Q:** When do you lean SQL, and when NoSQL?
**A:** Lean SQL for transactions across rows, complex joins, and queries you cannot predict in advance. Lean NoSQL for very high write volume, flexible schemas, or simple lookups by key that tolerate stale reads. Most real systems use both.

**Q:** Name the four NoSQL families and one use for each.
**A:** Key-value for sessions and caches. Document for catalogs and profiles. Wide-column for time series and feeds, where write volume is very high. Graph for social connections and recommendations, where you follow relationships.

**Q:** What does ACID stand for?
**A:** Atomicity, consistency, isolation, and durability. Together they mean a transaction either fully happens or does not, leaves the data valid, is not disturbed by concurrent transactions, and survives a crash once committed.

**Q:** What is an index, and what does it cost?
**A:** An index is a sorted structure that turns a full table scan into a direct lookup. It costs storage, and it slows every write, because each index must be updated too. Index the columns you filter and sort on, not every column.

**Q:** B-tree or LSM tree: what is the difference?
**A:** A B-tree updates data in place and gives fast reads with predictable latency, so it fits read-heavy relational workloads. An LSM tree appends writes to memory and flushes sorted files to disk, so it absorbs very high write volume, at the cost of extra work at read time and background compaction.

**Q:** What is denormalization, and what does it trade?
**A:** Storing the same data in more than one place, or precomputing a result, so a read touches one place instead of joining. It trades write complexity and storage for read speed. It matters most across shards, where joins are expensive.

**Q:** DynamoDB or MongoDB: what is the deciding question?
**A:** Can you list every query the application will ever make? If yes, DynamoDB gives key access at any scale with zero operations. If the product is still changing, MongoDB's ad hoc queries and aggregation pipeline forgive what you did not predict. See [DynamoDB vs MongoDB](dynamodb-vs-mongodb.md).

**Q:** What is an inverted index, and how does it differ from a B-tree?
**A:** It maps each term to the sorted list of documents containing it, so a text query intersects a few of those lists instead of scanning documents. A B-tree finds an exact value in one column and has no notion of relevance, which is why search engines use a different structure.

## Replication and quorum

See [replication](../patterns/replication.md) and [quorum](../patterns/quorum.md).

**Q:** Leader-follower or multi-leader replication: what is the difference?
**A:** Leader-follower sends all writes to one node and copies them to followers that serve reads. It scales reads and keeps write ordering simple, but the leader is a bottleneck. Multi-leader accepts writes on several nodes. It scales writes and survives a leader loss, but you must resolve conflicting writes.

**Q:** What is replication lag, and why does it matter?
**A:** It is the delay before a write reaches the read replicas. During that window replicas return old data. A user can save a change and then not see it, which is why some reads must go to the leader.

**Q:** Explain quorum and the R plus W greater than N rule.
**A:** A quorum is the number of nodes that must acknowledge an operation. With N replicas, a read quorum R and a write quorum W, setting R plus W greater than N forces the read set and the write set to share at least one node. That shared node holds the newest value.

**Q:** Synchronous or asynchronous replication: what is the difference?
**A:** Synchronous replication waits for the follower to acknowledge before confirming the write. Nothing is lost on failover, but every write pays the extra round trip. Asynchronous replication confirms immediately and copies after, so writes are fast but recent ones can be lost.

**Q:** What is split brain?
**A:** Two nodes both believe they are the leader, usually after a network partition, and both accept writes. The data then diverges. Quorum rules and fencing prevent it, by making sure only one side can win.

**Q:** Two servers each accepted a write. Why can you not use timestamps to decide which is newer?
**A:** Their clocks drift, and clock sync still leaves milliseconds of skew. Last-writer-wins by timestamp silently drops the write whose server was running behind. You need a [logical clock](../patterns/logical-clocks.md) instead.

**Q:** Lamport clock or vector clock: what is the difference?
**A:** A Lamport clock is one counter per node. It guarantees that if A caused B then A's value is lower, but it cannot tell you two events were concurrent. A vector clock keeps one counter per node, so comparing two vectors detects true concurrency, which is what lets a system keep both versions and merge them.

## Sharding and partitioning

See [sharding and partitioning](../patterns/sharding-partitioning.md) and [consistent hashing](../patterns/consistent-hashing.md).

**Q:** What problem does consistent hashing solve?
**A:** With plain modulo hashing, adding or removing one node changes the target of almost every key, so the cache empties and the database is overwhelmed. Consistent hashing places nodes and keys on a ring, so only the keys next to the changed node move.

**Q:** What are virtual nodes, and why use them?
**A:** Each physical machine is placed at many points on the ring instead of one. That evens out the key distribution and spreads a failed node's load across all the survivors instead of one neighbor.

**Q:** What is a hot spot, and how do you avoid one?
**A:** One shard receives far more traffic than the others, usually from a poor shard key, such as partitioning by a celebrity account. Avoid it with a key that has many distinct values and even traffic, and split hot keys by adding a suffix.

**Q:** Name the common sharding strategies.
**A:** Range based, which keeps ordered scans cheap but creates hot spots. Hash based, which spreads evenly but loses range scans. Directory based, which keeps a lookup table for full control, at the cost of an extra hop and another thing to keep available.

**Q:** Why are cross-shard queries expensive?
**A:** The query must reach every shard, wait for the slowest, and combine the results in the application. Joins and transactions that span shards are worse, because they also need coordination to stay correct.

## Messaging and asynchronous work

See [message queues](../patterns/message-queues.md) and [Kafka vs RabbitMQ vs SQS](kafka-vs-rabbitmq-vs-sqs.md).

**Q:** Why put work on a message queue?
**A:** Four reasons: the producer and consumer no longer call each other directly, the queue absorbs traffic spikes, failed work can be retried, and each side scales on its own.

**Q:** What is back pressure?
**A:** The system pushing back when producers outpace consumers, so the backlog cannot grow without limit. In practice: cap the queue, reject or slow new work, and add consumers based on queue depth. Watch queue depth and consumer lag.

**Q:** Why must queue consumers be idempotent?
**A:** Most queues deliver at least once, so the same message can arrive twice after a retry. Idempotent means handling it twice has the same effect as handling it once, which is what prevents a double charge.

**Q:** At-most-once, at-least-once, or exactly-once delivery?
**A:** At-most-once may lose messages and never repeats them. At-least-once never loses messages but may repeat them, and it is the common default. Exactly-once is really at-least-once plus deduplication, so it costs extra coordination.

**Q:** A log or a broker: how do Kafka and RabbitMQ differ?
**A:** Kafka is a durable, ordered log. Consumers track their own position and can replay history, which suits streaming and event sourcing. RabbitMQ is a broker that routes a message to a consumer and drops it once acknowledged, which suits task queues and complex routing.

**Q:** What is a dead letter queue?
**A:** A separate queue for messages that keep failing after a set number of retries. It stops one bad message from blocking the consumer forever, and it keeps the message for inspection.

**Q:** Batch or stream processing: how do you choose?
**A:** Batch processes large, bounded sets on a schedule, and it is simpler and cheaper per record. Streaming processes records as they arrive, with results in seconds. Choose by how fresh the answer must be, because freshness is what you pay for.

**Q:** Kafka, Kinesis, or Pub/Sub: what separates them?
**A:** They are all durable streams, so the deciding factors are cloud and capacity model. Kafka runs anywhere and gives you the full ecosystem, at operational cost. Kinesis is AWS with shards you size. Pub/Sub is GCP with no partitions to manage. See [Kafka vs Kinesis vs Pub/Sub](kafka-vs-kinesis-vs-pubsub.md).

**Q:** Every buffer needs what two things?
**A:** A bound, and a policy for when it fills. The policies are block the producer, shed load (reject with 429 or 503 plus Retry-After), or drop data. An unbounded queue does not remove overload, it hides overload until it is fatal. See [backpressure](../patterns/backpressure.md).

**Q:** Why autoscale consumers on queue depth rather than CPU?
**A:** A consumer blocked waiting on a slow downstream dependency looks idle on CPU while the backlog keeps growing. Queue depth and consumer lag are the signals that actually track falling behind.

## Distributed transactions and event-driven state

See [distributed transactions](../patterns/distributed-transactions.md), [event sourcing and CQRS](../patterns/event-sourcing-cqrs.md), and the [outbox pattern](../patterns/outbox-pattern.md).

**Q:** How does two-phase commit work, and why is it rare between services?
**A:** A coordinator asks every participant to prepare, and commits only when all vote yes. It is atomic, but it blocks: participants hold locks while waiting, and a dead coordinator freezes all of them. One slow service would stall everyone, so it lives inside databases rather than between microservices.

**Q:** What is a saga?
**A:** One logical operation split into a chain of local transactions, each committing immediately. A later failure is undone by a compensating action, such as refunding a charge. The price is that half-finished states are visible between steps.

**Q:** Choreography or orchestration for a saga?
**A:** In choreography each service reacts to the previous service's event, so there is no coordinator but the flow is written down nowhere. In orchestration one service drives the steps and handles failures, giving you one place to read the flow. Past about three steps, choose orchestration.

**Q:** What is the dual-write problem?
**A:** A service must update its database and publish an event, and no transaction covers both. A crash in between leaves either a state change nobody hears about or an event for a change that rolled back.

**Q:** How does the outbox pattern fix it?
**A:** The event is inserted into an outbox table in the same local transaction as the state change, so the two commit together or not at all. A relay then reads unsent rows and publishes them. Delivery is at-least-once, so consumers must be idempotent.

**Q:** What is event sourcing, and what does CQRS add?
**A:** Event sourcing stores the facts (deposited 100, withdrew 30) in an append-only log instead of current state, and derives state by replaying them. CQRS separates the write path from purpose-built read models, each shaped for one query and updated by projectors reading the log.

**Q:** When is event sourcing the wrong choice?
**A:** Plain CRUD with a single view. You would pay for read-after-write lag, event schemas you must support forever, and slow rebuilds without snapshots, and get nothing back. Reach for it when audit or time-travel queries are real requirements.

## APIs and communication

See [REST vs gRPC vs GraphQL](rest-vs-grpc-vs-graphql.md) and [API gateway](../patterns/api-gateway.md).

**Q:** TCP or UDP: when do you use each?
**A:** TCP is reliable and ordered, so use it when losing data is unacceptable, as with web requests and databases. UDP is best effort with less overhead, so use it when late data is worthless anyway, as with live voice, video, and gaming.

**Q:** Which HTTP methods are idempotent, and why does it matter?
**A:** GET, PUT, and DELETE are idempotent. POST and PATCH are not. Idempotent requests are safe to retry after a timeout. That is why a retried POST can charge a card twice, and why payments need an idempotency key.

**Q:** REST or RPC: what is the difference?
**A:** REST models resources with standard verbs, so it is uniform, cacheable, and a good default across teams and for public APIs. RPC models actions as function calls, which is a tighter fit and faster for internal service to service traffic.

**Q:** When would you choose gRPC or GraphQL over REST?
**A:** Choose gRPC for internal, high-volume service calls, where its binary format, streaming, and generated clients pay off. Choose GraphQL when many different clients need different fields from one round trip. Keep REST for public, cacheable, simple APIs.

**Q:** What does an API gateway do?
**A:** It is the single entry point in front of many services. It handles authentication, rate limiting, routing, and request shaping in one place, so each service does not repeat that work. It is also a bottleneck and a failure point, so it must be redundant.

**Q:** Offset or cursor pagination: which is better and why?
**A:** Cursor pagination is better at scale. Offset pagination skips rows, so deep pages get slower, and rows shift when data changes between requests. A cursor points at the last item seen, so it stays fast and stable.

## Real-time delivery

See [long polling, WebSockets, and SSE](../patterns/long-polling-websockets-sse.md).

**Q:** Polling, long polling, SSE, or WebSockets: what is the difference?
**A:** Polling asks on a timer and wastes most requests. Long polling holds the request open until there is news, then reconnects. Server-sent events keep one open connection for server-to-client updates. WebSockets keep one open connection in both directions.

**Q:** How do you choose between them?
**A:** Choose by direction and frequency. Use polling when a delay of a minute is fine. Use server-sent events for a live feed that only flows down, such as a price ticker. Use WebSockets when both sides send often, such as chat or collaborative editing.

## Rate limiting and resilience

See [rate limiting](../patterns/rate-limiting.md) and [circuit breaker](../patterns/circuit-breaker.md).

**Q:** How does a token bucket rate limiter work?
**A:** Tokens are added at a fixed rate up to a maximum. Each request removes one token, and a request with no token available is rejected or delayed. The bucket size sets how large a burst you allow, and the refill rate sets the sustained limit.

**Q:** Leaky bucket or sliding window: how do they differ from token bucket?
**A:** A leaky bucket drains at a constant rate, so it smooths output and allows no bursts. A sliding window counts requests in the recent period, so it enforces a limit accurately without the edge spike that a fixed window allows.

**Q:** What does a circuit breaker do?
**A:** It stops calling a failing dependency once errors pass a threshold. It then fails fast for a cooldown, and after that lets a few test requests through. If they succeed it resumes. This stops one slow service from consuming every thread upstream.

**Q:** How should retries be implemented?
**A:** With a limit, exponential backoff, and random jitter, and only for errors that may succeed later. Without backoff, retries add load to a service that is already struggling. Without jitter, all clients retry at the same instant.

**Q:** What are timeouts and bulkheads?
**A:** A timeout caps how long you wait for a dependency, so a slow call cannot hold a thread forever. A bulkhead gives each dependency its own limited pool of connections or threads, so one failing dependency cannot starve the rest.

## Coordination

See [leader election](../patterns/leader-election.md), [distributed locking](../patterns/distributed-locking.md), and [heartbeats](../patterns/heartbeats.md).

**Q:** What is leader election, and when do you need it?
**A:** It is how a cluster agrees on one node to do a job that only one node may do, such as accepting writes or running a scheduled task. It usually runs through a consensus service, and it needs a majority so two leaders cannot both win.

**Q:** What is a fencing token, and why does a distributed lock need one?
**A:** A number that increases every time the lock is granted. The holder sends it with each write, and the storage layer rejects anything older. It is what protects you when a lock holder pauses, its lease expires, and it wakes up still believing it holds the lock.

**Q:** What do heartbeats do?
**A:** Each node sends a small periodic message to say it is alive. Missing several in a row marks the node as failed, which triggers failover or rebalancing. The interval trades detection speed against false alarms from a brief network delay.

**Q:** How do a thousand nodes learn who is in the cluster?
**A:** A [gossip protocol](../patterns/gossip-protocol.md). Each node periodically exchanges its membership table with a few random peers and keeps the newest entry per node. Information reaches everyone in about log N rounds, and each node's cost stays constant as the cluster grows.

**Q:** Why not just heartbeat every node to a coordinator?
**A:** The coordinator is a single point of failure and a hot spot, and all-to-all heartbeats cost N-squared messages per round. Gossip is the decentralized middle, at the price of eventual convergence and occasional false suspicion.

## Durability and data integrity

See [write-ahead log](../patterns/write-ahead-log.md), [checksums](../patterns/checksums.md), and [bloom filters](../patterns/bloom-filters.md).

**Q:** What is a write-ahead log?
**A:** An append-only file where every change is recorded and flushed to disk before the change is applied. After a crash, the system replays the log to recover. Appending sequentially is far faster than updating data in place.

**Q:** What do checksums protect against?
**A:** Silent corruption of data in storage or in transit. A small value is computed from the data and stored with it. If a later recomputation does not match, the copy is bad and can be repaired from a replica.

**Q:** What is a bloom filter, and what is its trade-off?
**A:** A small structure that answers set membership. It can say "possibly present" for something absent, but it never says "not present" for something that is there. That one-sided error lets it use very little memory, and it saves expensive lookups for keys that are not there.

## Landmark systems

See the [deep dives](../deep-dives/) for the full case studies.

**Q:** What idea makes Borg and Kubernetes work?
**A:** Declarative desired state plus a reconciliation loop. You describe what should be running, and controllers continuously compare that to reality and correct the difference. Treating the datacenter as one scheduled pool, instead of machines owned by teams, is what reclaims the wasted capacity.

**Q:** Why is Redis fast, and what is the cost of that design?
**A:** Everything is in memory and one command runs at a time, so every operation is atomic with no locks. The cost is a hard per-node ceiling: one slow command blocks every client, which is why commands that walk a whole keyspace are dangerous in production.

**Q:** Why is deep pagination expensive in a distributed search index?
**A:** A query is scatter-gather across shards, and each shard must return enough hits for the coordinator to merge correctly. Asking for page 100 forces every shard to return 100 pages worth, so cost grows with the page number.

**Q:** What is a watermark in stream processing?
**A:** A moving assertion that no event older than time T will still arrive. It is what allows a time window to close and emit a result, given that events arrive late and out of order. Events arriving after it follow a stated policy: drop, or update the emitted result.

**Q:** Does a stream processor's exactly-once guarantee make your pipeline exactly-once?
**A:** No. Checkpoints restore the processor's own state exactly, but a replay re-emits output, so the sink must be transactional or idempotent. Exactly-once is a property of the whole pipeline, not a checkbox on one component.

**Q:** How does HNSW search billions of vectors quickly?
**A:** It links each vector to its near neighbors in a graph and walks greedily toward the query, with sparse upper layers for long jumps and dense lower layers for fine search. It is approximate: you trade recall against latency, and that dial is a product decision.

**Q:** What is the hard part of vector search in practice?
**A:** Filtering. Applying a metadata filter after the graph walk can return too few results, and applying it during the walk can disconnect the graph. Pre-filtering versus post-filtering is a real design decision, and permission-filtered retrieval is where it bites.

## Design problem shapes

Recurring shapes from the [question catalog](../questions/).

**Q:** Identified or counted inventory: why does it change the design?
**A:** Ticket seats are identified: you hold seat 12F, so each seat is its own row with a status. Hotel rooms are counted: you book one king room per night, so inventory is a count per room type per date and a stay updates several date rows in one transaction.

**Q:** How do you hold an item during checkout without a distributed lock?
**A:** A conditional update inside one transaction: set the status to held only where it is still free. If the row count comes back short, someone else won. The database's own atomicity settles the race, and a TTL on the hold releases abandoned checkouts.

**Q:** Why can a stale availability display never cause a double-sell?
**A:** Because the purchase transaction is the source of truth and re-checks at commit time. A stale cached map costs one user a "just taken" message, which is a far cheaper problem than serializing every viewer through the booking database.

**Q:** What does a spatial index do that a normal index cannot?
**A:** It makes points that are close in space close in the index, using geohash cells or a quadtree. A B-tree sorts on one dimension, so it narrows latitude and then scans that whole band around the world to check longitude.

**Q:** Why does video conferencing use UDP for media but a reliable channel for signaling?
**A:** A retransmitted video frame arrives after the moment it described, so fresh-but-lossy beats late-but-reliable. Signaling (join, mute, roster) is small and must be correct, so it stays on a reliable channel.

**Q:** What is an SFU, and why not a mesh?
**A:** A selective forwarding unit takes one uploaded stream per client and forwards selected streams down to others. A mesh has every client send to every other, so upload bandwidth runs out at around four participants.

**Q:** Why does a code assistant cache prompt prefixes?
**A:** Consecutive completion requests share almost the whole prompt (the file so far) and differ by a few characters. Caching the model's computed state for the shared prefix means each keystroke request pays only for the new tokens, which is what makes the product affordable.

**Q:** Why must an LLM gateway meter tokens rather than requests?
**A:** One request can cost a hundred tokens or a hundred thousand. Since true usage is known only after the response, quotas estimate from the prompt, reserve against the budget, then settle with actuals.

## Numbers worth memorizing

See [estimation](estimation.md) for the full tables and a worked example.

**Q:** Roughly how long is a memory read, an SSD read, and a cross-continent round trip?
**A:** A main memory reference is about 100 nanoseconds. An SSD random read is about 100 microseconds, so about a thousand times slower. A round trip between continents is about 150 milliseconds, which is over a million times slower than memory.

**Q:** What is a round trip inside one data center?
**A:** About 500 microseconds, or half a millisecond. This is why a design that makes many sequential internal calls is slow, even though every service looks fast on its own.

**Q:** How do you convert requests per day to requests per second?
**A:** A day is about 86,400 seconds, so round it to 100,000. Divide the daily number by 100,000. One hundred million requests per day is roughly 1,000 per second.

**Q:** What do the powers of two give you?
**A:** Two to the tenth is about a thousand, which is a kilobyte. Two to the twentieth is a million, a megabyte. Two to the thirtieth is a billion, a gigabyte. Two to the fortieth is a trillion, a terabyte.

## The interview itself

See [interview framework](interview-framework.md), [common mistakes](common-mistakes.md), and [senior vs staff expectations](senior-vs-staff-expectations.md).

**Q:** What are the steps of the interview framework?
**A:** Clarify requirements and scope. Estimate the scale. Define the API. Design the data model. Sketch the high-level architecture. Deep dive on one or two components. Finish with bottlenecks and trade-offs.

**Q:** What is the most common reason a candidate fails?
**A:** Process, not knowledge. Designing before clarifying, skipping estimation, working in silence, and never naming a trade-off. The knowledge is usually there and does not get shown.

**Q:** What separates a staff answer from a senior answer to the same question?
**A:** A senior candidate produces a correct design with sound trade-offs. A staff candidate also questions the requirements, names what the design will cost, plans the migration and failure path, and says what they would measure to know it works.

**Q:** How should you handle a part of the design you do not know?
**A:** Say so directly, then reason from what you do know. State your assumption, name the option you would choose, and say what you would verify. Interviewers score reasoning, and a confident guess presented as fact is worse than an honest gap.

## Go deeper

- Full explanations: [patterns](../patterns/) and the other [cheat sheets](./)
- Practice questions: [question catalog](../questions/) and the [practice bank](../questions/practice-bank.md)
- The real systems behind the cards: [deep dives](../deep-dives/)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=cheat-sheets-flashcards)
