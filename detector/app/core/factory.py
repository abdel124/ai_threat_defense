from app.services.prompt_injection import PromptInjectionDetector
from app.services.base import AbstractThreatDetector

def get_detector(name: str) -> AbstractThreatDetector:
    if name == "default":
        return PromptInjectionDetector()
    else:
        raise ValueError(f"Unsupported detector: {name}")