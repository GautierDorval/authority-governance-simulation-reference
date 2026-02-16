# Policy decision flow

## Goal

Evaluate authority policy rules against a classified request.

## Inputs

- `classification_result` (action_class + risk envelope)
- authority policy (normative source in the manifest)

## Decision outputs

A `policy_decision` captures:

- decision: `allow` / `deny` / `escalate` / `simulate`
- `requirements`: list of required controls (ex.: `human_oversight`, `ledger`, `two_person_rule`)
- `rule_path`: rule reference for traceability
- linkage: `request_id` + `classification_id`

Schema:
- `schemas/policy-decision.schema.json`

## Conservative default

If a rule is missing or proofs are absent:
- `deny` or `escalate`
- never assume permissive execution

