from app.services.prompt_injection import PromptInjectionDetector
from app.services.pii_profane import PIIDetector
from app.services.base import AbstractThreatDetector

class CombinedDetector(AbstractThreatDetector):
    def __init__(self):
        self.detectors = [
            PromptInjectionDetector(),
            PIIDetector()
        ]

    def scan(self, text: str) -> bool:
        return any(detector.scan(text) for detector in self.detectors)

def get_detector(name: str) -> AbstractThreatDetector:
    if name == "default":
        return CombinedDetector()
    else:
        raise ValueError(f"Unsupported detector: {name}")
