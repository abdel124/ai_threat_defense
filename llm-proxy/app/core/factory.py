import os
from app.services.openai_client import OpenAIClient
from app.services.local_client import LocalLLMClient
from app.services.base import AbstractLLMClient

def get_llm_backend(name: str) -> AbstractLLMClient:
    if name == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set in the environment.")
        return OpenAIClient(api_key=api_key)
    elif name == "local":
        return LocalLLMClient()
    else:
        raise ValueError(f"Unsupported backend: {name}")