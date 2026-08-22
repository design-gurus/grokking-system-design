# Block (Square): system design interview

> How Block (Square) actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Block (Square) runs it.** Every question is a money movement question, drawn from Square merchant payments, Cash App transfers, and Afterpay installments. Mid-level and senior candidates get one design round inside the virtual onsite, and correctness carries more weight than in most design interviews because the data is money. Interviewers reward fintech specifics: idempotency keys, card network behavior, append-only records, and at least one trade-off argued in both directions with real numbers attached.

## Signature questions

- Design a peer-to-peer transfer system that feels instant to users
- Design the pipeline from a card payment at a Square reader to the merchant's balance
- Design a fraud detection service that flags suspicious transactions in near real time
- Design the ledger that tracks every balance change
- Design a reconciliation job that compares internal records against bank records

## What interviewers probe

- A unique key on every payment request, and duplicate requests rejected rather than charged again
- Saying which parts of the design need strong consistency, since balances cannot serve stale reads
- Append-only history for auditability, with editing or deleting records treated as a defect
- Handling external card networks and banks that time out: retries, pending states, a queue for stuck transactions, and what the user sees while waiting

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [distributed transactions](../patterns/distributed-transactions.md), [consistency models](../patterns/consistency-models.md), [circuit breaker](../patterns/circuit-breaker.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design api gateway](../questions/design-api-gateway.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [Block (Square) system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-block-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
