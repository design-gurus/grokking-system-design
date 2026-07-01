# Design Netflix

> A video streaming service that ingests, encodes, and streams video to a global audience, with browse and recommendations.

## 1. Requirements

**Functional**
- Upload and ingest video (content side).
- Transcode video into multiple resolutions and bitrates.
- Stream video smoothly with adaptive quality.
- Browse, search, and get recommendations.

**Non-functional**
- Massive read and bandwidth scale.
- Minimal buffering and startup delay.
- Global reach.

## 2. Estimation

The dominant cost is bandwidth and storage of video, not request volume. A single title exists in many encodings and resolutions, multiplying storage. Delivery must happen close to users, so a [CDN](../patterns/cdn.md) is central.

See the [estimation cheat sheet](../cheat-sheets/estimation.md).

## 3. The two pipelines

- Ingest and encoding (write path, offline): uploaded video is split into segments and transcoded into many bitrate and resolution variants, then pushed to the CDN.
- Playback (read path, online): the client streams from the nearest CDN edge using adaptive bitrate streaming (HLS or DASH), switching quality based on network conditions.

```mermaid
flowchart LR
    Upload[Upload] --> TP[Transcoding Pipeline]
    TP --> OS[(Object Storage)]
    OS --> CDN[CDN Edges]
    CDN --> Player[Player]
```

## 4. Adaptive bitrate streaming

Video is stored as small segments at several quality levels. The player requests the next segment at the quality its current bandwidth can support, so playback adapts smoothly instead of buffering.

## 5. Deep dive

- CDN strategy: pre-position popular titles at the edge; the origin handles the long tail.
- Metadata and catalog: a separate service for titles, search, and user data.
- Recommendations: an offline pipeline computes suggestions; the serving layer reads them.
- Resume and watch history: per-user state, eventually consistent.

## 6. Bottlenecks and trade-offs

- Bandwidth and storage dominate; encoding variants and CDN placement are the levers.
- Encoding is expensive and offline; playback must be cheap and fast.
- Freshness of recommendations vs cost; precompute and serve.

## Go deeper

- Read more (free): [Designing a Scalable Video Streaming Platform (Netflix/YouTube)](https://www.designgurus.io/blog/design-video-streaming-platform)
- For harder problems like this: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)