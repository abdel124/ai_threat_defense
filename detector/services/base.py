from abc import ABC, abstractmethod

class AbstractThreatDetector(ABC):
    @abstractmethod
    def scan(self, text: str) -> bool:
        pass
