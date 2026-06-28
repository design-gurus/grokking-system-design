# Design Dropbox

> A cloud storage service that stores files and syncs them across a user's devices, with sharing.

## 1. Requirements

**Functional**
- Upload and download files.
- Sync changes across all of a user's devices.
- Share files and folders.

**Non-functional**
- Durability (never lose a file).
- Efficient sync (do not re-upload unchanged data).
- Support large files.

## 2. Estimation

Storage is the dominant cost. Files are large and many are duplicates across users, so deduplication and efficient transfer matter more than request rate.

See the [estimation cheat sheet](../cheat-sheets/estimation.md).

## 3. The key idea: chunking

Files are split into fixed-size chunks. Each chunk is identified by a hash of its content (content-addressable storage). Benefits:

- Sync only changed chunks, not the whole file.
- Deduplicate identical chunks across files and users.
- Resume interrupted uploads chunk by chunk.

```
[file] -> [split into chunks] -> [hash each chunk] -> upload only new chunks -> [object storage]
```

## 4. The two services

- Metadata service: tracks files, versions, and the ordered list of chunk hashes per file. This is the source of truth for "what the file looks like".
- Block (chunk) storage: the actual chunk bytes in object storage, keyed by content hash.

A sync client watches for local changes, computes chunk hashes, asks the metadata service what is new, and uploads only those chunks.

## 5. Deep dive

- Sync: clients poll or receive notifications of metadata changes, then fetch new chunks.
- Conflicts: two devices edit the same file; resolve with versioning and conflict copies rather than silent overwrites.
- Sharing: permissions live in the metadata service.
- Consistency: metadata needs stronger consistency than chunk storage.

## 6. Bottlenecks and trade-offs

- Storage cost; deduplication and compression help.
- Sync latency vs server load; notifications beat constant polling.
- Metadata is the hot, consistency-critical path; chunk storage is large but simpler.

## Go deeper

- Read more (free): [How to Design a Cloud Storage Service (Dropbox)](https://www.designgurus.io/blog/design-cloud-storage-service)
- For harder problems like this: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)