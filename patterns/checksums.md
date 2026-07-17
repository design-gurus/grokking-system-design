# Checksums

> A small fingerprint computed from data, checked after transfer or storage to detect corruption.

## What it is

Disks silently flip bits, networks drop and mangle packets, and memory fails. A checksum is a compact value (CRC32, MD5, SHA-256) computed from a block of data. Recompute it later: if it does not match, the data changed. It converts silent corruption, the worst kind of failure, into a detectable and therefore fixable one.

## How it works

```
Writer:  data --> checksum(data) = c --> store/send (data, c)
Reader:  receive (data, c) --> checksum(data) == c ?
            yes: use it
            no:  discard, re-fetch from another replica or re-request
```

The crucial pairing: detection plus **redundancy** equals repair. A checksum alone tells you the data is bad; a replica or an erasure-coded copy lets you fix it. Storage systems (GFS, HDFS, S3) checksum every block on write and verify on every read, plus background "scrubbing" passes that re-verify cold data before all copies of it rot.

## Where it is used

- Storage: per-block checksums in HDFS, GFS, ZFS; verify on read, repair from a healthy replica.
- Network transfer: verifying file uploads and downloads end to end (TCP's checksum is weak; applications add their own).
- Content addressing: when the checksum of the content is also its identifier (Git objects, S3 ETags, Docker layers), integrity checking and deduplication come for free.
- Replica comparison: Merkle trees (trees of checksums) let two replicas find which ranges differ without shipping the data, used in Cassandra and Dynamo anti-entropy.

## Trade-offs

| Pro | Con |
|-----|-----|
| Turns silent corruption into detected errors | CPU cost on every read and write path |
| Cheap: a few bytes per block | Detects but cannot repair without redundancy |
| Enables dedup and content addressing | Weak checksums (CRC) can collide; pick strength for the threat |

## How to talk about it in an interview

Checksums come up in file storage, upload, and data pipeline designs. One strong sentence: "every block gets a checksum, verified on read and by periodic scrubbing, and a failed check triggers repair from another replica." Mentioning Merkle trees for efficient replica sync is a bonus in senior interviews.

## Go deeper

- Related deep dives: [GFS](../deep-dives/gfs-distributed-file-system.md), [HDFS](../deep-dives/hdfs-file-storage.md)
- Every pattern, in depth: [System Design Patterns](https://www.designgurus.io/course/system-design-patterns)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)