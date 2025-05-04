from fastapi import APIRouter, Depends, Header
from app.models.request import QueryRequest
from app.services.llm_router import LLMRouter
from app.utils.auth import JWTAuthenticator
from app.core.container import get_jwt_authenticator

router = APIRouter()

@router.post("/query")
async def route_query(
    request_data: QueryRequest,
    authorization: str = Header(...),
    auth: JWTAuthenticator = Depends(get_jwt_authenticator),
    llm_router: LLMRouter = Depends(LLMRouter)
):
    user_info = auth.verify_auth_header(authorization)
    return await llm_router.route_request(request_data)