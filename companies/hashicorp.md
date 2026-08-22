# HashiCorp: system design interview

> How HashiCorp actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How HashiCorp runs it.** Every prompt maps onto one of the company's own tools: secrets storage (Vault), job placement (Nomad), shared state with locking (Terraform), and service discovery (Consul). Candidates report one or two design rounds inside the virtual onsite, 45 to 60 minutes each, next to pair programming and PR review. Interviewers change the requirements mid-discussion, so the grade includes how you adjust and whether you still name what each choice costs.

## Signature questions

- Design a secrets manager with per-request policy checks and audit logging
- Design a job scheduler that places work on healthy servers and restarts after failure
- Design shared state with locking so two writers never overlap
- Design service discovery as servers join and leave
- Design rate limiting, caching, and replication for an API

## What interviewers probe

- Requirements and rough numbers first, without being prompted
- The cost of each choice, not only its benefit
- Failure thinking at three levels: a server, a network link, and a whole zone
- Choosing consistency over availability where the data is dangerous when stale, and defending it

## Prepare

- Patterns to review: [distributed locking](../patterns/distributed-locking.md), [leader election](../patterns/leader-election.md), [quorum](../patterns/quorum.md), [consistency models](../patterns/consistency-models.md), [heartbeats](../patterns/heartbeats.md)
- Practice questions: [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design api gateway](../questions/design-api-gateway.md), [Design rate limiter](../questions/design-rate-limiter.md)
- Full company guide: [HashiCorp system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-hashicorp-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
