# Non-functional requirements

> What a system must *be*, not just what it must *do*. These are the qualities interviewers probe, and the constraints that shape every design decision.

Functional requirements say what the system does (post a tweet, book a ride). Non-functional requirements say how well it must do it. Clarifying these early is one of the strongest signals in an interview, because they drive every later choice.

## The core qualities

| Quality | The question it answers | What it drives |
|---------|-------------------------|----------------|
| Scalability | Can it handle growth in users, data, and traffic? | Sharding, replication, stateless services |
| Availability | What fraction of time is it up? | Redundancy, failover, no single point of failure |
| Reliability | Does it work correctly, even under failure? | Retries, idempotency, durability |
| Latency | How fast is a single request? | Caching, CDNs, data locality |
| Throughput | How many requests per unit time? | Horizontal scaling, queues |
| Consistency | Do reads reflect the latest writes? | Replication and the consistency model |
| Durability | Is committed data ever lost? | Replication, write-ahead logs, backups |

## Scalability

- Vertical scaling (a bigger machine) is simple but capped; horizontal scaling (more machines) is how large systems grow. See [sharding](../patterns/sharding-partitioning.md).
- Stateless services scale horizontally easily, so push state into a data store or [cache](../patterns/caching.md).

## Availability

- Measured in nines: 99.9% is about 8.7 hours of downtime per year; 99.99% is about 52 minutes.
- Achieved with redundancy and by removing single points of failure (see [load balancing](../patterns/load-balancing.md) and [replication](../patterns/replication.md)).

## Reliability

- The system behaves correctly and recovers from failures. Idempotency and retries are central, so a repeated request does not cause a wrong result.

## Latency vs throughput

- Latency is the time for one request; throughput is requests per second. They are different and sometimes in tension. State a target for each (for example p99 latency under 200 ms, 10,000 requests per second).

## Consistency vs durability

- Consistency is about whether reads see the latest write (see [consistency models](../patterns/consistency-models.md) and the [CAP theorem](../patterns/cap-theorem.md)). Pick the weakest model the product tolerates, since weaker is faster and more available.
- Durability is about not losing acknowledged data, provided by replication and write-ahead logs.

## How to use this in an interview

State the non-functional requirements explicitly before you design, and put numbers on them: expected users and QPS, target latency, availability target, and the consistency the product needs. Then let those numbers justify every later decision. Skipping this step is one of the most common ways candidates lose the room.

## Go deeper

- Read more (free): [Scalability in System Design](https://www.designgurus.io/blog/grokking-system-design-scalability), [High Availability in System Design](https://www.designgurus.io/blog/high-availability-system-design-basics)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)