# Groq: system design interview

> How Groq actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Groq runs it.** Conversations run on inference-at-speed atop deterministic, compiler-scheduled silicon: execution time is knowable, which turns scheduling into bin-packing and admission control into a real-time capacity ledger that can make honest promises. Fixed-supply hardware makes utilization the margin.

## Signature questions

- Design the inference-serving API: routing, admission control, streaming, first-token latency accounted stage by stage
- Design scheduling for deterministic accelerators (exploit predictability rather than importing GPU-style reactive queueing)
- Design multi-model capacity management: residency, rebalancing, and cold-swap costs on fixed fleets
- Design tiered rate limiting where paid-tier latency never degrades

## What interviewers probe

- Latency decomposed with numbers: queueing is the variance when execution is deterministic
- Determinism exploited, not ignored: precise capacity math and honest SLAs
- Throughput-latency tension navigated deliberately for a speed-first product

## Prepare

- Patterns to review: [rate limiting](../patterns/rate-limiting.md), [load balancing](../patterns/load-balancing.md), [message queues](../patterns/message-queues.md)
- Practice questions: [Design rate limiter](../questions/design-rate-limiter.md), [Design api gateway](../questions/design-api-gateway.md)
- Full company guide: [Groq system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-groq-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
