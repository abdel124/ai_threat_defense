from app.services.base import AbstractLLMClient

class LocalLLMClient(AbstractLLMClient):
    async def query(self, prompt: str) -> str:
        return f"[Local LLM] Echo: {prompt}"