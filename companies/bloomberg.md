# Bloomberg: system design interview

> How Bloomberg actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Bloomberg runs it.** Consistently reported as the loop's hardest round: real-time financial systems probed with relentless "why this and not the alternative" follow-ups. The domain canon (conflation, slow-consumer protection, A/B feeds, entitlements) separates fluent designs from generic pub-sub.

## Signature questions

- Design market-data distribution to hundreds of thousands of Terminal subscribers with per-user entitlements
- Design a price-alert system at Bloomberg scale
- Design news ingestion: thousands of sources, dedup, entity tagging, seconds from wire to screen

## What interviewers probe

- Conflation literacy: coalescing latest-value per instrument to consumer-appropriate rates
- Failure handling as the second half of every answer, with staleness always visible
- Entitlements as architecture, checked at scale without becoming the bottleneck

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [caching](../patterns/caching.md), [load balancing](../patterns/load-balancing.md), [long polling websockets sse](../patterns/long-polling-websockets-sse.md)
- Practice questions: [Design stock exchange](../questions/design-stock-exchange.md), [Design google news](../questions/design-google-news.md)
- Full company guide: [Bloomberg system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-bloomberg-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
