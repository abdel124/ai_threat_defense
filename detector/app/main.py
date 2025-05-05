from fastapi import FastAPI
from pydantic import BaseModel
from app.core.factory import get_detector

app = FastAPI()

class DetectionRequest(BaseModel):
    input_text: str
    user_id: str

@app.post("/detect")
async def detect_threat(req: DetectionRequest):
    detector = get_detector("default")
    print(req.input_text)
    result = detector.scan(req.input_text)
    return {"threat_detected": result}