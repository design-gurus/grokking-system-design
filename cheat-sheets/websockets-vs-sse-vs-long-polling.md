# WebSockets vs SSE vs long polling

How to choose a real-time delivery mechanism, and how to justify it in an interview. They are not three qualities of the same thing: long polling simulates push with ordinary requests, Server-Sent Events stream one way over plain HTTP, and WebSockets replace HTTP with a two-way channel. Start from the direction and frequency of messages. (The [pattern page](../patterns/long-polling-websockets-sse.md) explains how each works; this sheet is the decision.)

## Quick comparison

| Dimension | Long polling | SSE | WebSockets |
|-----------|--------------|-----|------------|
| Direction | Server to client, simulated | Server to client stream | Both directions |
| Transport | Repeated HTTP requests, each held until data | One long-lived HTTP response | Own protocol, after an HTTP upgrade handshake |
| Message format | Anything HTTP can carry | UTF-8 text events only | Text and binary frames |
| Reconnection | Built into the request loop | Automatic, resumes via Last-Event-ID | Yours to build, including resume |
| Strict proxies and firewalls | Works everywhere | Good (it is plain HTTP) | Occasionally blocked; use wss and a fallback |
| Cost per message | A full HTTP request | Cheap once connected | Cheapest once connected |
| Browser API | fetch / XHR | EventSource | WebSocket |
| Classic gotcha | Latency gap and duplicate handling between polls | Six-connection limit per domain on HTTP/1.1 (HTTP/2 fixes it) | Load balancer idle timeouts kill quiet connections; heartbeats are on you |

## The one-question shortcut

Ask: does the client send messages over the same channel, at high frequency?

- Yes → WebSockets (chat, multiplayer games, collaborative cursors, trading).
- No, data only flows down → SSE (feeds, notifications, tickers, progress, LLM token streams).
- Updates are rare, or the network path is hostile → long polling still works everywhere.

## How to choose

1. Notification stream, live score, news feed, progress bar → SSE. One direction, plain HTTP, automatic reconnection with resume built in.
2. Streaming LLM tokens → SSE. This is how ChatGPT and the Claude API deliver output: the client sends one request and reads a stream.
3. Chat, multiplayer, collaborative editing → WebSockets. The client talks constantly, and a request per message would drown you.
4. A dashboard that refreshes every 30 seconds → plain polling. Do not pay for a persistent connection to move slow-changing data.
5. The fallback path → long polling. When a corporate proxy kills streams, it is what still works.

## What interviewers probe

- The fan-out path: an event is produced on one server, but the user's connection lives on another. A pub/sub layer ([message queues](../patterns/message-queues.md)) routes events to whichever gateway node holds each connection.
- Connection state at scale: a node holds tens of thousands of open connections, so connection-aware [load balancing](../patterns/load-balancing.md) and sticky routing replace plain round robin.
- Reconnect storms: a deploy disconnects everyone at once, and they all come back at once. Jittered backoff on the client, [rate limiting](../patterns/rate-limiting.md) at the edge.
- Missed messages: SSE gives you Last-Event-ID; over WebSockets, resume cursors are your job. Expect "the connection dropped for ten seconds: what did the user miss?"
- Dead connections: an idle connection and a dead one look identical without [heartbeats](../patterns/heartbeats.md), and infrastructure silently reaps quiet connections.

## How to talk about it in an interview

Do not say "I will use WebSockets because it is real-time". Say "notifications only flow from server to client, so SSE: plain HTTP, automatic reconnection, nothing bidirectional to babysit. The collaborative editor is different: clients send operations constantly, so that surface gets a WebSocket, and I will pay for the connection gateway it needs." Defaulting to WebSockets for one-way data is a classic junior tell; choosing SSE when the flow is one-way is a senior signal.

## Go deeper

- How each mechanism works: [long polling, WebSockets, and SSE](../patterns/long-polling-websockets-sse.md)
- Questions that lean on this choice: [design WhatsApp](../questions/design-whatsapp.md), [design a live comment stream](../questions/design-live-comment-streaming.md)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=cheat-sheets-websockets-vs-sse-vs-long-polling)
