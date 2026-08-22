# Sierra: system design interview

> How Sierra actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Sierra runs it.** The system design round replaced the coding screen, which the company has said publicly, so this session decides more of the result than at most places. You design an agentic system for a real customer use case, and one reported question is an agent that handles subscription cancellation for a company. Product judgment is graded next to the architecture: conversation flow, guardrails, safe typed tool calls into billing systems, human handoff, and how you would measure whether the agent works.

## Signature questions

- Design an agent that handles subscription cancellation
- Design an agent for refunds, order changes, or appointment booking
- Design guardrails that stop wrong or unsafe agent actions
- Design safe tool calls into a customer's billing or scheduling systems
- Design the evaluation setup that replays recorded conversations against new agent versions

## What interviewers probe

- Product thinking alongside architecture, including why a user would accept the flow
- Honesty about model failure: confirmations, policy checks, human handoff, and logging
- Communication order: requirements, design, risks, measurement, with check-ins before going deep
- What you would cut for a first version, said out loud

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [circuit breaker](../patterns/circuit-breaker.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md), [caching](../patterns/caching.md), [api gateway](../patterns/api-gateway.md)
- Practice questions: [Design ai agent orchestration](../questions/design-ai-agent-orchestration.md), [Design model evaluation pipeline](../questions/design-model-evaluation-pipeline.md), [Design chatgpt](../questions/design-chatgpt.md)
- Full company guide: [Sierra system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-sierra-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
