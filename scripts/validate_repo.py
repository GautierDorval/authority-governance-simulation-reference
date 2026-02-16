#!/usr/bin/env python3
"""
Minimal repository validation.

This repository is simulation-only. The goal of this script is to validate:
- JSON syntax (schemas + examples)
- JSON Schema conformance for examples
- Cross-artifact linkage (request_id / classification_id / decision_id)
- Basic timestamp ordering within each scenario chain

This is intentionally lightweight and is NOT a conformance checker for the
normative standard.
"""

from __future__ import annotations

import json
import sys
import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Tuple

try:
    import jsonschema  # type: ignore
except Exception as e:  # pragma: no cover
    print("ERROR: jsonschema is required for validation. Install with: pip install jsonschema", file=sys.stderr)
    raise


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        raise RuntimeError(f"Invalid JSON: {path}") from e


def parse_dt(value: str) -> datetime:
    # Accept Zulu timestamps.
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    return datetime.fromisoformat(value).astimezone(timezone.utc)


def schema_store() -> Dict[str, Any]:
    schemas_dir = REPO_ROOT / "schemas"
    store: Dict[str, Any] = {}
    for p in sorted(schemas_dir.glob("*.schema.json")):
        schema = load_json(p)
        sid = schema.get("$id")
        if not isinstance(sid, str) or not sid:
            raise RuntimeError(f"Schema missing $id: {p}")
        store[sid] = schema

        if "example.org" in sid:
            raise RuntimeError(f"Schema $id must not use example.org: {p} -> {sid}")
        if "authority-governance-simulation-reference" not in sid:
            raise RuntimeError(f"Schema $id should reference this repo: {p} -> {sid}")

    return store


def validate_example(example: Dict[str, Any], schema: Dict[str, Any], store: Dict[str, Any], path: Path) -> None:
    resolver = jsonschema.RefResolver.from_schema(schema, store=store)  # deprecated but practical
    try:
        jsonschema.validate(instance=example, schema=schema, resolver=resolver)
    except jsonschema.ValidationError as e:
        raise RuntimeError(f"Schema validation failed for {path}:\n{e.message}") from e


@dataclass(frozen=True)
class ScenarioChain:
    name: str
    request: Dict[str, Any]
    classification: Dict[str, Any]
    decision: Dict[str, Any]
    ledger: Dict[str, Any]


def load_scenarios() -> List[ScenarioChain]:
    req_dir = REPO_ROOT / "examples" / "authority-requests"
    cls_dir = REPO_ROOT / "examples" / "classification-results"
    dec_dir = REPO_ROOT / "examples" / "policy-decisions"
    led_dir = REPO_ROOT / "examples" / "ledger-entries"

    scenarios: List[Tuple[str, str, str, str]] = [
        ("publish_simulation", "publish_simulation.json", "publish_simulation.classification.json", "publish_simulation.decision.json", "publish_simulation.ledger.json"),
        ("delete_denied", "delete_denied.json", "delete_denied.classification.json", "delete_denied.decision.json", "delete_denied.ledger.json"),
        ("pay_denied", "pay_denied.json", "pay_denied.classification.json", "pay_denied.decision.json", "pay_denied.ledger.json"),
    ]

    out: List[ScenarioChain] = []
    for name, req_fn, cls_fn, dec_fn, led_fn in scenarios:
        req = load_json(req_dir / req_fn)
        cls = load_json(cls_dir / cls_fn)
        dec = load_json(dec_dir / dec_fn)
        led = load_json(led_dir / led_fn)
        out.append(ScenarioChain(name=name, request=req, classification=cls, decision=dec, ledger=led))
    return out


def validate_linkage(chain: ScenarioChain) -> None:
    req_id = chain.request["request_id"]
    cls_id = chain.classification["classification_id"]
    dec_id = chain.decision["decision_id"]

    # Request ↔ classification
    if chain.classification["request_id"] != req_id:
        raise RuntimeError(f"[{chain.name}] classification.request_id mismatch")

    # Classification ↔ decision
    if chain.decision["request_id"] != req_id:
        raise RuntimeError(f"[{chain.name}] decision.request_id mismatch")
    if chain.decision["classification_id"] != cls_id:
        raise RuntimeError(f"[{chain.name}] decision.classification_id mismatch")

    # Decision ↔ ledger
    if chain.ledger["request_id"] != req_id:
        raise RuntimeError(f"[{chain.name}] ledger.request_id mismatch")
    if chain.ledger["decision_id"] != dec_id:
        raise RuntimeError(f"[{chain.name}] ledger.decision_id mismatch")
    if chain.ledger.get("classification_id") != cls_id:
        raise RuntimeError(f"[{chain.name}] ledger.classification_id mismatch")

    # Timestamp monotonicity
    t_req = parse_dt(chain.request["timestamp"])
    t_cls = parse_dt(chain.classification["timestamp"])
    t_dec = parse_dt(chain.decision["timestamp"])
    t_led = parse_dt(chain.ledger["timestamp"])

    if not (t_req <= t_cls <= t_dec <= t_led):
        raise RuntimeError(
            f"[{chain.name}] timestamps out of order: request={t_req} cls={t_cls} decision={t_dec} ledger={t_led}"
        )


def main() -> int:
    store = schema_store()

    # Load schemas
    schemas_dir = REPO_ROOT / "schemas"
    schemas: Dict[str, Any] = {}
    for p in sorted(schemas_dir.glob("*.schema.json")):
        schema = load_json(p)
        schemas[p.name] = schema

    # Validate examples against schemas
    mapping = [
        ("examples/authority-requests", "authority-request.schema.json"),
        ("examples/classification-results", "classification-result.schema.json"),
        ("examples/policy-decisions", "policy-decision.schema.json"),
        ("examples/ledger-entries", "ledger-entry.schema.json"),
    ]

    for rel_dir, schema_name in mapping:
        schema = schemas.get(schema_name)
        if schema is None:
            raise RuntimeError(f"Missing schema: {schema_name}")
        dir_path = REPO_ROOT / rel_dir
        for p in sorted(dir_path.glob("*.json")):
            example = load_json(p)
            validate_example(example, schema, store, p)

    # Cross-artifact checks
    for chain in load_scenarios():
        validate_linkage(chain)

    print("OK: repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
