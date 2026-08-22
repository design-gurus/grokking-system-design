# Snap: system design interview

> How Snap actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Snap runs it.** Deletion is a first-class requirement here, so storage answers need a time to live and a delete path that survives a failed job. Mid-level and senior candidates get one dedicated design round inside the virtual onsite, drawn from Snap's own products: disappearing messages, Stories, media delivery, and AR lenses. Sharing runs over a friend graph rather than public followers, which keeps fan-out small and moves the pressure onto media upload, object storage, and CDN delivery instead.

## Signature questions

- Design disappearing messages
- Design Stories that expire after a fixed window
- Design media upload and delivery for photos and video
- Design push notifications for new messages
- Design delivery of augmented reality lens files to phones

## What interviewers probe

- A clear order: requirements, estimates, architecture, then depth, with real numbers such as storage per day at your assumed scale
- At least one trade-off argued in both directions, for example push against pull for notifications
- Deletion handled as core design, including what happens when a delete job fails and how retries stay safe
- Continuous narration, since silence is the main failure mode, and asking the interviewer questions counts as a strength

## Prepare

- Patterns to review: [cdn](../patterns/cdn.md), [caching](../patterns/caching.md), [message queues](../patterns/message-queues.md), [api gateway](../patterns/api-gateway.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design whatsapp](../questions/design-whatsapp.md), [Design instagram](../questions/design-instagram.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [Snap system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-snap-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
