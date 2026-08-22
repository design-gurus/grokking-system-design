# Latency numbers: the one-page visual

Every latency number worth knowing, on one page. These numbers are why systems are designed the way they are: caching exists because of the first rows, CDNs exist because of the last one. Memorize the ladder, and half of system design becomes obvious.

## The ladder

The scale is logarithmic: **every full block is another 10x slower**. The bars would not fit on a linear scale, because the bottom row is a hundred million times the top row.

```
L1 cache reference             1 ns   █
Mutex lock / unlock           20 ns   ██▎
Main memory reference        100 ns   ███
Compress 1 KB                  2 µs   ████▎
Read 1 MB from memory         10 µs   █████
SSD random read              100 µs   ██████
Round trip inside a DC       500 µs   ██████▋
Read 1 MB from SSD             1 ms   ███████
HDD disk seek                 10 ms   ████████
Read 1 MB from HDD            20 ms   ████████▎
Coast-to-coast round trip     70 ms   ████████▊
Cross-continent round trip   150 ms   █████████▏
```

All numbers are approximate and rounded for recall. Interviewers want the right order of magnitude, not the datasheet.

## The gaps that matter

The absolute numbers matter less than the jumps between them:

| Gap | Ratio | What it means for design |
|-----|-------|--------------------------|
| Memory vs SSD random read | ~1,000x | Cache in memory before touching any disk ([caching](../patterns/caching.md)) |
| SSD vs HDD seek | ~100x | Random reads on spinning disks are a design smell |
| Sequential vs random | ~10 to 100x | Append, do not update in place ([write-ahead log](../patterns/write-ahead-log.md)) |
| Same data center vs cross-continent | ~300x | Geography is a product decision, not a tuning knob ([CDN](../patterns/cdn.md)) |
| One DC round trip vs one memory read | ~5,000x | Every network hop you avoid pays for a lot of local work |

## If a nanosecond were a second

Multiply everything by a billion, and the ladder becomes human-sized:

| Operation | Real time | Human scale |
|-----------|-----------|-------------|
| L1 cache reference | 1 ns | one second |
| Main memory reference | 100 ns | almost two minutes |
| Read 1 MB from memory | 10 µs | about three hours |
| SSD random read | 100 µs | a little over a day |
| Round trip inside a data center | 500 µs | almost six days |
| Read 1 MB from SSD | 1 ms | almost two weeks |
| HDD disk seek | 10 ms | almost four months |
| Cross-continent round trip | 150 ms | almost five years |

When your code makes a cross-continent call between two memory reads, it is pausing a two-minute task for five years.

## Round trips, not bandwidth

Most request latency is round trips, so count them:

- A TCP handshake costs one round trip before any data moves. TLS adds one to two more. Reuse connections; do not pay this per request.
- A 200 ms latency budget fits one cross-continent round trip, or about 400 round trips inside a data center. Sequential calls to five services in another region blow the budget on hops alone.
- Batch small requests and parallelize independent ones. Ten sequential in-DC calls cost 5 ms of pure network; the same ten in parallel cost 0.5 ms.

## The human thresholds

- Around 100 ms feels instant.
- Around 1 second, attention breaks and the interaction feels slow.
- These two numbers are the latency budget every user-facing design is solving for, and why p99 matters more than the average: the slowest experience is the one users remember.

## How to use this in an interview

Anchor your design choices to a number: "a feed read hits memory in microseconds, but assembling it from three services in another region costs 150 ms before any work happens, so the feed is precomputed and cached regionally." Capacity math and the worked example live in the [estimation sheet](estimation.md); this page is the latency half of that story.

## Go deeper

- [Back-of-the-envelope estimation](estimation.md): the capacity numbers and the method
- [Caching](../patterns/caching.md), [CDN](../patterns/cdn.md), and [replication](../patterns/replication.md): the three patterns these numbers justify
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)
