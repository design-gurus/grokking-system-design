# Roblox: system design interview

> How Roblox actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Roblox runs it.** Gaming-platform physics: real-time multiplayer state under human-reflex latency budgets, matchmaking and session placement, a real virtual economy, and safety systems for an audience heavy with minors. Latency, concurrency, and fault tolerance are graded hard.

## Signature questions

- Design real-time state replication with interest management (players receive what is near them)
- Design matchmaking and session placement with viral-experience thundering herds
- Design the virtual economy backbone: Robux transactions with money-grade integrity
- Design chat moderation with kid-grade strictness at massive throughput

## What interviewers probe

- Interest-management arithmetic converting quadratic fan-out into tractable streams
- Creator code as untrusted, wildly variable workload
- Safety with age-tier semantics, designed fail-safe

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [message queues](../patterns/message-queues.md), [idempotency](../patterns/idempotency.md), [rate limiting](../patterns/rate-limiting.md)
- Practice questions: [Design discord](../questions/design-discord.md), [Design live comment streaming](../questions/design-live-comment-streaming.md)
- Full company guide: [Roblox system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-roblox-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
