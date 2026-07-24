# Back-of-the-envelope estimation

The numbers worth memorizing so you can size a system quickly and credibly.

## Latency numbers every engineer should know (approximate)

| Operation | Time |
|-----------|------|
| L1 cache reference | ~1 ns |
| Branch mispredict | ~3 ns |
| L2 cache reference | ~4 ns |
| Mutex lock/unlock | ~25 ns |
| Main memory reference | ~100 ns |
| Compress 1 KB | ~2 microseconds |
| Read 1 MB sequentially from memory | ~10 microseconds |
| Send 1 KB over a 1 Gbps network | ~10 microseconds |
| SSD random read | ~100 microseconds |
| Round trip within a data center | ~500 microseconds |
| Read 1 MB sequentially from SSD | ~1 ms |
| Disk seek (spinning) | ~10 ms |
| Read 1 MB sequentially from disk | ~20 ms |
| Round trip between continents | ~150 ms |

Takeaway: memory is roughly 100 times faster than SSD, which is far faster than a disk seek, which is far faster than a cross-continent network call. [Cache](../patterns/caching.md) accordingly, and keep the common path in the fast tiers.

## Powers of two (for storage)

| Power | Exact value | Approx | Name |
|-------|-------------|--------|------|
| 2^7 | 128 | — | — |
| 2^8 | 256 | — | — |
| 2^10 | 1,024 | 1 thousand | 1 KB |
| 2^16 | 65,536 | 65 thousand | 64 KB |
| 2^20 | 1,048,576 | 1 million | 1 MB |
| 2^30 | ~1.07 billion | 1 billion | 1 GB |
| 2^32 | ~4.29 billion | 4 billion | 4 GB (the IPv4 address space) |
| 2^40 | ~1.10 trillion | 1 trillion | 1 TB |
| 2^50 | ~1.13 quadrillion | 1 quadrillion | 1 PB |

Handy for sizing IDs and storage: 2^32 is ~4 billion (an `int` overflows here — use 64-bit IDs at scale), and 2^64 is ~1.8 × 10^19.

## Availability (the "nines")

| Availability | Downtime per year | Per day |
|--------------|-------------------|---------|
| 99% | 3.65 days | 14.4 min |
| 99.9% | 8.77 hours | 1.44 min |
| 99.99% | 52.6 min | 8.6 s |
| 99.999% | 5.26 min | 864 ms |

Each extra nine cuts downtime 10×. The full table plus how availability combines in sequence vs parallel is in [availability patterns](../fundamentals/availability-patterns.md).

## Time conversions

- 1 day is about 86,400 seconds (round to 100,000 for quick math).
- 1 month is about 2.5 million seconds.
- "X per day" divided by 100,000 gives roughly "X per second".

## A worked example

100 million writes per day:
- Per second: 100,000,000 / 100,000 is about 1,000 writes per second.
- At a 100 to 1 read-to-write ratio: about 100,000 reads per second.
- At 1 KB per record: 100 GB of new data per day, about 36 TB per year.

## How to use this in an interview

State your assumptions, round aggressively, and show the division (this is Step 2 of the [interview framework](interview-framework.md)). Interviewers care that the method is sound, not that the number is exact.

## Go deeper

More estimation practice in the [course](https://www.designgurus.io/course/grokking-the-system-design-interview).