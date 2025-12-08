from fastapi import FastAPI
from ..model.input import Input
from ..core.processor import process_message
from fastapi.responses import StreamingResponse

app = FastAPI(title="Lib-AI")
@app.post('/response')
def responses(dados:Input):
    return StreamingResponse(
        process_message(dados),
        media_type="text/plain"
    )