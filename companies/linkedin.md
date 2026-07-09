# LinkedIn: system design interview

> How LinkedIn actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How LinkedIn runs it.** Product-centric prompts (feed, notifications, People You May Know) that are secretly graph problems: the key instinct is designing for extreme degree skew (most members have hundreds of connections; some have millions of followers). Tradeoff narration is explicitly graded.

## Signature questions

- Design the LinkedIn feed: hybrid push/pull fan-out by follower count
- Design People You May Know: triangle-closing at a billion-member scale with hot-node sampling
- Design a notification system where restraint (aggregation, rate limits per member) is a values statement
- Design job search and recommendations: two-sided matching with freshness

## What interviewers probe

- Graph-data instincts: skew handled structurally, not as an afterthought
- Product sense inside the architecture: why professional feeds differ from consumer ones
- Member-impact framing: designs end at what the user experiences

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [caching](../patterns/caching.md), [message queues](../patterns/message-queues.md), [database indexing](../patterns/database-indexing.md)
- Practice questions: [Design people you may know](../questions/design-people-you-may-know.md), [Design linkedin connections](../questions/design-linkedin-connections.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [LinkedIn system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-linkedin-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
