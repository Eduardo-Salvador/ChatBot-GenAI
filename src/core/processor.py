from .gemini_client import chat
from ..model.input import Input
from .config import *

def process_message(dados: Input) -> str:
    """
    :param dados: Description
    :type dados: Input
    :return: Description
    :rtype: str
    """
    response = chat.send_message(
        dados.msg,
        config={
            "temperature": DEFAULT_TEMPERATURE,
            "top_p": DEFAULT_TOKENS_PERCENTAGE,
            "top_k": DEFAULT_WORDS_USE,
            "max_output_tokens": DEFAULT_OUTPUT_TOKENS
        }
    )
    return response.text