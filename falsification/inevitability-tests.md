# Inevitability Tests

A structure is not treated as inevitable because it is common, useful, or fashionable. It must survive deletion and substitution.

## I-01 Target

**Setting:** an autonomous actor is asked to accomplish a consequential task.

**Delete:** all explicit target, goal, postcondition, desired-state, and acceptance-criteria semantics.

**Failure condition:** the system can no longer determine what counts as completion, or reconstructs equivalent semantics elsewhere.

**Current assessment:** strong conditional inevitability for purposeful action.

## I-02 Bounded Authority

**Setting:** an autonomous actor can use resources or powers controlled by another actor.

**Delete:** all scope, constraints, validity, permission, capability, and mandate semantics.

**Failure condition:** the system either becomes unable to act or grants effectively unbounded power, forcing an equivalent boundary mechanism to reappear.

**Current assessment:** strong candidate across trust boundaries.

## I-03 Verification

**Setting:** one actor claims that a consequential transition has occurred and another actor must rely on that claim.

**Delete:** evidence, measurement, observation, audit, attestation, and verification semantics.

**Failure condition:** acceptance becomes equivalent to trusting an unsupported self-claim, or an equivalent verification mechanism reappears.

**Current assessment:** strong candidate across trust boundaries; weaker in fully trusted or deterministic environments.

## I-04 Judgment

**Setting:** multiple consequential alternatives exist and an actor must commit resources, authority, or responsibility to one proposition.

**Delete:** all explicit decision commitment, approval, acceptance, rejection, selection, ranking, or judgment records.

**Failure condition:** the system cannot distinguish authority-to-act from the proposition actually committed to, or reconstructs a decision/approval/intent record.

**Current assessment:** conditional; not required for every deterministic action.

## I-05 Delegation

**Setting:** authority held by actor A is exercised by actor B on A's behalf.

**Delete:** all delegation, mandate-chain, impersonation, capability-transfer provenance, or equivalent semantics.

**Failure condition:** B's authority source becomes indeterminate, or equivalent provenance reappears.

**Current assessment:** strong conditional inevitability when authority crosses actors.

## I-06 Termination

**Setting:** authority, delegation, or commitment is not intended to last forever.

**Delete:** revocation, expiry, completion, supersession, cancellation, and scope-exhaustion semantics.

**Failure condition:** the relation becomes indefinite or the system reconstructs an end condition.

**Current assessment:** termination semantics are strong; first-class event representation remains unproven.

## I-07 Actor Binding

**Setting:** a system must distinguish who judged, authorized, acted, delegated, or verified.

**Delete:** stable actor binding within the relevant responsibility domain.

**Failure condition:** event ownership and authority provenance become indistinguishable.

**Current assessment:** strong requirement, but no claim that a single global identity protocol is inevitable.

## I-08 Temporal Ordering

**Setting:** validity depends on whether judgment, authorization, action, termination, and verification occurred in a meaningful order.

**Delete:** timestamps and all other partial-order mechanisms.

**Failure condition:** stale authority and post-hoc authorization cannot be distinguished from valid ordering.

**Current assessment:** strong structural requirement; absolute wall-clock time is not necessarily required.

## Scoring template

For each test, record:

- domain;
- operational requirements;
- removed structure;
- replacement allowed;
- observed failure;
- reconstructed equivalent;
- information loss;
- implementation complexity;
- verdict: `SURVIVES`, `WEAKENS`, `FAILS`, or `INDETERMINATE`.
