from fastapi import FastAPI
from ..model.input import Input
from ..core.processor import process_message

app = FastAPI(title="Lib-AI")
@app.post('/response')
def responses(dados:Input) -> str:
    return process_message(dados)