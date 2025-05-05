from fastapi import FastAPI
from pydantic import BaseModel
from app.core.factory import get_llm_backend
import httpx

app = FastAPI()

class LLMQuery(BaseModel):
    prompt: str
    model: str

@app.post("/query")
async def query_llm(req: LLMQuery):
    llm_client = get_llm_backend(req.model.lower())
    result = await llm_client.query(req.prompt)

    # Call detector service
    async with httpx.AsyncClient() as client:
        detect_response = await client.post(
            "http://127.0.0.1:8002/detect",
            json={"input_text": result, "user_id": "anonymous"}  # You can pass real user ID if available
        )
        detection_result = detect_response.json()

    return {
        "response": result,
        "threat_detected": detection_result.get("threat_detected", False)
    }