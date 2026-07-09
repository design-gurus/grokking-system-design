# Adobe: system design interview

> How Adobe actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Adobe runs it.** Design runs at three altitudes: product architecture at creative-cloud scale, object-oriented low-level design, and database judgment, increasingly with a generative-AI accent (Firefly-style features with GPU economics inside consumer products).

## Signature questions

- Design a cloud document service: layered documents, versioning, sync, collaboration (model-first: operation logs over file overwrites)
- Design an asset pipeline for multi-gigabyte files: chunked uploads, delta sync, preview generation
- Design a generative AI feature at product scale: queuing, latency inside an interactive tool, cost control
- LLD: a document editor's object model with undo/redo (the command-pattern question in its natural habitat)

## What interviewers probe

- Document-model thinking: start with the data model, derive the architecture
- Large-binary pragmatics: a one-pixel edit must not re-upload four gigabytes
- Undo as a design constraint across every prompt

## Prepare

- Patterns to review: [cdn](../patterns/cdn.md), [caching](../patterns/caching.md), [consistency models](../patterns/consistency-models.md), [checksums](../patterns/checksums.md)
- Practice questions: [Design google docs](../questions/design-google-docs.md), [Design dropbox](../questions/design-dropbox.md), [Design collaborative whiteboard](../questions/design-collaborative-whiteboard.md)
- Full company guide: [Adobe system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-adobe-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
