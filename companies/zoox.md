# Zoox: system design interview

> How Zoox actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Zoox runs it.** Designs are graded by what happens when a part fails with a rider inside a driverless vehicle, so the failure discussion decides the round. It is one 45 to 60 minute session in the onsite loop, and it often sets the offer level: mid-level and senior candidates get a full distributed systems discussion, while entry-level candidates may get object-oriented design instead. Interviewers push on real-time behavior, so name the delay budget, say what breaks it, and reason about worst-case delay rather than the average.

## Signature questions

- Design a fleet telemetry and monitoring pipeline for hundreds of vehicles
- Design ride requests, dispatch, and vehicle assignment for a robotaxi service
- Design a real-time vehicle health service with a tight delay budget
- Design a remote assistance system for a stuck vehicle
- Design a simulation results store

## What interviewers probe

- Requirements and numbers before boxes: delay budgets, message rates, and failure rules
- Worst-case delay versus average delay, because vehicle systems are judged on the worst case
- A stated failure story for every component, volunteered before the interviewer asks
- Raising safety yourself when a choice risks the rider, then choosing the careful side

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [backpressure](../patterns/backpressure.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md), [heartbeats](../patterns/heartbeats.md), [replication](../patterns/replication.md)
- Practice questions: [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design uber](../questions/design-uber.md), [Design distributed message queue](../questions/design-distributed-message-queue.md)
- Full company guide: [Zoox system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-zoox-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
