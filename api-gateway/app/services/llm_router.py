import httpx
from app.models.request import QueryRequest

class LLMRouter:
    async def route_request(self, request: QueryRequest) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://llm-proxy:8001/query",
                json={"prompt": request.prompt, "model": request.model}
            )
            return {
                "status": "success",
                "model": request.model,
                "response": response.json()["response"]
            }