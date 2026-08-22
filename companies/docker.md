# Docker: system design interview

> How Docker actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Docker runs it.** Interviewers work on infrastructure daily, so vague storage math gets caught: being specific about layer sizes, bandwidth, and request rates matters more here than at most companies. Candidates report the round in senior processes, about an hour on video alongside a project review, with the company's own problems as prompts: registries, build systems, and container logging. Balanced coverage of numbers, trade-offs, failures, and communication scores better than being excellent in one area only.

## Signature questions

- Design a container registry
- Design a build service that runs untrusted jobs safely
- Design centralized logging for thousands of microservice containers
- Compare a monolith and microservices for a given product
- Design rate limiting and caching for a public API

## What interviewers probe

- Estimates of storage, bandwidth, and request rates offered without being asked
- Splitting strongly consistent metadata from cacheable blob storage, and saying why
- Failure handling for partial uploads and region loss
- Plain spoken structure, which counts at a remote-first company

## Prepare

- Patterns to review: [cdn](../patterns/cdn.md), [caching](../patterns/caching.md), [checksums](../patterns/checksums.md), [consistency models](../patterns/consistency-models.md), [rate limiting](../patterns/rate-limiting.md)
- Practice questions: [Design amazon s3](../questions/design-amazon-s3.md), [Design dropbox](../questions/design-dropbox.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design code deployment system](../questions/design-code-deployment-system.md)
- Full company guide: [Docker system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-docker-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
