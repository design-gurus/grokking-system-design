# Glossary

Common system design vocabulary, in plain language. Terms with a dedicated page link to it.

- **[Availability](fundamentals/availability-patterns.md)**: the percentage of time a system is operational and able to serve requests. Often stated in nines (99.9 percent is "three nines").
- **[Back pressure](fundamentals/asynchronism.md)**: a system pushing back on producers when consumers can't keep up, so queues don't grow unbounded.
- **[Cache](patterns/caching.md)**: a fast store holding copies of data to speed up repeated reads.
- **[CAP theorem](patterns/cap-theorem.md)**: under a network partition, a distributed system can guarantee either consistency or availability, not both at once.
- **[CDN (content delivery network)](patterns/cdn.md)**: a network of edge servers that cache static content close to users.
- **[Consistency](patterns/consistency-models.md)**: every read reflects the most recent write. Models range from strong to eventual.
- **[Consistent hashing](patterns/consistent-hashing.md)**: a hashing scheme that minimizes how much data moves when nodes are added or removed.
- **[Denormalization](fundamentals/databases.md)**: deliberately duplicating or precomputing data so reads hit one place instead of joining, trading write cost for read speed.
- **[DNS (Domain Name System)](fundamentals/dns.md)**: the internet's phone book, resolving a hostname to an IP address; also a tool for load distribution and failover.
- **[Eventual consistency](fundamentals/consistency-patterns.md)**: replicas converge to the same value over time, but a read may briefly return stale data.
- **[Federation](fundamentals/databases.md)**: splitting databases by function (users, products, orders) so each scales independently.
- **[Horizontal scaling](fundamentals/performance-vs-scalability.md)**: adding more machines. Contrast with vertical scaling (a bigger machine).
- **Idempotency**: an operation that has the same effect whether applied once or many times. Important for retries.
- **[Latency](fundamentals/latency-vs-throughput.md)**: the time to serve a single request. Contrast with throughput (requests per unit time).
- **[Load balancer](patterns/load-balancing.md)**: distributes incoming traffic across multiple servers.
- **[Message queue](patterns/message-queues.md)**: a buffer that decouples producers from consumers and enables async processing.
- **[Partition (shard)](patterns/sharding-partitioning.md)**: a horizontal slice of data stored on a separate node.
- **[Quorum](patterns/replication.md)**: the minimum number of nodes that must agree for a read or write to succeed.
- **[Rate limiting](patterns/rate-limiting.md)**: capping how many requests a client can make in a window.
- **[Replication](patterns/replication.md)**: keeping copies of data on multiple nodes for availability and read scaling.
- **[Reverse proxy](fundamentals/reverse-proxy-vs-load-balancer.md)**: a server that fronts your backends, adding TLS termination, caching, and security at one entry point.
- **[RPC (remote procedure call)](fundamentals/communication.md)**: an API style where the client calls what looks like a local function; contrast with REST's resource model.
- **[Service discovery](fundamentals/application-layer.md)**: how a caller finds a healthy instance of a service whose instances come and go.
- **[Sharding](patterns/sharding-partitioning.md)**: partitioning data across nodes so the dataset scales beyond one machine.
- **[Throughput](fundamentals/latency-vs-throughput.md)**: the number of requests a system handles per unit time.
- **Write-ahead log (WAL)**: an append-only log written before applying changes, used for durability and recovery.

## Go deeper

Every term here is covered in depth in the [course](https://www.designgurus.io/course/grokking-the-system-design-interview).