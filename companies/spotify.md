# Spotify: system design interview

> How Spotify actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Spotify runs it.** Spotify-flavored prompts (shuffle, notifications, podcast search, playlist sync) at streaming scale, with a communication bar that exceeds the algorithmic one: a clean medium solution narrated well outperforms a hard one delivered messily.

## Signature questions

- Design the backend for shuffle or playlist sync across devices
- Design a podcast search engine
- Design real-time notifications for releases and social features

## What interviewers probe

- Read-heavy personalization with cache strategy
- Latency where the user is mid-listen
- Incident-style operational thinking (a case-study round probes triage directly)

## Prepare

- Patterns to review: [caching](../patterns/caching.md), [cdn](../patterns/cdn.md), [message queues](../patterns/message-queues.md), [database indexing](../patterns/database-indexing.md)
- Practice questions: [Design recommendation system](../questions/design-recommendation-system.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [Spotify system design interview](https://www.designgurus.io/answers/detail/what-are-the-top-system-design-interview-questions-for-spotify-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
