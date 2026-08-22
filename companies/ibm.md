# IBM: system design interview

> How IBM actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How IBM runs it.** Three qualities decide this 45 to 60 minute round: scalability, reliability, and maintainability, and the last one carries unusual weight because the designs are expected to run for years inside banks and governments. The question is usually broad and unrelated to the team you applied to, since interviewers want general architecture skill rather than product knowledge. Plain explanation is graded on purpose, because many engineers here sit with clients, so a clever design that is hard to operate or hard to describe scores badly.

## Signature questions

- Design a log processing system for a large company
- Design a URL shortener
- Design a notification service
- Design a pipeline that collects, stores, and processes large volumes of data
- Design an integration that connects older on-premise software to cloud services without downtime

## What interviewers probe

- A clear path from requirements to a finished design, spoken the whole way through
- Honest trade-offs, such as cost against speed, named for each choice
- Failure cases and security handled rather than assumed away
- Language simple enough that a non-expert could follow the design

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [load balancing](../patterns/load-balancing.md), [caching](../patterns/caching.md), [replication](../patterns/replication.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md)
- Practice questions: [Design tinyurl](../questions/design-tinyurl.md), [Design notification system](../questions/design-notification-system.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md)
- Full company guide: [IBM system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-ibm-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
