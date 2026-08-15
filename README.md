# Accountable Reality Transition (ART)

**A falsifiable research framework for autonomous action across trust boundaries.**

ART is an open research program by **Cognitive Emergence**.

It asks a narrow but foundational question:

> **When autonomous actors begin to change reality across trust boundaries, which structures remain impossible to remove — regardless of what they are called or how they are implemented?**

ART does not begin by assuming a protocol, product, legal theory, or universal ontology. It begins with adversarial tests: remove a structure, replace it, hide it elsewhere, and test whether an independently designed system must reconstruct a semantic equivalent in order to keep functioning.

## Current working hypothesis

For consequential autonomous action across trust boundaries, three structures appear especially difficult to eliminate:

1. **Target** — what change is intended and what conditions define acceptable completion;
2. **Bounded Authority** — who may cause the change, within what scope, constraints, and validity;
3. **Verification** — how a claimed change becomes an accepted, evidence-supported state.

As autonomy, discretion, delegation depth, and institutional consequence increase, additional structures may be forced into explicit form:

- **Judgment** — a consequential commitment selecting, accepting, rejecting, or fixing a proposition among possible transitions;
- **Delegation** — propagation of bounded authority across actors;
- **Termination** — closure, revocation, expiry, completion, or supersession of authority or commitment relationships;
- **Causal Attribution** — what contributed to the observed transition;
- **Responsibility** — how consequences are normatively assigned;
- **Settlement** — how value, rights, reputation, or liabilities are reallocated after an accepted transition.

These are **research hypotheses**, not established primitives.

## Research discipline

ART should survive only if it withstands attack.

The project therefore uses five primary tests:

- **Deletion test** — remove the candidate structure. Can the system still achieve its stated purpose?
- **Substitution test** — can a simpler existing concept replace it without information loss?
- **Hidden-reconstruction test** — if explicit representation is forbidden, does the same semantics reappear in policy, code, logs, contracts, or human process?
- **Cross-domain test** — does the structure recur across independently different domains?
- **Independent-convergence test** — do independent designers facing the same constraints reconstruct an isomorphic structure without being given ART vocabulary?

A failed hypothesis should be revised or removed rather than protected.

## Machine-readable falsification corpus

ART includes a machine-readable corpus under [`corpus/`](corpus/) rather than relying only on prose examples.

The initial `v0.1` corpus contains **20 adversarial cases across ten domains**. Each case identifies:

- the operational setting and trust boundary;
- the candidate structure under attack;
- the deletion/substitution procedure;
- allowed alternatives;
- evidence required to evaluate the attack;
- the condition that would weaken or falsify the claim;
- a verdict vocabulary of `SURVIVES`, `WEAKENED`, `FALSIFIED`, or `INDETERMINATE`.

Cases conform to [`corpus/schema/art-case.schema.json`](corpus/schema/art-case.schema.json). A CI workflow validates schema conformance, unique case IDs, filename/ID consistency, and corpus-index completeness on relevant pushes and pull requests.

Local validation:

```sh
python -m pip install "jsonschema[format]>=4.23,<5"
python scripts/validate_corpus.py
```

The initial cases are synthetic adversarial probes. They are not empirical evidence for ART. The research goal is to progressively replace them with independently documented real systems, incidents, comparative designs, and reproducible traces.

## Relationship to TSTO and JEP

ART is the **theory layer**. It is intentionally distinct from specific engineering artifacts.

- **TSTO (Target State Transition Object)** defines a machine-verifiable object for **what state change counts as completion**. It fixes a subject, evidence-backed baseline, target, validity, constraints, verification policy, and integrity. It intentionally excludes responsibility, execution, pricing, settlement, and disputes.
- **JEP (Judgment Event Protocol)** explores interoperable representations of Judgment, Delegation, Termination, and Verification events.

A working layering is therefore:

```text
ART
  theory of accountable reality transitions
       │
       ├── TSTO
       │     intended transition / completion object
       │
       ├── JEP
       │     judgment-related event representation
       │
       └── bindings / implementations / domain profiles
```

ART does not require TSTO or JEP to be correct. TSTO and JEP do not prove ART. Each layer must remain independently falsifiable.

## Repository map

```text
.
├── README.md
├── README.zh-CN.md
├── theory/
│   ├── ART-v0.1.md
│   ├── definitions.md
│   └── claims-and-boundaries.md
├── falsification/
│   ├── README.md
│   ├── inevitability-tests.md
│   ├── alternative-grammars.md
│   └── counterexample-registry.md
├── corpus/
│   ├── README.md
│   ├── index.json
│   ├── schema/art-case.schema.json
│   └── cases/                 # 20 initial adversarial JSON cases
├── scripts/
│   └── validate_corpus.py
├── predictions/
│   └── prediction-ledger.md
├── relationships/
│   └── TSTO-JEP.md
├── examples/
│   └── cross-domain-cases.md
├── papers/
│   └── README.md
├── CONTRIBUTING.md
├── CITATION.cff
├── .zenodo.json
├── CHANGELOG.md
├── SECURITY.md
└── LICENSE.md
```

## Status

- Version: `ART v0.1`
- Status: Conceptual preprint / research hypothesis
- Publisher: **Cognitive Emergence**
- Initial public research date: **2026-08-15**
- Peer reviewed: **No**

The repository is deliberately explicit about uncertainty. Terms such as *inevitable*, *minimal*, *primitive*, *universal*, and *unique* are claims to be earned through falsification, not assumed by naming.

## Research priorities

The immediate priorities are:

1. test whether **Target, Bounded Authority, and Verification** are operationally non-removable under stated conditions;
2. test whether **Judgment, Delegation, Termination, and Verification** form a minimal event basis or whether a smaller/better grammar exists;
3. grow the machine-readable falsification corpus from synthetic probes into documented real systems and incidents;
4. maintain a timestamped prediction ledger;
5. invite independent alternative designs and publish failures openly.

## Related Cognitive Emergence work

- [TSTO Specification](https://github.com/cognitive-emergence/tsto-spec)
- JEP is treated here as a related engineering research program; ART does not depend on adoption of any single JEP version.

## Feedback

The most valuable contributions are counterexamples, simpler alternative models, failed mappings, and independently derived structures.

Please use GitHub Issues for research challenges, falsification reports, prior-art references, alternative grammars, and cross-domain cases.
