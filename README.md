# Authority governance — simulation reference

> **Non-normative simulation reference**  
> This repository illustrates conceptual patterns for **Authority Governance** (Layer 3)  
> as defined in the normative standard:  
> https://github.com/GautierDorval/interpretive-governance-manifest (pinned releases preferred)

## Critical notices

**This is NOT production code.**  
**This is NOT a prescriptive implementation guide.**  
**This is NOT an endorsement of any specific technical stack.**  
**This is NOT a safety guarantee.**

This repository exists to:
- illustrate normative constraints defined in the manifest (Layer 3)
- demonstrate decision flows and data structures
- provide conceptual integration patterns (**simulation-only**)

This repository does NOT:
- provide executable orchestration code
- prescribe tool wiring or infrastructure
- include security hardening or production patterns
- guarantee safety, compliance, or fitness for purpose
- provide bypass or exploitation guidance

Conformance to the standard is determined by the manifest, not by this reference.

## Why the stubs are non-executable (by design)

All code under `stubs/` raises `NotImplementedError` on purpose.

This is a safety and scope boundary:
- to prevent accidental production use,
- to avoid implying a normative implementation recipe,
- to keep this repository focused on **flows + schemas + examples**.

## Relationship to the normative standard (source of truth)

Normative definitions live in the manifest repository:

- Manifest repo: https://github.com/GautierDorval/interpretive-governance-manifest  
- Preferred: pinned releases (this demo references `v1.4.1` in `DEMO-META.yaml`).

If a discrepancy exists, the normative repository prevails.

## Relationship to the executable Layer 2 reference

This repository illustrates **Authority Governance** (Layer 3).  
If you also need a minimal executable illustration for **Constraintive Governance** (Layer 2), see:

- https://github.com/GautierDorval/interpretive-agentic-reference

These two references are complementary:
- Layer 2 reference: bounded retrieval + fixed inference + schema validation + policy-driven abstention
- This repo (Layer 3): authority classification + policy decision + ledger entry (**simulation-only**)

## What this demonstrates

- `authority_request` → `classification_result` → `policy_decision` → `ledger_entry`
- decision paths: allow / deny / escalate / simulate
- simulation-only behavior (no execution)
- conflict handling (planner vs critic)
- ledger entry format examples (traceability + opposability signals)

```mermaid
flowchart LR
  AR[authority_request] --> CR[classification_result] --> PD[policy_decision] --> LE[ledger_entry]
```

## Quick start

Start with:
- `SCOPE.md`
- `flows/authority-request-flow.md`
- `schemas/`
- `examples/`

### End-to-end scenarios (filled)

Each scenario provides a complete chain of artifacts:

- `examples/authority-requests/`
- `examples/classification-results/`
- `examples/policy-decisions/`
- `examples/ledger-entries/`

## License

Apache-2.0. See `LICENSE.md`.

