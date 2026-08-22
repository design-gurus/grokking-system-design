# Boston Dynamics: system design interview

> How Boston Dynamics actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Boston Dynamics runs it.** The clients in your diagram are robots, and a wrong answer can move a heavy machine near a person, so safety is treated as a requirement rather than a feature. Candidates report robotics-flavored sessions covering on-robot software architecture and fleet-level systems, with the Orbit fleet product giving the cloud-side questions a natural anchor. Interviewers change one assumption and watch you adapt: three reported probes are clock drift between robots, a perception model that degrades after a camera change, and how safety margins are enforced in motion planning.

## Signature questions

- Design the cloud side for a fleet of inspection robots across customer sites
- Design ingestion, storage, and review tools for heavy robot sensor data and video
- Design the on-robot split of perception, planning, and control
- Design event ordering when robot clocks drift

## What interviewers probe

- Latency, bandwidth, and reliability assumptions stated early, with numbers
- A clean split between what must run on the robot and what can run in the cloud
- Degraded modes: what the robot does when the network, a sensor, or the cloud fails
- Depth in robotics fundamentals over breadth of web components

## Prepare

- Patterns to review: [logical clocks](../patterns/logical-clocks.md), [message queues](../patterns/message-queues.md), [idempotency](../patterns/idempotency.md), [heartbeats](../patterns/heartbeats.md), [backpressure](../patterns/backpressure.md)
- Practice questions: [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design amazon s3](../questions/design-amazon-s3.md)
- Full company guide: [Boston Dynamics system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-boston-dynamics-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
