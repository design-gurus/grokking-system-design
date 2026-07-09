# Robinhood: system design interview

> How Robinhood actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Robinhood runs it.** Brokerage-grade correctness under consumer-scale experience: real-time market data to millions of app sessions, order paths where a bug is someone's money, and market-open bursts as the capacity benchmark. Using Safety First as an explicit design lens lands well with interviewers.

## Signature questions

- Design real-time market data delivery: per-symbol subscriptions, coalescing to screen rates, visible staleness
- Design the order submission path: idempotent, state-machined, reconciled against executions
- Design price alerts: millions of triggers, inverted indexing by symbol, exactly-once notification

## What interviewers probe

- The read/write asymmetry: market data loss-tolerant, order flow neither lost nor duplicated
- Market-hours burst physics: the open as the design point
- Fail-safe degradation: block market orders before showing wrong prices

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [message queues](../patterns/message-queues.md), [long polling websockets sse](../patterns/long-polling-websockets-sse.md), [rate limiting](../patterns/rate-limiting.md)
- Practice questions: [Design stock exchange](../questions/design-stock-exchange.md), [Design reminder alert system](../questions/design-reminder-alert-system.md)
- Full company guide: [Robinhood system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-robinhood-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
