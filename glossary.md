# Glossary

Common system design vocabulary, in plain language. Terms with their own cheat sheet link to it.

- **Availability**: the percentage of time a system is operational and able to serve requests. Often stated in nines (99.9 percent is "three nines").
- **[Cache](patterns/caching.md)**: a fast store holding copies of data to speed up repeated reads.
- **CAP theorem**: under a network partition, a distributed system can guarantee either consistency or availability, not both at once.
- **CDN (content delivery network)**: a network of edge servers that cache static content close to users.
- **Consistency**: every read reflects the most recent write. Models range from strong to eventual.
- **[Consistent hashing](patterns/consistent-hashing.md)**: a hashing scheme that minimizes how much data moves when nodes are added or removed.
- **Eventual consistency**: replicas converge to the same value over time, but a read may briefly return stale data.
- **Horizontal scaling**: adding more machines. Contrast with vertical scaling (a bigger machine).
- **Idempotency**: an operation that has the same effect whether applied once or many times. Important for retries.
- **Latency**: the time to serve a single request. Contrast with throughput (requests per unit time).
- **[Load balancer](patterns/load-balancing.md)**: distributes incoming traffic across multiple servers.
- **[Message queue](patterns/message-queues.md)**: a buffer that decouples producers from consumers and enables async processing.
- **Partition (shard)**: a horizontal slice of data stored on a separate node.
- **Quorum**: the minimum number of nodes that must agree for a read or write to succeed.
- **[Rate limiting](patterns/rate-limiting.md)**: capping how many requests a client can make in a window.
- **[Replication](patterns/replication.md)**: keeping copies of data on multiple nodes for availability and read scaling.
- **Sharding**: partitioning data across nodes so the dataset scales beyond one machine.
- **Throughput**: the number of requests a system handles per unit time.
- **Write-ahead log (WAL)**: an append-only log written before applying changes, used for durability and recovery.

## Go deeper

Every term here is covered in depth in the [course](https://www.designgurus.io/course/grokking-the-system-design-interview).