# Contributing to ART

ART is a research repository. The highest-value contribution is often a successful attack on the current theory.

## Preferred contributions

We especially welcome:

- counterexamples;
- simpler alternative grammars;
- prior art that weakens an originality claim;
- real systems that work without a proposed inevitable structure;
- cross-domain cases that fail to map naturally;
- independent derivations that converge on or diverge from ART;
- implementation evidence about verification cost, ambiguity, or interoperability;
- corrections to definitions or prediction records.

## Contribution standard

Please distinguish among:

1. **Observation** — what a real system does;
2. **Interpretation** — how you think it maps to a concept;
3. **Claim** — what general conclusion you infer;
4. **Evidence** — what allows another person to inspect or reproduce the claim.

Avoid presenting a convenient mapping as proof of inevitability.

## Counterexample format

A useful counterexample should include:

```text
Domain:
Operational requirements:
ART claim challenged:
Structure removed:
Replacement used, if any:
Why the system still works:
Evidence / implementation details:
Information lost, if any:
Suggested theory change:
```

## Alternative grammar format

```text
Primitive set:
Definitions:
Target problem domain:
Example mappings:
Why it is smaller/better:
Where ART loses information or creates redundancy:
Implementation evidence, if available:
```

## Prediction ledger

Do not edit the original wording of a timestamped prediction after evidence emerges. Add dated evaluations below the original text.

## Terminology discipline

Terms such as `universal`, `minimal`, `primitive`, `inevitable`, `unique`, and `canonical` require explicit evidence. Use narrower wording when the claim is not yet established.

## Engineering proposals

Engineering proposals should preserve layer boundaries. Do not place legal responsibility, payment, workflow, or other domain-specific semantics into a narrow core unless cross-domain necessity is demonstrated.

## Conduct

Critique ideas and evidence directly. Strong disagreement and adversarial testing are welcome; personal attacks are not.
