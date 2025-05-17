from fastapi import FastAPI
from pydantic import BaseModel
from app.core.factory import get_llm_backend
import httpx
from datetime import datetime

app = FastAPI()

class LLMQuery(BaseModel):
    prompt: str
    model: str

@app.post("/query")
async def query_llm(req: LLMQuery):
    llm_client = get_llm_backend(req.model.lower())
   # print('kiki ', llm_client)
    result = await llm_client.query(req.prompt)

    async with httpx.AsyncClient() as client:
        # Scan output with detector
        detect_response = await client.post(
            "http://detector:8002/detect",
            json={"input_text": result, "user_id": "anonymous"}
        )
        detection_result = detect_response.json()

        # Log full interaction
        await client.post("http://logger:8003/log", json={
            "user_id": "anonymous",
            "input_text": req.prompt,
            "output_text": result,
            "input_threat_detected": False,  # handled by api-gateway
            "output_threat_detected": detection_result.get("threat_detected", False),
            "timestamp": datetime.utcnow().isoformat()
        })

    return {
        "response": result,
        "output_threat_detected": detection_result.get("threat_detected", False)
    }
