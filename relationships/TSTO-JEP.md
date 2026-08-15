# ART, TSTO, and JEP

This document keeps the theory and engineering layers separate.

## ART

**ART (Accountable Reality Transition)** is a falsifiable theory/research framework. It asks which structures become non-removable when autonomous actors cause consequential changes across trust boundaries.

ART is not a wire protocol and does not define a JSON object.

## TSTO

**TSTO (Target State Transition Object)** is an engineering specification from Cognitive Emergence for expressing **what state change counts as completion**.

TSTO/00 currently fixes:

- Subject;
- evidence-backed Baseline;
- machine-evaluable Target;
- validity/time boundaries;
- Constraints;
- immutable Profile reference;
- Verification Policy reference;
- content integrity.

TSTO intentionally does **not** encode:

- responsible party;
- workflow or execution plan;
- pricing;
- settlement;
- legal liability;
- mutable execution status.

Repository: https://github.com/cognitive-emergence/tsto-spec

## JEP

**JEP (Judgment Event Protocol)** explores interoperable representations of judgment-related events such as:

- Judgment;
- Delegation;
- Termination;
- Verification.

ART does not assume J/D/T/V is already minimal, sufficient, or unique. That is an active falsification target.

## Layering

```text
ART
│
│  asks what structures are unavoidable and why
│
├── TSTO
│   machine-verifiable intended transition / completion object
│
├── JEP
│   candidate judgment-related event grammar
│
└── Bindings / Profiles / Infrastructure
    identity, execution, evidence, enterprise systems,
    payments, compliance, settlement, etc.
```

## Important separation: verification policy vs verification event

A target object may specify **how** a future result should be verified. That is not the same as an actual verification event that later occurs.

Therefore:

```text
verification policy ≠ verification event
```

This separation is important for preserving the immutability of a target object while allowing multiple later determinations.

## Independence rule

The layers are intentionally non-circular:

- ART is not proven because TSTO or JEP exists;
- TSTO may remain useful even if ART is revised;
- JEP may remain useful even if J/D/T/V is not a natural minimal basis;
- ART may survive even if a better protocol replaces TSTO or JEP.

## Compatibility objective

ART-related engineering should complement rather than replace established identity, authentication, authorization, transport, payment, audit, and domain standards unless a concrete information gap is demonstrated.

The goal is to find the narrowest missing semantic layer, not to rebuild the entire stack.
