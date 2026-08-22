# Jump Trading: system design interview

> How Jump Trading actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Jump Trading runs it.** Systems questions are spread across the loop instead of concentrated in one design round, and the emphasis stays low-level: memory, threads, sockets, and the cost of each. Candidates report a phone screen mixing coding with systems fundamentals, a 45 to 60 minute session on designing a low-latency component, and a separate C++ session covering the memory model and the cost of abstractions. Throughput questions about storing billions of market events per day pull in the distributed layer, but latency thinking is the core.

## Signature questions

- Design a market data feed handler
- Design an order gateway or an in-memory order book
- Design a fast logging pipeline
- Design a store for billions of market events per day for research and replay
- Share data between one fast writer thread and many readers without locks

## What interviewers probe

- Whether you reason with real magnitudes: the cost of a cache miss, a lock, a system call, a network hop
- Failure handling on feeds: sequence gaps, replay requests, and marking data stale meanwhile
- A straight path with few branches, preallocated memory, and a pinned hot thread, each justified
- Intellectual honesty: saying what you have not used beats confident guessing

## Prepare

- Patterns to review: [backpressure](../patterns/backpressure.md), [message queues](../patterns/message-queues.md), [sharding partitioning](../patterns/sharding-partitioning.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md)
- Practice questions: [Design stock exchange](../questions/design-stock-exchange.md), [Design distributed message queue](../questions/design-distributed-message-queue.md), [Design ad click aggregator](../questions/design-ad-click-aggregator.md)
- Full company guide: [Jump Trading system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-jump-trading-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
