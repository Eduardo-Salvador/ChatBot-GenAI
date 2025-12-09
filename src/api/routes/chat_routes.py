from fastapi import FastAPI
from ..dto.requests.chat_request import Input
from ...services.chat_service import process_message
from fastapi.responses import StreamingResponse

app = FastAPI(title="Lib-AI")
@app.post('/response')
def responses(dados:Input):
    return StreamingResponse(
        process_message(dados),
        media_type="text/plain"
    )