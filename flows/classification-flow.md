# Classification flow

## Goal

Map an authority request to a taxonomy action_class and risk envelope.

## Inputs

- authority_request
- action taxonomy (normative source)

## Classification outputs (conceptual)

- action_class (string)
- surface (internal/external)
- criticality (low/medium/high/critical)
- data_sensitivity (none/confidential/pii/secret)
- reversibility_class (reversible/compensable/irreversible)

## Failure behavior

If classification is ambiguous:
- degrade to escalate or simulate
- record ambiguity in ledger notes
