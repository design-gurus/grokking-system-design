# Patterns: the building blocks of system design

Learn these once and you can assemble an answer to almost any design question. Each file is a short, practical cheat sheet: what the pattern is, when to use it, the trade-offs, and how to talk about it in an interview.

| Pattern | What it solves | Status |
|---------|----------------|--------|
| [Caching](caching.md) | Read latency and load on the data store | Written |
| [Load balancing](load-balancing.md) | Distributing traffic across servers | Written |
| Sharding and partitioning | Scaling data beyond one machine | Planned |
| Replication | Availability and read scaling | Planned |
| Consistency models | Correctness under concurrency | Planned |
| CAP theorem | Reasoning about trade-offs under partitions | Planned |
| Consistent hashing | Even distribution with minimal reshuffling | Planned |
| Message queues | Decoupling and async processing | Planned |
| Rate limiting | Protecting services from overload | Planned |
| CDN | Serving static content close to users | Planned |
| Database indexing | Fast lookups | Planned |
| Bloom filters | Cheap "definitely not present" checks | Planned |

## Add a new pattern

1. Copy [_template.md](_template.md) to `patterns/your-pattern.md`.
2. Fill in each section.
3. Add a row above and, if it is a core pattern, to the table in the root [README](../README.md).

For the full, in-depth treatment of every pattern with interactive diagrams, see the [course](https://www.designgurus.io/course/grokking-the-system-design-interview).