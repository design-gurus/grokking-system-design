# Airbnb: system design interview

> How Airbnb actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Airbnb runs it.** Two-sided marketplace design with inventory that is unique and calendar-bound: search and ranking over listings, booking consistency (no double-booked nights), and trust systems. Product empathy for hosts and guests earns credit alongside architecture.

## Signature questions

- Design listing search with filters, ranking, and map views
- Design the booking system: calendar consistency, holds, and payments
- Design reviews and trust/fraud systems for a two-sided market

## What interviewers probe

- Booking correctness: the double-book is the cardinal failure
- Search relevance versus freshness tradeoffs
- Host-and-guest framing of every decision

## Prepare

- Patterns to review: [database indexing](../patterns/database-indexing.md), [consistency models](../patterns/consistency-models.md), [caching](../patterns/caching.md), [idempotency](../patterns/idempotency.md)
- Practice questions: [Design airbnb](../questions/design-airbnb.md)
- Full company guide: [Airbnb system design interview](https://www.designgurus.io/answers/detail/what-are-the-top-system-design-interview-questions-for-airbnb-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
