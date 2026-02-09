# Policy decision flow

## Goal

Evaluate authority policy rules against a classified request.

## Inputs

- classified request (action_class + envelope)
- authority policy (normative source)

## Decision outputs

- allow / deny / escalate / simulate
- requirements list (human_oversight, ledger, identity, proof_reversibility, two_person_rule, etc.)
- rule_path reference for traceability

## Conservative default

If a rule is missing or proofs are absent:
- deny or escalate
- never assume permissive execution
