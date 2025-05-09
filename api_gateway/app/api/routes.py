from fastapi import APIRouter, Depends, Header
from app.models.request import QueryRequest
from app.services.llm_router import LLMRouter
from app.utils.auth import JWTAuthenticator
from app.core.container import get_jwt_authenticator
import httpx
from datetime import datetime

router = APIRouter()


@router.post("/query")
async def route_query(
    request_data: QueryRequest,
    #authorization: str = Header(...),
    #auth: JWTAuthenticator = Depends(get_jwt_authenticator),
    llm_router: LLMRouter = Depends(LLMRouter)
):
    #user_info = auth.verify_auth_header(authorization)

    # Scan input prompt for threats
    async with httpx.AsyncClient() as client:
        input_scan = await client.post(
            "http://detector:8002/detect",
            json={"input_text": request_data.prompt, "user_id": request_data.user_id}
        )
        input_threat = input_scan.json().get("threat_detected", False)

        # Log the prompt before LLM call
        await client.post("http://logger:8003/log", json={
            "user_id": request_data.user_id,
            "input_text": request_data.prompt,
            "output_text": "",
            "input_threat_detected": input_threat,
            "output_threat_detected": False,
            "timestamp": datetime.utcnow().isoformat()
        })
        if input_threat:
            return {
                "message": "Input prompt flagged as unsafe. Request blocked.",
                "input_threat_detected": True
            }, 403

    # Forward to LLM proxy and get response
    response = await llm_router.route_request(request_data)
    response["input_threat_detected"] = input_threat
    return response
