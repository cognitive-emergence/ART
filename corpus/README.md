# ART Falsification Corpus

This directory contains machine-readable adversarial cases used to test ART claims.

The corpus is not a collection of supportive examples. Each case must identify a concrete operational setting, name the structure under attack, permit reasonable substitutes, and define what outcome would weaken or falsify the current ART hypothesis.

## Directory layout

```text
corpus/
├── README.md
├── schema/
│   └── art-case.schema.json
├── index.json
└── cases/
    ├── agents/
    ├── commerce/
    ├── enterprise/
    ├── finance/
    ├── healthcare/
    ├── logistics/
    ├── public-sector/
    ├── robotics/
    ├── software/
    └── supply-chain/
```

## Case discipline

A valid case MUST separate:

1. observed facts / operational requirements;
2. the ART structure being challenged;
3. the deletion or substitution experiment;
4. measurable information loss or system failure;
5. a verdict that may weaken ART.

A mapping to ART vocabulary is not evidence by itself.

## Verdict vocabulary

- `SURVIVES` — the candidate structure appears operationally non-removable in this case.
- `WEAKENED` — a simpler substitute works with limited or no material loss.
- `FALSIFIED` — the stated ART claim fails for the defined scope.
- `INDETERMINATE` — evidence or system assumptions are insufficient.

## Initial corpus

The initial v0.1 corpus contains 20 adversarial cases across ten domains. These are starting probes, not empirical proof. The next milestone is to replace synthetic assumptions with independently documented real systems and reproducible traces.
