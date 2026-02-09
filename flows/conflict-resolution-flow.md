# Conflict resolution flow (planner vs critic)

## Goal

Prevent multi-role systems from drifting into contradictory action.

## Pattern

- planner proposes a request
- critic challenges classification, policy fit, or risk
- if conflict persists:
  - escalate to human oversight, or
  - degrade to simulate-only

## Requirements

- conflicts must be recorded (ledger notes or proof_refs)
- no “persuasive” tie-breaker
- policy and non-negotiables dominate
