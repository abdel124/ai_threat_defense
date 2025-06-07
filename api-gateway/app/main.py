from fastapi import FastAPI, Response
from app.api.routes import router
from prometheus_client import generate_latest, Counter, CONTENT_TYPE_LATEST

REQUEST_COUNTER = Counter('http_requests_total', 'Total number of HTTP requests')

app = FastAPI(title="AI Threat Defense - API Gateway")
app.include_router(router, prefix="/api")

@app.middleware("http")
async def count_requests(request, call_next):
    REQUEST_COUNTER.inc()
    return await call_next(request)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)