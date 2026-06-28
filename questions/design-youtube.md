# Design YouTube

> A video platform to upload, process, store, and stream videos to a global audience, with search and recommendations.

## Requirements

- Upload and process (transcode) videos.
- Stream smoothly with adaptive quality.
- Search, view counts, and recommendations.
- Read-heavy, global, huge storage and bandwidth.

## Key ideas

- Upload and transcoding run offline: split video into segments and encode multiple bitrates, then push to a [CDN](../patterns/cdn.md). This is the same pipeline as [Netflix](design-netflix.md).
- Playback uses adaptive bitrate streaming from the nearest edge.
- Metadata (titles, channels, view counts) lives in a separate service; view counts are a high-volume counter (see the [likes counter](design-youtube-likes-counter.md)).
- Storage: raw and encoded video in object storage fronted by the CDN.

## Go deeper

- Quick, focused prep: [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)