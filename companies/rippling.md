# Rippling: system design interview

> How Rippling actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Rippling runs it.** The compound-startup architecture: one employee graph powering payroll, IT, and finance, so prompts run on shared data models with many consumers, event cascades across products, and the offboarding guarantee (access revocation must complete, on time, provably).

## Signature questions

- Design the offboarding cascade: priority-tiered revocation, verified not just sent, with honest partial-failure states
- Design the employee graph: schema evolution with many product consumers
- Design app provisioning across hundreds of third-party SaaS APIs with drift detection

## What interviewers probe

- Shared-foundation discipline: blast radius reasoned for every schema change
- Cascade correctness: sagas, compensation, idempotent steps
- Integration realism: reconciliation as the truth mechanism

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [idempotency](../patterns/idempotency.md), [write ahead log](../patterns/write-ahead-log.md), [circuit breaker](../patterns/circuit-breaker.md)
- Practice questions: [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [Rippling system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-rippling-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
