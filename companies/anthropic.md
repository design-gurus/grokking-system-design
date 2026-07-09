# Anthropic: system design interview

> How Anthropic actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Anthropic runs it.** Prompts wear AI framing (GPU clusters, inference batches) but the core problems are classic infrastructure: queuing, batching, routing, and failure handling, with the model treated as a black box. Problems are often novel and close to what their teams are actively solving, so the interviewer may not have one correct answer in mind.

## Signature questions

- Design an inference batching system for a single GPU that processes up to 100 inputs per batch while users wait synchronously (the most-reported prompt)
- Scale that batching design to a fleet of GPUs with routing, capacity tracking, and mid-batch failover
- Design an LLM token-generation service handling ~100,000 requests per second
- Design a distributed search system over ~1B documents at ~1M queries per second

## What interviewers probe

- Requirements discipline: extract latency targets and throughput numbers before drawing boxes
- Failure modes raised unprompted: GPU dies mid-batch, retries need idempotency, bounded queues with backpressure
- Comfort decomposing an unsolved problem instead of pattern-matching a memorized architecture

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [load balancing](../patterns/load-balancing.md), [idempotency](../patterns/idempotency.md), [rate limiting](../patterns/rate-limiting.md)
- Practice questions: [Design chatgpt](../questions/design-chatgpt.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md)
- Full company guide: [Anthropic system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-anthropic-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
