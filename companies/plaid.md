# Plaid: system design interview

> How Plaid actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Plaid runs it.** Every question starts from one hard fact: thousands of bank APIs fail, return partial pages, or send the same record twice, and the system must stay correct anyway. The round sits inside the virtual onsite and covers transaction sync across banks, reliable webhook delivery to customer apps, and retries that cannot create duplicate transactions. Candidates report that the failure-scenario discussion, not the box diagram, separates strong answers from average ones.

## Signature questions

- Design a bank transaction sync system across thousands of bank APIs
- Design reliable webhook delivery to customer apps
- Design retries for failed bank calls without creating duplicate transactions
- Design a pipeline that cleans and categorizes transactions at volume

## What interviewers probe

- Failure thinking first: what happens when a bank errors halfway through a page of results, or a webhook receiver is down for an hour
- Named mechanisms rather than intentions: idempotency keys, backoff, dead-letter queues, reconciliation
- Simple volume math said aloud (accounts, syncs per day, storage) to justify the queue, worker pool, and storage layout
- Whether you raise background reconciliation without being asked

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [message queues](../patterns/message-queues.md), [rate limiting](../patterns/rate-limiting.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md), [circuit breaker](../patterns/circuit-breaker.md)
- Practice questions: [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design notification system](../questions/design-notification-system.md), [Design payment system](../questions/design-payment-system.md)
- Full company guide: [Plaid system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-plaid-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
