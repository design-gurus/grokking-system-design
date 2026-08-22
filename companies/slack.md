# Slack: system design interview

> How Slack actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Slack runs it.** Most of the score sits in the connection layer: a pool of gateway servers holding WebSockets, with pub/sub behind them so each gateway receives only the channels its connected users belong to. The round runs about an hour, and candidates report one design interview for mid-level and sometimes two for senior, with the extra time spent on trade-offs and failure cases. Every question maps to a real problem in the product, including presence, duplicate-free notifications, and search restricted to each company's own data.

## Signature questions

- Design a team chat system with channels and message history
- Design presence showing which users are online right now
- Design push notifications to phones and desktops without duplicates
- Design search over billions of stored messages, scoped per company
- Design a rate limiter capping API calls per app per minute

## What interviewers probe

- Scope clarified before any parts are drawn: group channels, history, search, ordering
- Building blocks in the right place, with gateways, pub/sub, storage, and presence separated
- Trade-off reasoning with reasons attached, such as per-channel sequence numbers for ordering and client-side dedup by message ID
- Rough math on open connections, messages per second, storage, and fan-out cost for large channels

## Prepare

- Patterns to review: [long polling websockets sse](../patterns/long-polling-websockets-sse.md), [message queues](../patterns/message-queues.md), [sharding partitioning](../patterns/sharding-partitioning.md), [caching](../patterns/caching.md), [rate limiting](../patterns/rate-limiting.md)
- Practice questions: [Design whatsapp](../questions/design-whatsapp.md), [Design discord](../questions/design-discord.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [Slack system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-slack-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
