# Counterexample Registry

This file is intentionally a permanent record. Counterexamples should remain visible even after the theory is revised.

## Status values

- `OPEN` — plausible challenge not yet resolved;
- `PARTIAL` — weakens a claim or narrows its scope;
- `RESOLVED` — current formulation explains the case without special pleading;
- `FATAL` — invalidates a current core hypothesis;
- `INDETERMINATE` — insufficient evidence.

## Registry

| ID | Candidate challenged | Counterexample / attack | Status | Consequence |
|---|---|---|---|---|
| CE-001 | Judgment universality | deterministic rule `if x > threshold then act` may need no explicit Judgment event | PARTIAL | Judgment claim narrowed to consequential discretionary commitment |
| CE-002 | Termination-event inevitability | fixed expiry can end authority without a separate Termination event | PARTIAL | termination *semantics* retained; first-class event remains unproven |
| CE-003 | Baseline universality | some tasks require only a terminal condition, not an explicit initial baseline | PARTIAL | Baseline treated as transition/measurement-dependent rather than universal |
| CE-004 | Responsibility as protocol primitive | systems can execute and verify outcomes while responsibility remains external in law/contracts | PARTIAL | Responsibility remains institutional layer, not minimal protocol fact |
| CE-005 | Causal attribution operational necessity | a service can complete and settle a deterministic outcome without full causal attribution | PARTIAL | Attribution moved downstream of minimal operational core |
| CE-006 | ART necessity | existing identity + authorization + workflow + logs may already be sufficient | OPEN | requires side-by-side implementation comparison |
| CE-007 | J/D/T/V minimality | intent/delegation/authorization/action/provenance grammars may be simpler | OPEN | alternative grammar program required |
| CE-008 | Outcome-market scale | verification cost may exceed the economic value of many real-world outcomes | OPEN | requires verification-economics filtering |

## Submission template

```text
ID:
Date:
Domain:
Claim challenged:
System requirements:
Proposed counterexample:
Why the system still works without the ART structure:
Simpler replacement, if any:
Evidence / implementation:
Suggested status:
```

## Research rule

A counterexample must not be relabeled as an ART structure merely to preserve the theory. If a competing model is simpler, that fact should be recorded explicitly.
