# Twitch: system design interview

> How Twitch actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Twitch runs it.** Everything reduces to fan-out arithmetic said out loud: a million viewers times thousands of chat messages per second is billions of deliveries, and that number justifies every choice after it. Candidates report the round inside the final loop, mainly for senior roles, running 45 to 60 minutes on live video, chat, presence, and viewer counts. Load is spiky, so the round rewards graceful degradation: an approximate viewer count that stays up beats an exact one that falls over.

## Signature questions

- Design Twitch chat for a million concurrent viewers
- Design live video delivery from streamer to worldwide viewers
- Design viewer counts and presence at scale
- Design clips and highlights from live video
- Design go-live notifications to millions of followers

## What interviewers probe

- Scale arithmetic stated explicitly before the architecture, not after it
- Two-step fan-out through a per-stream channel to connection servers, with a registry mapping streams to servers
- Overload behavior: rate limits per sender, batching, and which messages you are willing to drop first
- Defense under pressure, since interviewers push one component until it breaks and watch you repair it; behavioral probes appear inside the round

## Prepare

- Patterns to review: [long polling websockets sse](../patterns/long-polling-websockets-sse.md), [backpressure](../patterns/backpressure.md), [load balancing](../patterns/load-balancing.md), [cdn](../patterns/cdn.md), [rate limiting](../patterns/rate-limiting.md)
- Practice questions: [Design live comment streaming](../questions/design-live-comment-streaming.md), [Design youtube](../questions/design-youtube.md), [Design notification system](../questions/design-notification-system.md), [Design discord](../questions/design-discord.md)
- Full company guide: [Twitch system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-twitch-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
