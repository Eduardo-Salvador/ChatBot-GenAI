from .gemini_client import client
from ..model.input import Input
from .config import *

def process_message(dados: Input):
    messages = [
        {
            "role": "user",
            "parts": [{"text": PERSUA}]
        }
    ]

    messages.append({"role": "user", "parts": [{"text": dados.msg}]})

    stream = client.models.generate_content_stream(
        model=MODEL_NAME,
        contents=messages,
        config={
            "temperature": DEFAULT_TEMPERATURE,
            "top_p": DEFAULT_TOKENS_PERCENTAGE,
            "top_k": DEFAULT_WORDS_USE,
            "max_output_tokens": DEFAULT_OUTPUT_TOKENS
        }
    )
    for chunk in stream:
        if chunk.text:
            yield chunk.text

    messages.append({"role": "model", "parts": [{"text": chunk.text}]})