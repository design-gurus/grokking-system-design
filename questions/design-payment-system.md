# Design a payment system

> Process payments reliably, without double-charging, with an accurate record of every transaction.

## 1. Requirements

**Functional**
- Charge a customer and pay out to a merchant.
- Integrate with external payment providers.
- Track the state of every transaction.

**Non-functional**
- Correctness above all (no lost or double payments).
- Strong consistency for money.
- Auditable and reconcilable.

## 2. The hard parts

- Idempotency: network retries must not charge twice. Every payment request carries an idempotency key, and the system records the result so a repeat returns the same outcome instead of charging again.
- Exactly-once effect: achieved with idempotency plus a durable record of each step, not by hoping a call happens once.
- Ledger: record money movements as immutable, double-entry entries (every debit has a matching credit), so balances are always reconstructable.

## 3. Deep dive

- State machine: a payment moves through states (initiated, authorized, captured, settled, failed, refunded) persisted at each step so it can resume after a crash.
- Async with reconciliation: external providers are slow and can fail; process asynchronously and reconcile against provider records to catch mismatches.
- Consistency: use strong consistency for the ledger; do not trade it away for money.

## 4. Trade-offs

- Latency vs safety: extra durability and confirmation steps cost time, but correctness wins for payments.
- At-least-once delivery plus idempotency gives an exactly-once effect without exactly-once messaging.

## Go deeper

- For the full worked solution: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)