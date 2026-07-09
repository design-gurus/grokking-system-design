# Cohere: system design interview

> How Cohere actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Cohere runs it.** The round runs on enterprise AI serving: multi-tenant models at low latency, retrieval with measured quality, and deployment into customer VPCs. Candidate reports name the probes directly: cost-per-query, latency budgets, GPU scheduling, and tenant isolation.

## Signature questions

- Design multi-tenant model serving with tier guarantees, noisy-neighbor protection, and utilization economics
- Design a RAG platform where evaluation (golden sets, regression gates) is core architecture
- Design fine-tuning as a product: training orchestration, model registry, rollback across hundreds of customer fine-tunes

## What interviewers probe

- KV-cache capacity math: concurrent streams x context length as the real formula
- Tenant isolation including the subtle leak paths: caches, logs, fine-tunes
- Deployment-constraint judgment for customer-controlled infrastructure

## Prepare

- Patterns to review: [rate limiting](../patterns/rate-limiting.md), [caching](../patterns/caching.md), [message queues](../patterns/message-queues.md), [consistency models](../patterns/consistency-models.md)
- Practice questions: [Design chatgpt](../questions/design-chatgpt.md), [Design rate limiter](../questions/design-rate-limiter.md)
- Full company guide: [Cohere system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-cohere-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
