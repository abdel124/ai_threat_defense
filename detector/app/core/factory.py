from detector.services.prompt_injection import PromptInjectionDetector
from detector.services.pii_profane import PIIDetector
from detector.services.base import AbstractThreatDetector

class CombinedDetector(AbstractThreatDetector):
    def __init__(self):
        self.detectors = [
            PromptInjectionDetector(),
            PIIDetector()
        ]

    def scan(self, text: str) -> bool:
        return any(detector.scan(text) for detector in self.detectors)