# Design a distributed job scheduler (like Cron)

> Run jobs at scheduled times or intervals across a fleet, reliably and exactly as intended.

## Requirements

- Schedule jobs to run at a specific time or on a recurring interval.
- Run them reliably across a fleet of workers.
- Avoid running the same job twice (or handle it safely).
- Scale to many jobs and survive worker failures.

## Key ideas

- Storage: persist jobs with their next run time, partitioned by time so the scheduler scans only the near-future window (related to the [reminder system](design-reminder-alert-system.md)).
- Dispatch: due jobs are placed on a [queue](../patterns/message-queues.md); workers pull and execute them.
- Exactly-once vs at-least-once: distributed scheduling usually guarantees at-least-once, so jobs should be idempotent, or use a lock (see [Chubby](../deep-dives/chubby-distributed-locking.md)) so only one worker runs a given job.
- Reliability: retries with backoff, and a dead letter path for jobs that keep failing.

## Go deeper

- Quick, focused prep: [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)