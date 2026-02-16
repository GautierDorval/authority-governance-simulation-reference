"""
DO NOT USE IN PRODUCTION — CONCEPTUAL STUB ONLY

This file defines a conceptual interface for classifying authority requests.
It is intentionally non-executable.

See:
- schemas/classification-result.schema.json
"""

from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass(frozen=True)
class ClassificationResult:
    classification_id: str
    timestamp: str
    request_id: str

    action_class: str
    surface: str
    criticality: str
    data_sensitivity: str
    reversibility_class: str

    notes: Optional[str] = None


def classify_authority_request(request: Dict[str, Any]) -> ClassificationResult:
    raise NotImplementedError("Conceptual stub only. No executable classification is provided.")
