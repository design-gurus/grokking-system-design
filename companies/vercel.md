# Vercel: system design interview

> How Vercel actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Vercel runs it.** The platform's own shapes: atomic immutable deployments, preview environments, build systems with layered caching, and edge networks, with developer experience graded as a design requirement (time-from-push-to-preview is the product).

## Signature questions

- Design preview deployments: an isolated environment per pull request, where idle previews cost a routing entry, not a server
- Design a build system: content-keyed caches, per-tenant fairness, burst absorption
- Design serverless function infrastructure: cold starts, scale-to-zero economics

## What interviewers probe

- Atomicity and rollback instincts: pointer swaps, never in-place mutation
- Multi-tenant economics with free-tier abuse realities
- Failure legibility: builds that fail atomically with errors naming the cause

## Prepare

- Patterns to review: [cdn](../patterns/cdn.md), [caching](../patterns/caching.md), [message queues](../patterns/message-queues.md), [load balancing](../patterns/load-balancing.md)
- Practice questions: [Design code deployment system](../questions/design-code-deployment-system.md), [Design amazon lambda](../questions/design-amazon-lambda.md)
- Full company guide: [Vercel system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-vercel-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
