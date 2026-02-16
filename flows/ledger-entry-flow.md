# Ledger entry flow

## Goal

Record authority outcomes in an audit-friendly entry.

## Required records

Ledger entries should exist for:
- `allow`
- `deny`
- `escalate`
- `simulate`
- `rollback` (if applicable)

## Minimal fields (simulation reference)

A `ledger_entry` captures:

- `entry_id`, `timestamp`, `environment`
- linkage: `request_id` + `decision_id` (and optionally `classification_id`)
- `actor_identity`
- `intent_summary`, `action_class`, `target`
- `surface`, `data_sensitivity`
- `taxonomy_version`, `policy_version`, `rule_path`
- `decision`
- `proof_refs` (pointers only, never invented content)
- `notes` (optional)

Schema:
- `schemas/ledger-entry.schema.json`

## Examples

See `examples/ledger-entries/` for filled entries that link back to requests and decisions.

