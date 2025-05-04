from fastapi import FastAPI
from pydantic import BaseModel
from detector.core.factory import get_detector

app = FastAPI()

class DetectionRequest(BaseModel):
    input_text: str
    user_id: str

@app.post("/detect")
async def detect_threat(req: DetectionRequest):
    detector = get_detector("default")
    result = detector.scan(req.input_text)
    return {"threat_detected": result}