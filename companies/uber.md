# Uber: system design interview

> How Uber actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Uber runs it.** Marketplace systems with physical-world constraints: matching, location, pricing, and ETAs, where every design decision trades rider experience against driver earnings. Expect the three-sided reasoning to be probed as hard as the architecture.

## Signature questions

- Design ride matching and dispatch: real-time driver location, supply-demand balancing
- Design surge pricing or a fare-calculation pipeline
- Design location ingestion and ETA computation at city scale

## What interviewers probe

- Geospatial partitioning and hot-city handling
- Marketplace tradeoffs named explicitly with both sides costed
- Real-time state at scale: driver positions as a firehose

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [message queues](../patterns/message-queues.md), [caching](../patterns/caching.md), [load balancing](../patterns/load-balancing.md)
- Practice questions: [Design uber](../questions/design-uber.md)
- Full company guide: [Uber system design interview](https://www.designgurus.io/answers/detail/what-are-the-top-system-design-interview-questions-for-uber-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
