# Walmart Global Tech: system design interview

> How Walmart Global Tech actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Walmart Global Tech runs it.** Retail at the world's largest scale: omnichannel inventory truth across 10,000+ stores and a digital catalog, Black Friday burst engineering, and supply-chain systems. Physical inventory is an estimate, so designs promise conservatively and reconcile continuously.

## Signature questions

- Design omnichannel inventory with buy-online-pickup-in-store: buffers, reservations, and the physical seam
- Design cart and checkout for Black Friday: waiting rooms, hot-SKU token allocation, degradation ladders
- Design order fulfillment routing across warehouses and stores

## What interviewers probe

- Inventory-truth honesty: shrink, drift, and conservative promising
- Burst arithmetic on a known calendar with pre-scaled capacity
- Consistency budgets by money-proximity

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [message queues](../patterns/message-queues.md), [caching](../patterns/caching.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design flash sale system](../questions/design-flash-sale-system.md), [Design amazon shopping cart](../questions/design-amazon-shopping-cart.md)
- Full company guide: [Walmart Global Tech system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-walmart-global-tech-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
