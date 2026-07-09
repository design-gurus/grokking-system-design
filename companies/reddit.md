# Reddit: system design interview

> How Reddit actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Reddit runs it.** Community-scale systems: feeds and ranking that balance engagement against community health, comment trees at enormous depth, and moderation tooling where volunteer moderators are load-bearing infrastructure.

## Signature questions

- Design the Reddit feed and ranking (hot/top/new) across wildly different community sizes
- Design comment trees: storage, pagination, and vote counting at thread scale
- Design moderation tooling and abuse detection for community-scale operations

## What interviewers probe

- Vote-count consistency: eventual with convergence, and why that is right
- Community-size skew: three-member and thirty-million-member subreddits on one architecture
- Trust and safety as architecture

## Prepare

- Patterns to review: [caching](../patterns/caching.md), [sharding partitioning](../patterns/sharding-partitioning.md), [message queues](../patterns/message-queues.md)
- Practice questions: [Design reddit](../questions/design-reddit.md), [Design youtube likes counter](../questions/design-youtube-likes-counter.md)
- Full company guide: [Reddit system design interview](https://www.designgurus.io/answers/detail/what-are-reddit-system-design-interview-questions?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
