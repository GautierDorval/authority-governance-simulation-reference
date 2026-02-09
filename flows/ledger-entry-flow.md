# Ledger entry flow

## Goal

Record authority decisions in an audit-friendly entry.

## Required records

Ledger entries must exist for:
- allow
- deny
- escalate
- simulate
- rollback (if applicable)

## Minimal fields (conceptual)

- entry_id, timestamp, environment
- actor_identity, principal_identity (optional)
- intent_summary, action_class, target
- taxonomy_version, policy_version, rule_path
- decision
- proof_refs (pointers only)

## Notes

This repository includes example ledger entries in `examples/ledger-entries/`.
