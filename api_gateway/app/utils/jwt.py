from fastapi import HTTPException, Header

async def verify_jwt(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        # Decode and validate here
        return {"user_id": "123"}  # placeholder
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
