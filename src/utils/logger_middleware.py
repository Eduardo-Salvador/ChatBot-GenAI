import json
from fastapi import Request
from ..api.chatbot import app
from sys import stderr
from loguru import logger
import time

logger.remove()
logger.add(
    sink=stderr,
    format="<green>{time:DD/MM HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan> | {file}:{line}",
    level="INFO"
)

@app.middleware("http")
async def log_requests(request:Request, call_next):
    start = time.time()

    raw = await request.body()
    data = json.loads(raw.decode())
    msg = data.get("msg")

    logger.info(f"REQUEST: {msg}")

    response = await call_next(request)

    process_time = (time.time() - start) * 1000  
    
    logger.info(f"RESPONSE: {response.status_code} | {process_time:.2f}ms")
    return response