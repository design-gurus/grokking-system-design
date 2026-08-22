# Zoom: system design interview

> How Zoom actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Zoom runs it.** Two formats share the same 60 minute slot: a high-level architecture question, or a low-level one about the classes and API contracts inside a single service. Mid-level candidates may get either, while senior candidates should expect the high-level form with deeper follow-up questions. A live latency budget of roughly 200 milliseconds governs the whole answer, so transport and server model choices (WebRTC over UDP, an SFU against an MCU) are where answers separate.

## Signature questions

- Design a video conferencing service
- Design a chat system for millions of users
- Design a notification service with retries and rate limits
- Scale an existing service to ten times its load without downtime

## What interviewers probe

- Requirements clarified, including meeting size, screen sharing, and recording, before any boxes are drawn
- Latency respected in every choice, with a reason given for the transport
- Trade-offs named without being asked, such as SFU forwarding against MCU mixing
- Regional media servers with nearest-server routing instead of one large server

## Prepare

- Patterns to review: [long polling websockets sse](../patterns/long-polling-websockets-sse.md), [load balancing](../patterns/load-balancing.md), [cdn](../patterns/cdn.md), [message queues](../patterns/message-queues.md), [rate limiting](../patterns/rate-limiting.md)
- Practice questions: [Design zoom](../questions/design-zoom.md), [Design whatsapp](../questions/design-whatsapp.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [Zoom system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-zoom-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
