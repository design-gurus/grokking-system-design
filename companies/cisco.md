# Cisco: system design interview

> How Cisco actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Cisco runs it.** Scale is counted in devices rather than users, so a telemetry design serving fifty thousand routers is decided by write volume, not by read traffic. The network is treated as part of the problem: bandwidth limits, timeouts, retransmission, and the choice between TCP and UDP all come up, and candidates who treat the network as invisible get noticed. Estimates matter more than usual, because device counts and message rates set the architecture, and some Cisco software runs on hardware with small memory and CPU.

## Signature questions

- Design a device telemetry collection pipeline
- Design a service that configures and monitors thousands of network devices
- Design a backend service that keeps working when servers or links fail
- Design a messaging service
- Design a URL shortener

## What interviewers probe

- A clear order: requirements, estimates, architecture, then depth on one part
- Rough math on devices, messages per second, and retention before any deep dive
- Follow-up answers one layer deeper, such as collector behavior during a network partition
- Reasoning spoken while drawing, since silence or a copied design is the common failure

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md), [backpressure](../patterns/backpressure.md), [heartbeats](../patterns/heartbeats.md), [replication](../patterns/replication.md)
- Practice questions: [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design distributed message queue](../questions/design-distributed-message-queue.md), [Design tinyurl](../questions/design-tinyurl.md)
- Full company guide: [Cisco system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-cisco-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
