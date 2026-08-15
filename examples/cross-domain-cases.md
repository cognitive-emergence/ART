# Cross-Domain Cases

These cases are not proofs. They are test material for asking whether ART structures recur without forcing the mapping.

## Case 1 — Enterprise procurement

**Initial state:** required goods not acquired.  
**Target:** specified goods delivered and accepted under budget/time constraints.  
**Authority:** procurement actor or agent may commit spend within scope.  
**Delegation:** procurement authority may be transferred to an agent or employee.  
**Action:** quote selection, order, payment, logistics.  
**Verification:** delivery, quantity, quality, invoice, acceptance evidence.  
**Responsibility/settlement:** payment, refund, penalties, supplier obligations.

Attack: can a cross-company procurement system remove Target, Authority, or Verification without reconstructing equivalents?

## Case 2 — Software production deployment

**Initial state:** version not in production.  
**Target:** specified artifact running under defined SLO/security conditions.  
**Authority:** release actor may modify production under scope.  
**Action:** deploy / migrate / configure.  
**Termination:** release permission expires, completes, or is revoked.  
**Verification:** test results, monitoring, artifact hashes, SLO evidence.

Attack: does a deterministic CI/CD policy eliminate the need for explicit Judgment while retaining the rest of the structure?

## Case 3 — Digital advertising

**Initial state:** capital allocated but target users/revenue not acquired.  
**Target:** measurable user/revenue state under CAC/ROAS and policy constraints.  
**Authority:** buyer/agent may spend within campaign and budget bounds.  
**Action:** bids, campaign changes, creative allocation.  
**Verification:** attributed users/revenue and fraud filtering.

Attack: where does causality become necessary, and where can simple outcome verification suffice?

## Case 4 — Invoice settlement

**Initial state:** invoice overdue with balance outstanding.  
**Target:** balance settled by deadline with specified evidence.  
**Authority:** finance actors may negotiate/payment-route within defined limits.  
**Action:** reminders, negotiation, transfer.  
**Verification:** bank settlement receipt + ledger state.  
**Settlement:** accounting state closes.

This is a strong TSTO-style case because target and evidence can be defined with low ambiguity.

## Case 5 — Autonomous commerce purchase

**Initial state:** user intent exists; product not purchased.  
**Target:** qualifying product acquired under price, quantity, merchant, and policy constraints.  
**Judgment:** discretionary selection among acceptable products may be explicit.  
**Authority:** agent has bounded spend/purchase permission.  
**Delegation:** principal authorizes agent.  
**Action:** purchase.  
**Verification:** order/payment/fulfillment evidence.

Attack: can ordinary payment authorization fully subsume Judgment and Target semantics?

## Case 6 — Physical delivery

**Initial state:** item at origin.  
**Target:** item delivered to accepted destination/recipient before deadline and without specified damage conditions.  
**Action:** multi-carrier physical movement.  
**Verification:** scans, signatures, geolocation, sensor evidence.  
**Challenge:** external reality is only partially observable and may produce conflicting evidence.

Attack: does verification cost exceed the value of formalized outcome contracting?

## Case 7 — Healthcare administrative workflow

**Initial state:** referral/authorization/prescription or reimbursement not completed.  
**Target:** a clearly defined administrative state change.  
**Authority:** professional, payer, patient, or institution has scoped powers.  
**Verification:** authoritative records.

Boundary: this example deliberately avoids assuming that clinical outcome, truth, or legal responsibility can be mechanically determined by ART.

## Case 8 — Government permit

**Initial state:** permit not granted.  
**Target:** permit issued under specified conditions.  
**Judgment:** an authorized decision maker may accept/reject a claim.  
**Authority:** statutory/organizational powers.  
**Verification:** signed permit and registry evidence.

Attack: is Judgment independent of Authorization, or can the approval be modeled as ordinary state transition under fixed rules?

## Case template

```text
Domain:
Actors:
Trust boundaries:
Initial observed state:
Target:
Constraints:
Bounded authority:
Judgment, if any:
Delegation, if any:
Actions:
Termination semantics:
Evidence:
Verification:
Observed/accepted state:
Causal attribution, if needed:
Responsibility, if needed:
Settlement/consequence, if any:
Structure that can be removed:
Structure that reappears elsewhere:
Verdict:
```
