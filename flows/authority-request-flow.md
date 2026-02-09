# Authority request flow (simulation-only)

## Goal

Illustrate how an agentic system should separate:
- inference (informational output)
- authority (request to act)

Core boundary:
- inference never implies authority

## Input

An authority request is a structured object describing:
- intent_summary
- action_class candidate (optional)
- target
- context flags (sensitivity, environment)
- requested mode: execute vs simulate (this repo uses simulate-only)

## Flow (conceptual)

1) Receive authority_request (do not execute)
2) Classify the request (taxonomy mapping)
3) Evaluate policy (allow / deny / escalate / simulate)
4) Produce a policy decision object
5) Write a ledger entry for the decision
6) Return simulation output only (no external effects)

## Outcomes

- allow: would be permitted in a real system, but remains simulation here
- deny: forbidden
- escalate: requires human oversight (no execution)
- simulate: simulation-only output (default for high-risk actions)

## Notes

This repository demonstrates the flow and data structures only.
