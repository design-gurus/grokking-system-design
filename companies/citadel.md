# Citadel: system design interview

> How Citadel actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Citadel runs it.** A different sport from web-scale design: the unit of latency is the microsecond, the data source is a market-data firehose, and correctness bugs convert directly into lost money. Strong candidates open with a latency budget and spend it stage by stage.

## Signature questions

- Design a real-time order book: single-writer per instrument, allocation-free hot paths, snapshot-plus-journal recovery
- Design a market data normalizer: A/B feed arbitration, gap detection, downstream staleness signaling
- Latency-budget redesigns: take a 500-microsecond pipeline under 50

## What interviewers probe

- Mechanical sympathy: cache lines, allocation, kernel bypass, lock-free reasoning
- The single-writer mindset: avoid coordination rather than manage it
- Speed-versus-safety tradeoffs named and engineered, not waved at

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [write ahead log](../patterns/write-ahead-log.md), [idempotency](../patterns/idempotency.md)
- Practice questions: [Design stock exchange](../questions/design-stock-exchange.md)
- Full company guide: [Citadel system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-citadel-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
