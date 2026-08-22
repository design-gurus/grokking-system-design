# Temporal: system design interview

> How Temporal actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Temporal runs it.** Name the guarantees before drawing any component: at least once delivery, idempotency, leases, and event history are used precisely here, and interviewers notice when they are not. Prompts cover durable job schedulers, distributed task queues, retry systems, and workflow orchestration for payments or orders, all versions of the company's own durable execution problem. Candidates also report concurrency and delivery-guarantee questions in the coding rounds, so the same themes repeat across the loop.

## Signature questions

- Design a durable job scheduler for millions of future jobs
- Design a distributed task queue with worker leases
- Design a retry system with idempotency keys and backoff
- Design workflow orchestration for payments or order processing

## What interviewers probe

- Whether guarantees are stated before components appear
- Failure-first design: crashed workers, duplicate messages, slow databases
- Saying plainly that delivery is at least once and the effect becomes exactly once through idempotency
- Naming the shard key out loud, with what it makes cheap and what it makes expensive

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [message queues](../patterns/message-queues.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md), [sharding partitioning](../patterns/sharding-partitioning.md), [distributed locking](../patterns/distributed-locking.md)
- Practice questions: [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design distributed message queue](../questions/design-distributed-message-queue.md), [Design payment system](../questions/design-payment-system.md), [Design reminder alert system](../questions/design-reminder-alert-system.md)
- Full company guide: [Temporal system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-temporal-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
