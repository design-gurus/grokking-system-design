# Okta: system design interview

> How Okta actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Okta runs it.** Security awareness is graded as a fourth signal next to structure, numbers, and depth, so token expiry, key rotation, encryption, and least privilege have to come up without a prompt. The round is about 60 minutes on a shared whiteboard or document, moving through requirements, high level design, a deep dive on one component, and trade-offs at the end. Even a generic question picks up an identity follow-up: a rate limiter becomes per-tenant rather than per-user, and a logging pipeline becomes a question about keeping secrets out of logs.

## Signature questions

- Design cross-domain single sign-on
- Design a distributed rate limiter
- Design session management and token issuance for a login service
- Design a real-time monitoring system
- Design a fraud detection pipeline for login traffic

## What interviewers probe

- Scoping the problem and stating users, apps, and uptime targets before drawing any boxes
- Estimation out loud: users, requests per second, and storage
- Depth on one component down to its data structures and failure cases
- Security vocabulary used unprompted: token expiry, key rotation, least privilege, encryption at rest

## Prepare

- Patterns to review: [api gateway](../patterns/api-gateway.md), [rate limiting](../patterns/rate-limiting.md), [caching](../patterns/caching.md), [replication](../patterns/replication.md), [load balancing](../patterns/load-balancing.md)
- Practice questions: [Design rate limiter](../questions/design-rate-limiter.md), [Design api gateway](../questions/design-api-gateway.md), [Design distributed cache](../questions/design-distributed-cache.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md)
- Full company guide: [Okta system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-okta-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
