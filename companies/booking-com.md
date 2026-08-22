# Booking.com: system design interview

> How Booking.com actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Booking.com runs it.** Selling the same room twice is treated as a real customer disaster, so correctness is graded ahead of raw scale. The round is 45 to 60 minutes on a virtual whiteboard for mid-level and senior engineers, built on travel systems: hotel search, availability, pricing, and the booking flow itself. Candidates report that clarifying questions at the start are expected rather than optional, and that the strongest senior signal is naming the pairing where search results may be seconds old while the booking check stays live.

## Signature questions

- Design hotel search with location, dates, and filters
- Design the booking flow so two users cannot book the same room
- Design a pricing service where prices move with demand and currency
- Design a notification service for reservations
- Design a review system

## What interviewers probe

- Consistency boundaries: strong for bookings and payments, eventual for search and reviews
- Estimates spoken out loud: queries per second and storage size
- The stale-search trade-off, paired with a live availability check and re-verification at checkout
- Degradation plans when pricing is slow or a region fails, plus write-path skew on a few popular properties

## Prepare

- Patterns to review: [consistency models](../patterns/consistency-models.md), [distributed transactions](../patterns/distributed-transactions.md), [idempotency](../patterns/idempotency.md), [caching](../patterns/caching.md), [replication](../patterns/replication.md)
- Practice questions: [Design hotel reservation](../questions/design-hotel-reservation.md), [Design ticketmaster](../questions/design-ticketmaster.md), [Design payment system](../questions/design-payment-system.md), [Design airbnb](../questions/design-airbnb.md)
- Full company guide: [Booking.com system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-booking-com-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
