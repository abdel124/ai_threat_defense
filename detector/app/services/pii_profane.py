import re
from detector.services.base import AbstractThreatDetector

class PIIDetector(AbstractThreatDetector):
    def scan(self, text: str) -> bool:
        pii_patterns = [
            r"\b\d{3}-\d{2}-\d{4}\b",     # SSN format
            r"\b\d{16}\b",                 # Credit card
            r"\b\d{10}\b",                 # Phone number
            r"(?i)\b(password|ssn|secret)\b"  # Sensitive keywords
        ]
        for pattern in pii_patterns:
            if re.search(pattern, text):
                return True
        return False