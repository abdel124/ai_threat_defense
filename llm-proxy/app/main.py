from fastapi import FastAPI
from pydantic import BaseModel
from app.core.factory import get_llm_backend

app = FastAPI()

class LLMQuery(BaseModel):
    prompt: str
    model: str

@app.post("/query")
async def query_llm(req: LLMQuery):
    llm_client = get_llm_backend(req.model.lower())
    result = await llm_client.query(req.prompt)
    return {"response": result}