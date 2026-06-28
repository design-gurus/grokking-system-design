# Design Discord

> A community chat platform with servers, channels, real-time messaging, presence, and voice.

## Requirements

- Servers (guilds) containing many channels.
- Real-time text messaging in channels, plus direct messages.
- Presence (who is online) and notifications.
- Large servers with many concurrent members.

## Key ideas

- Real-time delivery uses persistent connections (WebSocket) and a routing layer, like [WhatsApp](design-whatsapp.md), but fan-out is per channel rather than per direct conversation.
- Messages are stored per channel, partitioned by channel id, ordered by time.
- Fan-out: a message in a busy channel must reach many connected clients; push to the connection servers holding those members.
- Presence and large-server scale are the hard parts; shard members and gateway connections.

## Go deeper

- Quick, focused prep: [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)