# Design Uber

> A ride-hailing service that matches riders with nearby drivers in real time and tracks the trip.

## 1. Requirements

**Functional**
- Drivers publish their location continuously.
- A rider requests a ride and is matched with a nearby driver.
- Both sides see live location during the trip.

**Non-functional**
- Low latency for matching and location updates.
- High availability.
- Handles dense, hot areas (city centers at rush hour).

## 2. Estimation

Assume millions of active drivers sending location updates every few seconds. That is a very high write rate of location pings, which dominates the design. Matching must be fast and local to a geographic area.

See the [estimation cheat sheet](../cheat-sheets/estimation.md).

## 3. API

- `POST /drivers/location` with driver id and coordinates (very frequent).
- `POST /rides` to request a ride from a pickup location.
- `GET /rides/{id}/location` for live trip tracking.

## 4. Geo-indexing: the key decision

To find nearby drivers quickly, you need a spatial index, not a full scan:

| Technique | Idea |
|-----------|------|
| Geohash | Encode lat/long into a short string; nearby points share a prefix |
| Quadtree | Recursively divide space into quadrants; dense areas split deeper |
| S2 cells | Map the sphere to cells; good for range and neighbor queries |

Drivers are bucketed into cells. A ride request looks up the rider's cell and its neighbors to find candidate drivers.

## 5. High-level design

```mermaid
flowchart LR
    Driver[Driver app] --> Loc[Location Service]
    Loc --> Geo[(In-memory Geo Index)]
    Rider[Rider app] --> Match[Matching Service]
    Match --> Geo
    Match --> Trip[Trip Service]
    Trip --> DB[(Data Store)]
```

- Location updates flow through a stream or queue (see [message queues](../patterns/message-queues.md)) into an in-memory geo index that is frequently updated.
- Matching reads the index for the rider's area and applies business rules (distance, rating, car type).

## 6. Deep dive

- Hot areas: a single cell in a busy downtown can be overloaded, so cells must be sized or split to balance load (a quadtree splits dense areas deeper).
- Consistency: driver locations are best-effort and eventually consistent; the latest ping wins.
- Trip state: the active trip needs stronger consistency than location pings.

## 7. Bottlenecks and trade-offs

- The write volume of location pings; absorb it with a stream and in-memory index rather than a database write per ping.
- Geo hotspots; handle with adaptive cell sizing.
- Matching latency vs match quality.

## Go deeper

- Full worked solution: the lesson [Designing Uber backend](https://www.designgurus.io/course-play/grokking-the-system-design-interview/doc/designing-uber-backend?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-uber) in [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-uber).
- A second, condensed walkthrough: the lesson [Design Uber/Lyft](https://www.designgurus.io/course-play/system-design-interview-crash-course/doc/design-uberlyft?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-uber) in [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-uber).
- The same system as microservices: the lesson [Case Study: A Ride-Hailing Platform](https://www.designgurus.io/course-play/grokking-microservices-for-system-design-interviews/doc/case-study-a-ridehailing-platform?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-uber) in [Grokking Microservices for System Design Interviews](https://www.designgurus.io/course/grokking-microservices-for-system-design-interviews?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-uber).
- The Redis design: the lesson [Design Uber Driver Matching](https://www.designgurus.io/course-play/grokking-redis/doc/85-design-ubers-driver-matching?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-uber) in [Grokking Redis](https://www.designgurus.io/course/grokking-redis?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-uber).
- The mobile client design: the lesson [Ride Hailing](https://www.designgurus.io/course-play/grokking-modern-mobile-system-design-interview/doc/ride-hailing?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-uber) in [Grokking Modern Mobile System Design Interview](https://www.designgurus.io/course/grokking-modern-mobile-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-uber).
- For harder problems like this: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-uber)
