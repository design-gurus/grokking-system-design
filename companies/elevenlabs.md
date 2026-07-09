# ElevenLabs: system design interview

> How ElevenLabs actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How ElevenLabs runs it.** The product decomposition round asks for the user experience and the system together, founder-style, for voice-product use cases. Underneath sits real-time audio physics: streaming synthesis where time-to-first-audio decides whether an agent feels conversational.

## Signature questions

- Design a customer-support voice agent: the STT-LLM-TTS chain inside a ~700ms first-audio budget, with interruption handling
- Design streaming text-to-speech serving with latency tiers and per-voice caching
- Design dubbing at scale: batch media pipelines with audio quality gates
- Design voice cloning infrastructure with consent verification and provenance as product

## What interviewers probe

- Latency arithmetic for conversation, with stages overlapped through streaming
- Product-system integration: UX moments driving system properties and vice versa
- Founder sequencing: the two-week slice that tests the core risk, named explicitly

## Prepare

- Patterns to review: [long polling websockets sse](../patterns/long-polling-websockets-sse.md), [message queues](../patterns/message-queues.md), [caching](../patterns/caching.md)
- Practice questions: [Design youtube](../questions/design-youtube.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [ElevenLabs system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-elevenlabs-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
