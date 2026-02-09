# Authority governance — simulation reference

> **Non-normative simulation reference**  
> This repository illustrates conceptual patterns for authority governance  
> as defined in the normative repository:  
> https://github.com/GautierDorval/interpretive-governance-manifest (pinned releases preferred)

## Critical notices

**This is NOT production code.**  
**This is NOT a prescriptive implementation guide.**  
**This is NOT an endorsement of any specific technical stack.**

This repository exists to:
- illustrate normative constraints defined in the manifest (Layer 3)
- demonstrate decision flows and data structures
- provide conceptual integration patterns (simulation-only)

This repository does NOT:
- provide executable orchestration code
- prescribe tool wiring or infrastructure
- include security hardening or production patterns
- guarantee safety, compliance, or fitness for purpose
- provide bypass or exploitation guidance

Conformance to the standard is determined by the manifest, not by this reference.

## Relationship to the normative standard

Normative definition (Layer 3 + ops pack):
- https://raw.githubusercontent.com/GautierDorval/interpretive-governance-manifest/v1.1.0/authority/inference-vs-authority.md
- https://raw.githubusercontent.com/GautierDorval/interpretive-governance-manifest/v1.1.0/authority/authority-policy.json
- https://raw.githubusercontent.com/GautierDorval/interpretive-governance-manifest/v1.1.0/authority/authority-ledger-spec.md

## What this demonstrates

- authority_request → classification → policy evaluation → decision
- decision paths: allow / deny / escalate / simulate
- simulation-only behavior (no execution)
- conflict handling (planner vs critic)
- ledger entry format examples

## Quick start

Start with:
- `SCOPE.md`
- `flows/authority-request-flow.md`
- `schemas/`
- `examples/`

## License

See `LICENSE.md`.
