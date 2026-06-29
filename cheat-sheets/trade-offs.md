# Trade-off decision guides

> Interviews reward reasoning about trade-offs, not memorized answers. Here are the common "X vs Y" decisions and how to choose, each with a one-line answer you can say out loud.

## Strong vs eventual consistency

- **Strong:** every read sees the latest write. Use for money, inventory, and anything where a wrong answer is worse than a slow one.
- **Eventual:** replicas converge over time; a read may be briefly stale. Use for feeds, counts, and profiles.
- **Pick the weakest the product tolerates**, since weaker is faster and more available. See [consistency models](../patterns/consistency-models.md).
- *Interview line:* "This is a like count, so I favor eventual consistency for throughput."

## Synchronous vs asynchronous

- **Sync:** the caller waits for the result. Simpler, but couples the response time to the slowest step.
- **Async (via a [queue](../patterns/message-queues.md)):** the caller returns immediately and the work happens later. Use for slow or spiky work (email, encoding, notifications).
- **Rule:** keep the request path synchronous only for what the user needs right now; push everything else async.
- *Interview line:* "Sending the confirmation email is async, so checkout does not wait on the mail provider."

## Push vs pull (fan-out)

- **Push (fan-out on write):** precompute and deliver into each recipient's view. Fast reads, but expensive for huge audiences (the celebrity problem).
- **Pull (fan-out on read):** assemble the view on demand. Cheap writes, slower reads.
- **Hybrid:** push for normal users, pull for the few with massive followings. This is the realistic answer for feeds and timelines.
- *Interview line:* "I push to most followers but pull for celebrities to avoid a write storm."

## Monolith vs microservices

- **Monolith:** one deployable unit. Simpler to build, test, and operate. The right default early on.
- **Microservices:** independent services that scale and deploy separately, at the cost of real operational complexity (networking, observability, data consistency).
- **Start with a monolith** and split out services when team size and scale justify it.
- *Interview line:* "I would start monolithic and extract services only where scaling or team boundaries demand it."

## Synchronous vs asynchronous replication

- **Sync replication:** a write waits for a replica to confirm. No data loss on failover, but higher write latency.
- **Async replication:** the write returns immediately and replicates in the background. Fast, but a crash can lose the last few writes. See [replication](../patterns/replication.md).
- *Interview line:* "Payments use synchronous replication; the activity feed uses async."

## Normalization vs denormalization

- **Normalized:** little duplication, but reads need joins.
- **Denormalized:** data is duplicated for fast reads, at the cost of more complex writes. Common in NoSQL and read-heavy systems.
- *Interview line:* "I denormalize the timeline for fast reads and accept the extra write work."

## SQL vs NoSQL

See the dedicated guide: [SQL vs NoSQL](sql-vs-nosql.md). Short version: choose by access pattern, not habit, and justify it from the requirements.

## How to use these in an interview

Name the trade-off out loud, state which side you pick, and tie it to the requirement. The decision matters less than showing you understand the cost of each option. "This is a feed, so I favor availability and eventual consistency" beats silently picking one.

## Go deeper

- Read more (free): [Consistency Patterns in Distributed Systems](https://www.designgurus.io/blog/consistency-patterns-distributed-systems), [Monolithic vs Microservices vs SOA](https://www.designgurus.io/blog/monolithic-service-oriented-microservice-architecture)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)