# Conformance checklist (conceptual)

This checklist is descriptive only.

## Boundary

- inference never implies authority
- unknown remains explicit
- persuasive “tie-breakers” do not override policy

## Authority governance primitives

- taxonomy classification exists (action class + surface + criticality + sensitivity + reversibility)
- policy outcomes are conservative by default
- proofs are pointers, not invented content
- ledger exists for deny / escalate / simulate / allow

## Ops pack primitives

- human oversight gates exist for critical actions
- privacy and minimization are respected
- change control and drift detection exist
- injection and exfiltration risks are considered
- incident response exists (kill switch concept)

## Reproducibility signals (recommended)

- schemas exist for key artifacts (request, classification, decision, ledger)
- examples validate against schemas
- cross-artifact linkage is checkable (request_id / decision_id)
