from fastapi import FastAPI
from app.api.routes import router
from prometheus_client import generate_latest, Counter
from flask import Response

REQUEST_COUNTER = Counter('http_requests_total', 'Total number of HTTP requests')

app = FastAPI(title="AI Threat Defense - API Gateway")
app.include_router(router, prefix="/api")

@app.before_request
def before_request():
    REQUEST_COUNTER.inc()

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')