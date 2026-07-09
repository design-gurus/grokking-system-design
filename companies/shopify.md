# Shopify: system design interview

> How Shopify actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Shopify runs it.** Commerce infrastructure with merchant obsession as the grading lens: designs are judged on how they protect a small business owner's sale. Flash-sale bursts (a creator drop melting checkout) are the canonical stress test.

## Signature questions

- Design checkout that survives a flash sale: queueing, inventory contention, degradation ladders
- Design inventory reservation across sales channels
- Design a multi-tenant storefront platform where every merchant customizes

## What interviewers probe

- The merchant framing: degraded search is acceptable, broken checkout never is
- Hot-SKU contention handled structurally
- Multi-tenant fairness: one viral store cannot slow the rest

## Prepare

- Patterns to review: [rate limiting](../patterns/rate-limiting.md), [message queues](../patterns/message-queues.md), [idempotency](../patterns/idempotency.md), [caching](../patterns/caching.md)
- Practice questions: [Design flash sale system](../questions/design-flash-sale-system.md), [Design amazon shopping cart](../questions/design-amazon-shopping-cart.md)
- Full company guide: [Shopify system design interview](https://www.designgurus.io/answers/detail/what-shopify-system-design-interview-questions-to-prepare?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
