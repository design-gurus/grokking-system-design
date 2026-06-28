# Design an API gateway

> A single entry point in front of many backend services that handles routing, auth, and cross-cutting concerns.

## Requirements

- Route incoming requests to the right backend service.
- Handle authentication, rate limiting, and TLS termination in one place.
- Be highly available and low latency.
- Support many services and high request volume.

## Key ideas

- The gateway routes by path or host to backend services, so clients see one endpoint instead of many.
- Cross-cutting concerns live here: authentication and authorization, [rate limiting](../patterns/rate-limiting.md), TLS termination, request and response transformation, and logging.
- It must not become a single point of failure: run it behind a [load balancer](../patterns/load-balancing.md) as a redundant, stateless fleet.
- Caching and circuit breaking protect slow or failing backends.

## Go deeper

- Read more (free): [Load Balancer vs Reverse Proxy vs API Gateway](https://www.designgurus.io/blog/load-balancer-reverse-proxy-api-gateway)
- Quick, focused prep: [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)