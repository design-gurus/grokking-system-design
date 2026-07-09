# Discord: system design interview

> How Discord actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Discord runs it.** The famous real-time canon: message fan-out where three-friend groups and million-member servers share one product surface, presence at hundreds of millions, and low-latency voice. The expected package is diagrams plus tradeoffs plus failure plans, together.

## Signature questions

- Design chat message delivery across server sizes: naive broadcast below a threshold, interest-managed above it
- Design presence and activity status with coalescing (loss-tolerant, cheap, enormous)
- Design voice infrastructure: regional SFU-style servers, failover mid-conversation
- Design message storage for the trillion-message problem

## What interviewers probe

- The fan-out asymmetry handled explicitly with a threshold argument
- Connection-state realism: gateways, resume semantics, reconnect storms
- Ephemeral-versus-durable guarantees assigned per data class

## Prepare

- Patterns to review: [long polling websockets sse](../patterns/long-polling-websockets-sse.md), [message queues](../patterns/message-queues.md), [sharding partitioning](../patterns/sharding-partitioning.md), [caching](../patterns/caching.md)
- Practice questions: [Design discord](../questions/design-discord.md), [Design whatsapp](../questions/design-whatsapp.md), [Design live comment streaming](../questions/design-live-comment-streaming.md)
- Full company guide: [Discord system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-discord-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
