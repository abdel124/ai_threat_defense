from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Threat Defense - API Gateway")
app.include_router(router, prefix="/api")