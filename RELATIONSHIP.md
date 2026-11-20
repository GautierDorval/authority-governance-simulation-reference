# Relationship to the normative standard

This repository is a **simulation-only reference**.

The normative definitions of Authority Governance (Layer 3) and the Agentic Operations Pack
live in:

- https://github.com/GautierDorval/interpretive-governance-manifest

This repository:
- does not define conformance,
- does not extend the standard,
- does not replace normative artifacts.

If a discrepancy exists, the normative repository prevails.

## Relationship to related (non-normative) references

This repository complements the executable Layer 2 reference:

- https://github.com/GautierDorval/interpretive-agentic-reference

Interpretive Agentic Reference demonstrates **Constraintive Governance** (Layer 2) in a minimal executable form.  
This repository demonstrates **Authority Governance** (Layer 3) as simulation artifacts and schemas only.

## Relationship to interpretive fidelity

This repository simulates authority decisions: whether a requested action is allowed, denied, escalated or simulated within a declared scope. Authorization and scope are distinct from fidelity.

- An authority decision concerns an action. [Interpretive fidelity](https://gautierdorval.com/en/definitions/interpretive-fidelity/), for which reconstruction fidelity is the entry term in the context of AI-generated answers, concerns whether an answer preserves the meaning and boundaries of its sources.
- The two meet when an answer reports on authority: presenting a capability as a permission, a simulated decision as an executed one, or a policy decision as something the system can authorize changes the status of a claim. The public [authority boundary rubric](https://github.com/GautierDorval/interpretive-governance-test-suite/blob/cf61a18ab86d547443d6c0962d4c20ad9ed796f1/scoring-models/authority-boundary-score.md) of the interpretive governance test suite, cited here at a fixed revision, describes how such shifts can be assessed in answers.
- The schemas, stubs, examples and ledger entries of this repository are simulation artifacts. Their presence, their schema validation and their cross-artifact linkage produce no semantic result and no fidelity measure.

## Versioning note

All schema `$id` values in this repository are pinned to the tag declared in `VERSION`
to reduce drift and preserve artifact identity.

