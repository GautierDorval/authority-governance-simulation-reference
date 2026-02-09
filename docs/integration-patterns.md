# Integration patterns (conceptual)

## Pattern: authority gate in front of execution

- all tool calls map to an authority_request
- classification happens before any tool execution
- policy decides allow / deny / escalate / simulate
- ledger entry is written for every outcome

## Pattern: simulation-first

- for high-risk classes, default to simulate
- human oversight becomes the only path to real execution (outside this repo)

## Pattern: conflict-aware pipeline

- planner proposes
- critic challenges
- unresolved conflict escalates or simulates
- never “argue” into authority
