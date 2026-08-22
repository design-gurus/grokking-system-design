# Hudson River Trading: system design interview

> How Hudson River Trading actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Hudson River Trading runs it.** There is no classic web-scale round here: the design questions are about one machine and the microseconds between a packet arriving and an output leaving. Candidates report lock-free data structures, CPU cache effects, and kernel bypass networking, especially for core developer roles, alongside direct fundamentals questions on virtual memory, context switches, and TCP behavior. Latency is graded in percentiles, so the 99th percentile belongs in your answer before the interviewer asks for it.

## Signature questions

- Design a market data feed handler that keeps an accurate order book
- Design a pipeline that consumes a high-rate feed and reacts within a strict time budget
- Design a lock-free structure that several threads share without corruption
- Diagnose a latency problem: name your measurements in order and the likely causes
- Explain what a context switch costs and where it shows up in your design

## What interviewers probe

- Whether you talk in percentiles rather than averages, and can name where you would timestamp
- Feed correctness: sequence numbers, gap detection, replay requests, and never trading on a stale book
- Honest accounting of the lock-free trade-off, including that it is harder to write and to prove correct
- Depth on threads, core pinning, memory layout, and kernel bypass rather than box drawing

## Prepare

- Patterns to review: [backpressure](../patterns/backpressure.md), [message queues](../patterns/message-queues.md), [checksums](../patterns/checksums.md), [heartbeats](../patterns/heartbeats.md)
- Practice questions: [Design stock exchange](../questions/design-stock-exchange.md), [Design distributed message queue](../questions/design-distributed-message-queue.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md)
- Full company guide: [Hudson River Trading system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-hudson-river-trading-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
