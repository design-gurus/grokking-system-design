# Together AI: system design interview

> How Together AI actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Together AI runs it.** Every question traces back to serving open-source models through an API: routing by model name, batching requests for GPU efficiency, and streaming tokens back one at a time. The round usually runs about 60 minutes with an engineer from an infrastructure team, and senior candidates are more likely to get a full design round while junior candidates may meet the same ideas inside the applied coding round. Latency reasoning with numbers for each stage of the request path counts for more here than a tidy box diagram.

## Signature questions

- Design a model inference API that serves many models for many customers
- Design the scheduler that batches incoming requests for GPU use
- Design token streaming over a long-lived connection
- Design quotas and fair rate limits for thousands of API customers
- Design a job scheduler for a shared GPU training cluster

## What interviewers probe

- Latency numbers per stage, especially time to first token against a stated target
- GPU scarcity: knowing why batching exists and what a bigger batch costs the first response
- Routing by model, since models are large and not every server holds every one
- Honest trade-offs named for each batching, caching, and scaling choice

## Prepare

- Patterns to review: [api gateway](../patterns/api-gateway.md), [rate limiting](../patterns/rate-limiting.md), [load balancing](../patterns/load-balancing.md), [caching](../patterns/caching.md), [long polling websockets sse](../patterns/long-polling-websockets-sse.md)
- Practice questions: [Design llm inference platform](../questions/design-llm-inference-platform.md), [Design llm gateway](../questions/design-llm-gateway.md), [Design rate limiter](../questions/design-rate-limiter.md), [Design gpu cluster scheduler](../questions/design-gpu-cluster-scheduler.md)
- Full company guide: [Together AI system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-together-ai-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
