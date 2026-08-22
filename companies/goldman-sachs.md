# Goldman Sachs: system design interview

> How Goldman Sachs actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Goldman Sachs runs it.** One dedicated design round at the Superday can set the level of the offer, and the interviewer spends much of it pushing on failure cases: what happens when this feed stops, and who notices first. The problem arrives broad with details missing on purpose, discussed at a whiteboard or shared drawing tool, and the questions track the firm's own systems: trading, market data, risk, and banking. Entry-level candidates get little or no design, and some interviewers still ask classics such as a URL shortener, a notification service, or a rate limiter.

## Signature questions

- Design a real-time trading platform
- Design a risk monitoring system that reads data from multiple exchanges
- Design an order management system or a price feed handler
- Design a reporting pipeline or a reference data service
- Design a URL shortener, notification service, or rate limiter (classics still appear)

## What interviewers probe

- The first five minutes: questions asked, requirements stated, and constraints named for latency, throughput, storage, and failure
- Trade-offs defended out loud, such as fast slightly stale alerts backed by exact end-of-day reconciliation
- Volunteered failure thinking, including detecting a dead feed and alerting on staleness itself
- Plain, clear explanation of technical choices, since Goldman engineers work next to the business

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md), [heartbeats](../patterns/heartbeats.md), [caching](../patterns/caching.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design stock exchange](../questions/design-stock-exchange.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design notification system](../questions/design-notification-system.md), [Design tinyurl](../questions/design-tinyurl.md)
- Full company guide: [Goldman Sachs system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-goldman-sachs-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
