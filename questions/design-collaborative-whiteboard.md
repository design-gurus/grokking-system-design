# Design a collaborative whiteboard (Miro)

> A shared canvas where many users draw and edit shapes together in real time.

## Requirements

- Multiple users edit the same board at once and see each other's changes live.
- Persist the board and support reconnection.
- Show presence and cursors.
- Stay responsive with many concurrent editors.

## Key ideas

- Real-time sync uses persistent connections; each edit (add, move, delete a shape) is broadcast to other connected clients on the same board.
- Conflict handling: concurrent edits to the same object need a resolution strategy (last-write-wins per object, or operational transforms or CRDTs for finer merging, like [Google Docs](design-google-docs.md)).
- State: keep the live board in memory on a board server, and persist a snapshot plus an operation log for recovery.
- Partition by board so each board's editors connect to the same server.

## Go deeper

- Quick, focused prep: [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)