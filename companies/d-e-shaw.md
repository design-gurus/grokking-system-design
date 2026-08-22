# D. E. Shaw: system design interview

> How D. E. Shaw actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How D. E. Shaw runs it.** Design sessions go mainly to senior candidates, one 45 to 60 minute session in the final round, and the weight sits on correctness rather than scale. Junior candidates get less formal design work but still meet systems questions inside coding rounds, plus a background round about systems they actually built. Interviewers pick the component you rushed and ask what breaks it, so design at even depth and name your checks before anyone requests them.

## Signature questions

- Design a market data pipeline that collects, cleans, and stores data for researchers
- Design an order management service
- Design a risk check that sits before orders reach an exchange
- Design a system that runs thousands of research jobs and manages their resources
- Design the failure path when a feed stops or two systems disagree

## What interviewers probe

- Estimation out loud: events per second, bytes per event, storage per year, with honest arithmetic
- Splitting the live path from the durable history path instead of one system serving both goals
- Correctness machinery: sequence gaps, replay, deduplication on write, and daily reconciliation against the source
- Acknowledged uncertainty, since candidates report that confident bluffing is detected and penalized

## Prepare

- Patterns to review: [batch vs stream processing](../patterns/batch-vs-stream-processing.md), [sharding partitioning](../patterns/sharding-partitioning.md), [idempotency](../patterns/idempotency.md), [checksums](../patterns/checksums.md), [replication](../patterns/replication.md)
- Practice questions: [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design stock exchange](../questions/design-stock-exchange.md), [Design ad click aggregator](../questions/design-ad-click-aggregator.md)
- Full company guide: [D. E. Shaw system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-d-e-shaw-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
