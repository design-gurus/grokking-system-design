# Design TinyURL

> A URL shortening service that turns a long URL into a short, unique alias and redirects users from the alias to the original.

## 1. Requirements

**Functional**
- Given a long URL, return a short URL.
- Given a short URL, redirect to the original long URL.
- Optional: custom aliases, expiration dates, basic analytics.

**Non-functional**
- High availability (redirects must almost never fail).
- Low latency redirects.
- Read-heavy: redirects vastly outnumber creations (a common assumption is 100 reads per write).

## 2. Estimation

Assume 100 million new URLs per month.
- Writes: roughly 40 per second on average.
- Reads: at 100 to 1, roughly 4,000 per second.
- Storage: 100 million per month times 12 months times 5 years is 6 billion objects. At about 500 bytes each, that is around 3 TB over 5 years.

See the [estimation cheat sheet](../cheat-sheets/estimation.md) for the numbers behind this.

## 3. API

- `POST /urls` with `{ longUrl, customAlias?, expiry? }` returns `{ shortUrl }`.
- `GET /{shortCode}` returns an HTTP 301 or 302 redirect to the long URL.

## 4. Data model

A single mapping is enough:

```
short_code (PK)  |  long_url  |  created_at  |  expiry  |  owner_id
```

Access pattern is a simple key lookup by `short_code`, so a key-value store or an indexed relational table both work well.

## 5. Generating the short code

Two common approaches:

| Approach | How | Trade-off |
|----------|-----|-----------|
| Hash the URL (for example base62 of a hash) | Take the first N characters of a hash | Simple, but collisions must be handled |
| Counter plus base62 encoding | A global counter, encoded to base62 | No collisions, but needs a distributed counter (for example a key generation service or ranges handed to each server) |

A pre-generated key service (a pool of unused keys handed out in batches) avoids collision checks on the hot path.

## 6. High-level design

```
[client] --> [load balancer] --> [app servers] --> [key-value store]
                                       |
                                    [cache]  (hot short codes)
```

- Redirects read from a cache first (short codes are very read-heavy and cache well). See [caching](../patterns/caching.md).
- Creations write to the store and assign a code from the key service.

## 7. Bottlenecks and trade-offs

- Read scaling: cache hot codes and add read replicas. See [replication](../patterns/replication.md).
- Code generation must avoid collisions and a single point of failure: use a key range service or [consistent hashing](../patterns/consistent-hashing.md) for distribution.
- 301 vs 302: 301 (permanent) is cacheable by browsers and reduces load but hides analytics; 302 (temporary) preserves analytics at the cost of more traffic.

## Go deeper

- Read more (free): [How to Design a URL Shortener](https://www.designgurus.io/blog/url-shortening)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)