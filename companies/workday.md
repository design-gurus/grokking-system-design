# Workday: system design interview

> How Workday actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Workday runs it.** Enterprise systems of record for HR and financials: the signature concept is effective-dated temporal data (every change has validity ranges; the org chart is a time-travel query), with paycheck-grade correctness and enterprise seasonality (payroll runs, open enrollment).

## Signature questions

- Design a payroll run: deterministic calculation as a pure function of effective-dated inputs, retroactivity handled explicitly
- Design open enrollment: configuration-heavy, burst-loaded, never-lose-elections
- Design org-structure modeling with effective dating and hierarchical security

## What interviewers probe

- Effective-dated thinking: as-of queries and retroactive recomputation
- Configurability without chaos across differently configured customers
- People-data privacy raised unprompted

## Prepare

- Patterns to review: [consistency models](../patterns/consistency-models.md), [write ahead log](../patterns/write-ahead-log.md), [idempotency](../patterns/idempotency.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design google calendar](../questions/design-google-calendar.md)
- Full company guide: [Workday system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-workday-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
