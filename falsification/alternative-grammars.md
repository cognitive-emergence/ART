# Alternative Grammars

ART should be compared against competing decompositions, not only against a null model.

## Baseline grammar A — security/workflow stack

```text
Identity → Authorization → Action → Audit Log
```

Attack question: can this stack represent consequential commitment, target completion semantics, delegation lifecycle, and post-condition verification without introducing additional first-class objects?

## Baseline grammar B — intent/action/provenance

```text
Intent → Delegation → Authorization → Action → Provenance
```

Attack question: does `Intent` subsume Judgment and Target without information loss? Does provenance subsume Verification?

## Baseline grammar C — state-machine view

```text
State + Transition Relation + Guard + Event
```

Attack question: can ordinary state-machine semantics express the institutional distinctions ART proposes without adding semantically equivalent labels?

## Baseline grammar D — capability model

```text
Object Capability → Invocation → Revocation
```

Attack question: can capability semantics absorb Bounded Authority, Delegation, and Termination more simply than ART's decomposition?

## Candidate ART control-event grammar

```text
J / D / T / V
```

Current interpretation:

- `J` — commitment around a consequential proposition or target;
- `D` — propagation of bounded authority or role;
- `T` — closure of authority/commitment relationships;
- `V` — evidence-based determination about a claim or transition.

This is not assumed to be minimal.

## Required comparison dimensions

Every grammar comparison should score:

1. semantic coverage;
2. information loss;
3. number of primitives;
4. composability;
5. cross-domain invariance;
6. deterministic validation;
7. compatibility with existing identity/auth/payment/transport standards;
8. implementation complexity;
9. human interpretability;
10. predictive usefulness.

## Kill condition for J/D/T/V

The J/D/T/V hypothesis should be rejected or revised if another grammar:

- uses fewer primitives;
- preserves the same relevant information;
- maps more naturally across domains;
- yields equal or better interoperability;
- avoids ambiguous or overlapping event classes.

## Invitation

Contributors are encouraged to submit a complete alternative grammar rather than only object-level objections. The strongest challenge is a working system that solves the same requirements with a materially simpler decomposition.
