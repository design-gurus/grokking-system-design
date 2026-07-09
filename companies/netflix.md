# Netflix: system design interview

> How Netflix actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Netflix runs it.** Design conversations lean on streaming-scale realities: CDN strategy, personalization, and resilience engineering (this is the company that invented chaos engineering). Senior loops probe operational maturity hard.

## Signature questions

- Design a video streaming platform: encoding tiers, CDN placement, adaptive bitrate
- Design the recommendation and personalization pipeline
- Design for resilience: regional failover, graceful degradation, chaos-tested assumptions

## What interviewers probe

- Read-heavy scale arithmetic and cache economics
- Degradation ladders: what dims first when things fail, and what never does
- Operational thinking: rollout, monitoring, and blast-radius control

## Prepare

- Patterns to review: [cdn](../patterns/cdn.md), [caching](../patterns/caching.md), [circuit breaker](../patterns/circuit-breaker.md), [load balancing](../patterns/load-balancing.md)
- Practice questions: [Design netflix](../questions/design-netflix.md), [Design youtube](../questions/design-youtube.md), [Design recommendation system](../questions/design-recommendation-system.md)
- Full company guide: [Netflix system design interview](https://www.designgurus.io/answers/detail/what-are-the-top-system-design-interview-questions-for-netflix-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
