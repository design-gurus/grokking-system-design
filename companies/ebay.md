# eBay: system design interview

> How eBay actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How eBay runs it.** Auction mechanics are the sharpest test in this loop: many bids on one item in the same second, a hard deadline, and exactly one winner. The round runs 45 to 60 minutes on a virtual whiteboard in the final loop, and candidates report it weighs heavily on the seniority level of the offer. Questions mirror the product line: listings and bidding, marketplace search, checkout and payouts, fraud pipelines, and notifications.

## Signature questions

- Design a bidding system for a live auction
- Design product search and a recommendation feed for the marketplace
- Design checkout and seller payout
- Design a fraud detection pipeline
- Design a clickstream pipeline or a feature flag service

## What interviewers probe

- Capacity numbers on demand: bids per second, storage per day, cache size, server count
- Where strong consistency is required (bids, payments) versus where eventual is fine (view counts, search freshness)
- Failure plans stated without being asked: cache dies, one shard runs slow
- Hot-item skew, meaning one popular auction overloading a single shard, raised before the interviewer raises it

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [message queues](../patterns/message-queues.md), [caching](../patterns/caching.md), [sharding partitioning](../patterns/sharding-partitioning.md), [long polling websockets sse](../patterns/long-polling-websockets-sse.md)
- Practice questions: [Design flash sale system](../questions/design-flash-sale-system.md), [Design ticketmaster](../questions/design-ticketmaster.md), [Design amazon shopping cart](../questions/design-amazon-shopping-cart.md), [Design payment system](../questions/design-payment-system.md)
- Full company guide: [eBay system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-ebay-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
