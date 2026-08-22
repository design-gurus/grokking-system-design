# Cerebras: system design interview

> How Cerebras actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Cerebras runs it.** The round splits by team: cloud and platform roles get a classic distributed systems question, while systems software roles get lower-level design covering memory, scheduling, and data movement on unusual hardware. Both versions run about 45 to 60 minutes with an engineer, and the product constraint drives the answer, because wafer-scale machines are few and expensive, so the scheduler matters more than the gateway. Designs that assume an infinite pool of identical servers miss the company's actual constraint.

## Signature questions

- Design a fast inference API that protects a very high token rate
- Design a data pipeline that keeps a very fast machine from sitting idle
- Design job scheduling across a small pool of expensive machines
- Design telemetry and monitoring for a fleet where every idle hour is lost money
- Design the memory movement and batching path, for systems software roles

## What interviewers probe

- Latency budgets stated per stage and then checked against the target
- Reasoning about scarcity rather than assuming servers can be added freely
- Hardware awareness: showing that keeping the machine busy decides the design
- Failure planning when one machine is a large share of total capacity

## Prepare

- Patterns to review: [api gateway](../patterns/api-gateway.md), [rate limiting](../patterns/rate-limiting.md), [backpressure](../patterns/backpressure.md), [long polling websockets sse](../patterns/long-polling-websockets-sse.md), [heartbeats](../patterns/heartbeats.md)
- Practice questions: [Design llm inference platform](../questions/design-llm-inference-platform.md), [Design gpu cluster scheduler](../questions/design-gpu-cluster-scheduler.md), [Design llm gateway](../questions/design-llm-gateway.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md)
- Full company guide: [Cerebras system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-cerebras-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
