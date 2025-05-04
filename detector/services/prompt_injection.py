import re
from detector.services.base import AbstractThreatDetector

class PromptInjectionDetector(AbstractThreatDetector):
    def scan(self, text: str) -> bool:
        suspicious_patterns = [
            r"(?i)ignore previous instructions",
            r"(?i)you are now",
            r"(?i)forget all previous",
            r"(?i)pretend to be"
        ]
        for pattern in suspicious_patterns:
            if re.search(pattern, text):
                return True
        return False