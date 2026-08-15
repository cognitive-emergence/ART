# Prior-Art Map

ART should be evaluated against established and emerging work rather than treated as isolated terminology.

This file is a map of research families to investigate. It is not an originality claim and is intentionally incomplete at v0.1.

## State-transition and formal-method traditions

Questions:

- What does ART add beyond ordinary state machines, transition systems, temporal logic, and guarded transitions?
- Are Target and Constraint merely established postcondition/invariant concepts in another vocabulary?
- Which proposed ART distinctions are genuinely institutional rather than computational?

## Identity, authentication, and authorization

Questions:

- Can existing identity + authorization + capability systems fully represent Bounded Authority?
- When does delegation provenance require a distinct portable object?
- Can authorization metadata absorb Judgment without information loss?

## Workflow and business-process systems

Questions:

- Are ART structures already latent in workflow goals, approvals, roles, transitions, and completion states?
- Does ART compress across workflow products or simply rename them?

## Provenance and audit

Questions:

- Can execution provenance and audit context fully subsume Judgment, Delegation, and Verification?
- When does an audit record become evidence of an outcome rather than only an event?

## Decision and governance systems

Questions:

- Is Judgment reducible to decision records, approvals, intents, or policy evaluations?
- Under what conditions is a commitment record independently necessary?

## Contracts, SLAs, and outcome-based mechanisms

Questions:

- Are Target/Verification structures already fully expressed by contracts, SLAs, acceptance tests, escrow, and oracle systems?
- What changes when these objects must become machine-portable across autonomous systems?

## Institutional responsibility and liability

Questions:

- Which responsibility relations can be derived from technical records?
- Which necessarily remain external normative determinations?
- How should ART avoid conflating causal provenance with legal or moral responsibility?

## Cognitive Emergence related work

- TSTO — Target State Transition Object Specification
- JEP — Judgment Event Protocol research program

See `relationships/TSTO-JEP.md` for the intended separation.

## Contribution rule

When adding a prior-art reference, include:

```text
Reference:
Date:
Concepts overlapped:
What it already solves:
What ART may still add:
Potential originality claim weakened:
Potential ART hypothesis strengthened:
```

Prior art that weakens ART is especially valuable.
