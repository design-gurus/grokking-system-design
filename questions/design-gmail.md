# Design Gmail

> An email service to send, receive, store, search, and organize mail at large scale.

## 1. Requirements

**Functional**
- Send and receive email.
- Store mail per user with labels or folders.
- Full-text search.
- Spam filtering.

**Non-functional**
- Durable storage (do not lose mail).
- Fast search.
- Read-heavy with large per-user storage.

## 2. Key components

- Mail storage: per-user mailboxes, partitioned by user id, with attachments in object storage.
- Sending and receiving: SMTP gateways feeding a [queue](../patterns/message-queues.md), so delivery and processing are async and retryable.
- Search: an inverted index per user maps terms to messages (see [database indexing](../patterns/database-indexing.md) for the idea).
- Spam filtering: a classification pipeline scores incoming mail.

## 3. Deep dive

- Storage scale: shard by user; a heavy user must not overload one node.
- Search index: built asynchronously as mail arrives; keep it close to the mailbox shard.
- Threading: group messages into conversations by subject and references.
- Attachments: store once in object storage, deduplicate identical attachments by content hash.

## 4. Trade-offs

- Index freshness vs cost: index asynchronously, so new mail is searchable within seconds.
- Strong durability for mail vs eventual consistency for secondary indexes.

## Go deeper

- For the full worked solution: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)