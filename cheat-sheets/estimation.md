# Back-of-the-envelope estimation

The numbers worth memorizing so you can size a system quickly and credibly.

## Latency numbers every engineer should know (approximate)

| Operation | Time |
|-----------|------|
| L1 cache reference | ~1 ns |
| Main memory reference | ~100 ns |
| Read 1 MB sequentially from memory | ~10 microseconds |
| SSD random read | ~100 microseconds |
| Round trip within a data center | ~500 microseconds |
| Read 1 MB sequentially from SSD | ~1 ms |
| Disk seek (spinning) | ~10 ms |
| Round trip between continents | ~150 ms |

Takeaway: memory is roughly 100 times faster than SSD, which is far faster than a disk seek, which is far faster than a cross-continent network call. [Cache](../patterns/caching.md) accordingly. For the full ladder on one log scale, with the design rules that fall out of it, see [latency numbers, visualized](latency-numbers.md).

## Powers of two (for storage)

| Power | Approx value | Name |
|-------|--------------|------|
| 10 | 1 thousand | 1 KB |
| 20 | 1 million | 1 MB |
| 30 | 1 billion | 1 GB |
| 40 | 1 trillion | 1 TB |
| 50 | 1 quadrillion | 1 PB |

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

More estimation practice in the [course](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=cheat-sheets-estimation).