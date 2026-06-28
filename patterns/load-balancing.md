# Load balancing

> Spread incoming traffic across multiple servers so no single one is overwhelmed, and so the system stays available when a server fails.

## What it is

A load balancer sits in front of a pool of servers and distributes requests among them. It improves scalability (add more servers behind it) and availability (route around unhealthy servers). It can operate at the transport layer (L4, by IP and port) or the application layer (L7, by HTTP attributes like path or headers).

## When to use it

- Any service that runs on more than one instance.
- When you need horizontal scaling and zero-downtime deploys.
- When you want health checks to remove failed instances automatically.

## Balancing algorithms

| Algorithm | How it works | Best for |
|-----------|--------------|----------|
| Round robin | Rotate through servers in order | Uniform servers and requests |
| Weighted round robin | Round robin with capacity weights | Mixed server sizes |
| Least connections | Send to the server with fewest active connections | Long-lived or uneven requests |
| Least response time | Favor the fastest-responding server | Latency-sensitive services |
| Hashing (for example by client IP) | Map a key to a server consistently | Sticky sessions, cache locality |

## L4 vs L7

- L4 (transport): fast, routes by IP and port, no visibility into the request content.
- L7 (application): can route by URL path, header, or cookie, enabling features like path-based routing and TLS termination, at a small latency cost.

## Avoiding a single point of failure

The load balancer itself must not be a single point of failure. Run it in a redundant pair (active-passive or active-active) and use DNS or a floating IP to fail over.

## Trade-offs

| Pro | Con |
|-----|-----|
| Horizontal scaling and high availability | Another component to operate and secure |
| Health checks remove bad instances | Can become a bottleneck if undersized |
| Enables zero-downtime deploys | Sticky sessions complicate scaling |

## How to talk about it in an interview

State where the load balancer sits, the algorithm and why, how health checks work, and how you make the load balancer itself redundant. Mention sticky sessions only if the app needs them, and prefer stateless services so you do not.

## Go deeper

- Read more (free): [Complete Load Balancer Guide](https://www.designgurus.io/blog/complete-load-balancing-guide)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)