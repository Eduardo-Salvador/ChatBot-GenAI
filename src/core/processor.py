from .gemini_client import chat
from ..model.input import Input
from .config import *

"""

Lógica do chat

Construção do prompt/histórico

Chamadas para gemini_client

Regras simples de fluxo

Ajustes de temperatura (caso venha do request)

Processamento das respostas

O processor é o “cérebro” da sua aplicação, mas não contém regras de negócio do domínio.

Ele só traduz pedido → LLM → resposta."""

def process_message(dados: Input) -> str:
    """
    Docstring for process_message
    
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