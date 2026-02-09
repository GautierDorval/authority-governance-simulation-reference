"""
DO NOT USE IN PRODUCTION — CONCEPTUAL STUB ONLY

This file defines a conceptual interface for evaluating authority policy.
It is intentionally non-executable.
"""

from dataclasses import dataclass
from typing import Dict, Any, List, Optional


@dataclass(frozen=True)
class PolicyDecision:
    decision: str  # allow | deny | escalate | simulate
    rule_path: str
    requirements: List[str]
    notes: Optional[str] = None


def evaluate_policy(classified: Dict[str, Any]) -> PolicyDecision:
    raise NotImplementedError("Conceptual stub only. No executable policy engine is provided.")
