from fastapi import FastAPI, Request
from prometheus_client import generate_latest, Counter
from starlette.responses import Response
from app.api.routes import router

REQUEST_COUNTER = Counter('http_requests_total', 'Total number of HTTP requests')

app = FastAPI(title="AI Threat Defense - API Gateway")
app.include_router(router, prefix="/api")

@app.middleware("http")
async def count_requests(request: Request, call_next):
    REQUEST_COUNTER.inc()
    response = await call_next(request)
    return response

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")