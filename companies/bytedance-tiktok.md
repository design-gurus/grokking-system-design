# ByteDance / TikTok: system design interview

> How ByteDance / TikTok actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How ByteDance / TikTok runs it.** Short-video planet scale: the For You feed backend, video upload and transcoding, and live-streaming infrastructure, with one grading behavior above the rest: justify tradeoffs explicitly, down to why you sacrificed consistency for availability during a viral spike.

## Signature questions

- Design the For You feed serving path: interaction pipelines, candidate generation, ranking under 100ms
- Design massive video upload and transcoding with moderation in the pipeline
- Design live-streaming comment infrastructure for millions of concurrent viewers

## What interviewers probe

- Hot-key instincts: one video attracting a meaningful share of global traffic within minutes
- Feed decomposition: cheap candidates, expensive ranking, feature freshness
- Explicit tradeoff defense with quantitative reasoning

## Prepare

- Patterns to review: [caching](../patterns/caching.md), [cdn](../patterns/cdn.md), [message queues](../patterns/message-queues.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design recommendation system](../questions/design-recommendation-system.md), [Design live comment streaming](../questions/design-live-comment-streaming.md), [Design youtube](../questions/design-youtube.md)
- Full company guide: [ByteDance / TikTok system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-bytedance-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
