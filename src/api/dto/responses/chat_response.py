from pydantic import BaseModel #Biblioteca para criar Classes de forma mais pratica.
from typing import List #Boa pratica para obrigar um tipo (Python tem tipagem dinamica)

class ChatResponse(BaseModel):
    message: str #Mensagem que a LLM ira mandar
    sources: List[str] | None = None  #Recebe uma lista de fontes (Rags ou ML propio), ou None (valor padrao) caso nao aplicavel
    timestamp: str #Data e hora da resposta para Logs futuros

"""
DTO de Saida:
Mensagem: SAIDA
Fontes: RAG OU ML
Time: DATA E HORA DA SAIDA (LOGS)
"""