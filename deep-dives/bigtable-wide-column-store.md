# BigTable: a wide-column store

> Google's distributed storage for structured data: a sparse, sorted, multi-dimensional map that scales to petabytes.

## What it is

BigTable is a wide-column store that holds a sparse, distributed, sorted map indexed by row key, column key, and timestamp. It backs many Google products and inspired HBase and Cassandra's data model.

## The problem it solves

Storing very large, semi-structured datasets (web pages, analytics) with fast lookups by key and efficient range scans, on commodity hardware.

## Key design ideas

| Idea | How it works |
|------|--------------|
| Data model | Rows sorted by key, grouped into column families; cells are versioned by timestamp |
| Tablets | A table is split by row range into tablets, each served by a tablet server |
| Built on GFS | SSTable files live in [GFS](gfs-distributed-file-system.md) for durable, replicated storage |
| Coordination | [Chubby](chubby-distributed-locking.md) elects the master and tracks tablet servers |

## Notable techniques

- Rows are sorted by key, so related data is co-located and range scans are efficient. Choosing the row key well is the main design lever.
- A single master assigns tablets and handles metadata, but is not on the data read path, so it is not a throughput bottleneck.
- SSTables plus an in-memory memtable (an LSM approach) give fast writes and efficient reads.

## Trade-offs

Excellent for key and range access at massive scale, but it is not a relational database: no joins, no multi-row transactions in the classic design.

## Go deeper

- For the full deep dive: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)