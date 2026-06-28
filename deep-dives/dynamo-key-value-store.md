# Dynamo: a distributed key-value store

> Amazon's design for a highly available key-value store that stays writable even during failures and partitions.

## What it is

Dynamo is a key-value store that prioritizes availability over strong consistency. It is the design that popularized always-writable, eventually consistent storage, and it influenced Cassandra, Riak, and DynamoDB.

## The problem it solves

For a shopping cart, being unable to write is worse than briefly showing stale data. Dynamo targets "always writable": every request should succeed, even during node failures or network partitions, accepting that replicas reconcile afterward.

## Key design ideas

| Idea | How it works |
|------|--------------|
| Partitioning | [Consistent hashing](../patterns/consistent-hashing.md) spreads keys across nodes with minimal reshuffling |
| Replication | Each key is replicated to N nodes around the ring |
| Tunable consistency | Quorums: a read needs R replicas, a write needs W; choosing R + W greater than N gives stronger guarantees |
| Conflict resolution | Vector clocks track versions; conflicting versions are reconciled (often by the application) |

## Notable techniques

- Hinted handoff: if a target node is down, another node temporarily holds the write and forwards it later, keeping the system writable.
- Read repair and anti-entropy (Merkle trees) heal divergent replicas over time.
- Gossip-based membership: nodes learn about each other without a central registry.

## Trade-offs

It gives up strong consistency for availability and partition tolerance (an AP system, see the [CAP theorem](../patterns/cap-theorem.md)). The application must tolerate and sometimes resolve conflicts.

## Go deeper

- For the full deep dive: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)