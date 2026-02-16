# Integration patterns (conceptual)

## Pattern: authority gate in front of execution

- all tool calls map to an `authority_request`
- classification happens before any tool execution
- policy decides allow / deny / escalate / simulate
- a ledger entry is written for every outcome (including deny / simulate)

## Pattern: simulation-first (high-risk defaults)

- for high-risk classes, default to `simulate` or `deny`
- human oversight becomes the only path to real execution (outside this repo)

## Pattern: conflict-aware pipeline (planner vs critic)

- planner proposes
- critic challenges
- unresolved conflict escalates or simulates
- never “argue” into authority: policy and non-negotiables dominate

## Related reference (Layer 2)

If you want a minimal executable reference for **Constraintive Governance** (Layer 2),
see:

- https://github.com/GautierDorval/interpretive-agentic-reference

That repository demonstrates a bounded retrieval + fixed inference + schema validation
pipeline that can sit **before** Layer 3 authority governance.

