from fastapi import APIRouter, Depends, Request
from app.models.request import QueryRequest
from app.services.llm_router import LLMRouter

router = APIRouter()

@router.post("/query")
async def route_query(
    request_data: QueryRequest,
    llm_router: LLMRouter = Depends(LLMRouter)
):
    response = await llm_router.route_request(request_data)
    return response