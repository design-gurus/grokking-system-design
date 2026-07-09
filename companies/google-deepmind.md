# Google DeepMind: system design interview

> How Google DeepMind actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Google DeepMind runs it.** Software engineers get a Google-style design round with an ML accent; research engineers get the rarer conversation: designing the machinery of frontier AI itself (distributed training, evaluation harnesses, experiment infrastructure). Rounds are strictly AI-tool-free, and estimates are probed with "how many machines is that?"

## Signature questions

- Design a model serving platform with tight latency percentiles, or an embedding/feature store
- Design distributed training for a model that does not fit on one accelerator (parallelism, checkpointing, failure recovery)
- Design an evaluation harness that runs dozens of benchmarks reproducibly across model versions
- Design experiment management for hundreds of researchers sharing an accelerator fleet

## What interviewers probe

- First-principles resource math: memory per parameter, interconnect bytes, tokens per second per chip
- Failure as the steady state: checkpoint cadence versus lost-work math at thousand-chip scale
- Reproducibility discipline: versioned data, seeds, and exact rerunnability as design requirements

## Prepare

- Patterns to review: [replication](../patterns/replication.md), [consistency models](../patterns/consistency-models.md), [write ahead log](../patterns/write-ahead-log.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md)
- Practice questions: [Design chatgpt](../questions/design-chatgpt.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md)
- Full company guide: [Google DeepMind system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-google-deepmind-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
