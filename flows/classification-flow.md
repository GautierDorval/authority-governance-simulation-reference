# Classification flow

## Goal

Map an `authority_request` to a taxonomy `action_class` and a risk envelope.

This classification is **conceptual** in this repository:
- no executable classifier is provided,
- but the intermediate artifact is represented and typed for auditability.

## Inputs

- `authority_request`
- action taxonomy (normative source in the manifest)

## Classification outputs

A `classification_result` captures:

- `action_class` (string)
- `surface` (`internal` | `external`)
- `criticality` (`low` | `medium` | `high` | `critical`)
- `data_sensitivity` (`none` | `confidential` | `pii` | `secret`)
- `reversibility_class` (`reversible` | `compensable` | `irreversible`)

Schema:
- `schemas/classification-result.schema.json`

## Failure behavior

If classification is ambiguous:
- degrade to `escalate` or `simulate`,
- record ambiguity in `classification_result.notes` and/or in the ledger entry.

