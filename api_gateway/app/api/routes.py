from app.utils.auth import JWTAuthenticator
from fastapi import Header

@router.post("/query")
async def route_query(
    request_data: QueryRequest,
    authorization: str = Header(...),
    auth: JWTAuthenticator = Depends(get_jwt_authenticator),
    llm_router: LLMRouter = Depends(LLMRouter)
):
    user_info = auth.verify_auth_header(authorization)
    print("Verified user:", user_info)
    return await llm_router.route_request(request_data)
