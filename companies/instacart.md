# Instacart: system design interview

> How Instacart actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Instacart runs it.** The source of truth is a physical shelf the company does not control, and that one fact generates most of the round. Questions are narrow and product-shaped, an hour on a shared drawing tool, with the interviewer steering scope toward a single feature across real-time inventory, shopper dispatch, and order fulfillment. Depth inside a small scope beats breadth here, and responding to the steering rather than fighting it is itself graded.

## Signature questions

- Design real-time inventory when shelves change without notice
- Design the order fulfillment flow from placement to delivery
- Design shopper dispatch and order batching
- Design substitutions with live customer approval
- Design catalog search over a large grocery catalog

## What interviewers probe

- Depth in a narrow scope: going deep on one flow beats naming twenty services, and proposing the next detail yourself reads well
- Collaboration in a guided round: checking in after each step and asking which area to expand
- The feedback path interviewers hope you find, where shopper corrections update inventory for the next customer
- Real-world judgment about wrong data: staleness scores, caching for browsing but rechecking availability at checkout, and one failure case with recovery

## Prepare

- Patterns to review: [caching](../patterns/caching.md), [message queues](../patterns/message-queues.md), [idempotency](../patterns/idempotency.md), [sharding partitioning](../patterns/sharding-partitioning.md), [consistency models](../patterns/consistency-models.md)
- Practice questions: [Design food delivery](../questions/design-food-delivery.md), [Design amazon shopping cart](../questions/design-amazon-shopping-cart.md), [Design payment system](../questions/design-payment-system.md)
- Full company guide: [Instacart system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-instacart-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
