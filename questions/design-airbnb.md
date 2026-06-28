# Design Airbnb

> A marketplace to search listings by location and dates, view availability, and book without double-booking.

## Requirements

- Search listings by location, dates, and filters.
- Show accurate availability.
- Book a listing without double-booking.
- Handle host and guest data.

## Key ideas

- Search: geospatial search by location plus date and attribute filters; a geo index (geohash or quadtree, see [Uber](design-uber.md)) narrows by area, then filters apply.
- Availability and booking: preventing double-booking is the core consistency problem. Reserve the dates atomically at booking time, similar to inventory in a [flash sale](design-flash-sale-system.md).
- Reservations: a hold during checkout with a timeout, confirmed on payment.
- Read-heavy search vs consistency-critical booking: separate those paths.

## Go deeper

- Quick, focused prep: [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)