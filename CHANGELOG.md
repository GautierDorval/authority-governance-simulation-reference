# Changelog — authority-governance-simulation-reference

## v2026-02-demo-v2

- Fixed schema identity: `$id` now points to this repository (pinned tag), not `example.org`.
- Added `classification-result` artifact (schema + filled examples) to complete the request → classification → decision → ledger chain.
- Hardened `ledger-entry` schema (documented optional fields, strict typing, `additionalProperties: false`).
- Added minimal CI validation (JSON syntax + schema validation + cross-artifact linkage checks).
- Standardized license to Apache-2.0 and added `CITATION.cff`.
- Documentation hardening: clarified relationship to the normative manifest and to the (executable) Layer 2 reference.
- Fixed filename typo (`non-iimplementation-guide.md` → `non-implementation-guide.md`) with a compatibility stub.

## v2026-02-demo-v1

- Initial publication of the simulation-only reference repository.
- Conceptual authority request flows (classification, policy decision, ledger).
- Non-executable stubs and schemas.
- No production code, no execution logic, no implementation recipes.
