import openai
from app.services.base import AbstractLLMClient

class OpenAIClient(AbstractLLMClient):
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key

    async def query(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]