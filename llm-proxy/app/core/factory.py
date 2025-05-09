from app.services.openai_client import OpenAIClient
from app.services.local_client import LocalLLMClient
from app.services.base import AbstractLLMClient

def get_llm_backend(name: str) -> AbstractLLMClient:
    if name == "openai":
        return OpenAIClient(api_key="")
    elif name == "local":
        return LocalLLMClient()
    else:
        raise ValueError(f"Unsupported backend: {name}")