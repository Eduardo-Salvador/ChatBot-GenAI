from pydantic import BaseModel
"""
Modelos de entrada

Tipos esperados nas rotas

Ex.: MensagemInput, UsuarioInput, ChatCompletionRequest

Você pode acrescentar:

Message

ChatHistory

User

ConfigOverrides

Tudo organizado e sem poluir as rotas."""


class Input(BaseModel):
    msg:str