# CDN (content delivery network)

> A network of edge servers that cache content close to users, cutting latency and offloading your origin.

## What it is

A CDN is a globally distributed set of caching servers. When a user requests content, it is served from a nearby edge location instead of your origin server far away. This reduces latency, absorbs traffic spikes, and lowers load and bandwidth costs on the origin.

## What to put on a CDN

- Static assets: images, video, CSS, JavaScript, fonts, downloads.
- Cacheable API responses and HTML where appropriate.
- Increasingly, dynamic content via edge compute, though that is more advanced.

## How content gets there

- Pull (origin pull): the CDN fetches from your origin on the first request for a path, then caches it. Simple to operate.
- Push: you upload content to the CDN ahead of time. More control, more work, good for large or predictable assets.

## Cache control

You control freshness with HTTP headers (Cache-Control, ETag, TTLs). For updates, use cache invalidation or content versioning (for example a hash in the filename) so users get the new version without serving stale content.

## Trade-offs

| Pro | Con |
|-----|-----|
| Lower latency for global users | Cache invalidation and staleness to manage |
| Offloads traffic from the origin | Added cost and another system to configure |
| Absorbs spikes and some attacks | Not a fit for highly personalized, uncacheable content |

## How to talk about it in an interview

Say what you cache, how content reaches the edge (pull vs push), and how you handle updates (versioned URLs or invalidation). Pair it with [caching](caching.md) as the client-and-edge layer of your caching story.

## Go deeper

- Read more (free): [Content Delivery Networks (CDN) in System Design](https://www.designgurus.io/blog/content-delivery-network-cdn-system-design-basics)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)