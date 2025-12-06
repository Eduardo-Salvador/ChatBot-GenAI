from fastapi import Request
from ..api.chatbot import app
from colorama import Fore
import logging

logging.basicConfig(
    level = logging.INFO,
    format =  "%(asctime)s -" + Fore.GREEN +" %(levelname)s:" + Fore.WHITE + "- %(message)s",
    datefmt ="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("Response LibAI")

@app.middleware("http")
async def log_requests(request:Request, call_next):
    body = await request.body()
    logger.info(f"Request: {request.method} {request.url} - Body: {body.decode()}")

    response = await call_next(request)
    
    logger.info(f"Response: status_code={response.status_code}")
    return response