from fastapi import FastAPI
from pydantic import BaseModel
import json
from datetime import datetime

app = FastAPI()

class LogEntry(BaseModel):
    user_id: str
    input_text: str
    output_text: str
    input_threat_detected: bool
    output_threat_detected: bool
    timestamp: str

@app.post("/log")
async def log_entry(entry: LogEntry):
    log_record = entry.dict()
    log_line = json.dumps(log_record)
    with open("logs.jsonl", "a") as f:
        f.write(log_line + "\n")
    return {"status": "logged"}