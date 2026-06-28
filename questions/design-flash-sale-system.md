# Design a flash sale system

> Sell a limited quantity of items to a massive burst of concurrent buyers, without overselling.

## 1. Requirements

**Functional**
- Sell a fixed inventory (for example 10,000 units).
- Accept orders during a short, intense window.
- Never sell more than the available stock.

**Non-functional**
- Handle an enormous traffic spike.
- No overselling (strong consistency on inventory).
- Be fair and responsive under load.

## 2. The two hard problems

- Preventing oversell: the inventory decrement must be atomic, so two buyers cannot both claim the last unit. Use an atomic operation (for example a conditional decrement in a fast store) or reserve-then-confirm.
- Surviving the spike: far more requests arrive than there is stock, so shed and smooth load early with caching, rate limiting, and a queue, rather than letting everything hit the database.

## 3. Deep dive

- Inventory as a counter: hold the count in a fast in-memory store (for example Redis) and decrement atomically; only requests that successfully decrement proceed to checkout.
- Admission control: a queue or token system admits a controlled number of buyers into checkout, so the backend sees a steady rate instead of the full spike.
- Reservation: reserve a unit on add-to-cart with a short timeout, and release it if the buyer does not complete in time.
- Idempotency: a buyer retrying must not consume two units.

## 4. Trade-offs

- Consistency over availability for inventory: it is better to reject some buyers than to oversell.
- User experience: a queue with a clear "you are in line" state beats errors or overselling.

## Go deeper

- For the full worked solution: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)