# Unity: system design interview

> How Unity actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Unity runs it.** The round splits by track, so backend candidates design distributed services while engine candidates design memory, allocation, and object lifetimes against a frame budget. It runs about 60 minutes inside the virtual final set, with backend prompts on telemetry, real-time multiplayer, and microservice splits, and engine prompts on object pooling, event systems, and Entity Component System trade-offs. Know your track before the interview, but prepare one design from each side, since candidates report cross-track follow-ups.

## Signature questions

- Design a game telemetry pipeline for millions of sessions
- Design real-time multiplayer session and presence services
- Design a split of a monolith into services that stay consistent
- Design an object pool that avoids memory churn
- Design an in-engine event system with no direct references between systems

## What interviewers probe

- Arithmetic out loud: bytes per event to megabytes per second to ingestion servers and queue partitions
- Naming the two-path design (a streaming path for live dashboards, a batch path for complete data) earns credit
- Operations depth beyond the diagram: monitoring, rollout, and what storage costs at this scale
- Client-side realism for games on weak devices: batching, compression, and dropping low-value events when buffers fill

## Prepare

- Patterns to review: [batch vs stream processing](../patterns/batch-vs-stream-processing.md), [message queues](../patterns/message-queues.md), [backpressure](../patterns/backpressure.md), [sharding partitioning](../patterns/sharding-partitioning.md), [consistency models](../patterns/consistency-models.md)
- Practice questions: [Design ad click aggregator](../questions/design-ad-click-aggregator.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design distributed message queue](../questions/design-distributed-message-queue.md)
- Full company guide: [Unity system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-unity-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
