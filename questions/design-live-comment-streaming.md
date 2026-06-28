# Design a live comment streaming service (Twitch chat)

> Broadcast a high-volume stream of live comments to many concurrent viewers in real time.

## Requirements

- Viewers post comments on a live stream.
- All viewers see comments in near real time.
- Handle very popular streams with huge concurrent audiences.
- Tolerate dropping some comments under extreme load.

## Key ideas

- Real-time fan-out: a comment must reach thousands or millions of connected viewers, pushed over persistent connections through a layer of broadcast servers.
- Scale fan-out by grouping viewers of a stream across many connection servers; a comment is published once and fanned out to all of them.
- Under extreme load, sampling or rate-limiting comments is acceptable, since not every viewer needs every message.
- This is a fan-out heavy variant of chat (see [Discord](design-discord.md)).

## Go deeper

- Quick, focused prep: [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)