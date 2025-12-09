# api/routes/chat_routes.py
from fastapi import APIRouter, Depends
from ..controllers.chat_controller import ChatController
from ..dto.requests.chat_request import ChatRequest
from ...core.config.deppendencies import get_chat_controller

# Cria router (NÃO cria app aqui!)
router = APIRouter(
    prefix="/chat",  # todas rotas começam com /chat
    tags=["chat"]    # tag para documentação
)

@router.post("/message")
async def send_message(
    request: ChatRequest,
    controller: ChatController = Depends(get_chat_controller)
):
    """
    Endpoint para enviar mensagem e receber resposta em streaming.
    
    - **message**: Mensagem do usuário (obrigatório)
    - **user_id**: ID do usuário (opcional)
    
    Retorna streaming de texto conforme IA gera resposta.
    """
    return await controller.send_message(request)