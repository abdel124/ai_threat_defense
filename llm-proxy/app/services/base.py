from abc import ABC, abstractmethod

class AbstractLLMClient(ABC):
    @abstractmethod
    async def query(self, prompt: str) -> str:
        pass