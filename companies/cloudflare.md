# Cloudflare: system design interview

> How Cloudflare actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Cloudflare runs it.** Internet-infrastructure scale: global edge networks, DDoS-magnitude traffic, and systems that must degrade gracefully when the internet itself misbehaves. Curiosity about protocol-level details is part of the culture and the evaluation.

## Signature questions

- Design a CDN or global edge network with cache hierarchies and invalidation
- Design DDoS mitigation or a global rate limiter
- Design DNS or proxy infrastructure at internet scale

## What interviewers probe

- Anycast, edge-versus-origin, and protocol fluency
- Graceful degradation under attack-scale load
- Blast-radius thinking for systems the internet depends on

## Prepare

- Patterns to review: [cdn](../patterns/cdn.md), [load balancing](../patterns/load-balancing.md), [rate limiting](../patterns/rate-limiting.md), [proxies](../patterns/proxies.md)
- Practice questions: [Design api gateway](../questions/design-api-gateway.md), [Design rate limiter](../questions/design-rate-limiter.md)
- Full company guide: [Cloudflare system design interview](https://www.designgurus.io/answers/detail/what-cloudflare-system-design-interview-questions-to-prepare?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
