# core/config/dependencies.py

from functools import lru_cache
from fastapi import Depends 
from ..config.settings import (
    GEMINI_API_KEY,
    MODEL_NAME,
    DEFAULT_TEMPERATURE,
    DEFAULT_TOKENS_PERCENTAGE,
    DEFAULT_WORDS_USE,
    DEFAULT_OUTPUT_TOKENS,
    SYSTEM_PROMPT
)

# ========================================
# IMPORTS DAS CAMADAS
# ========================================

# Infra (implementações técnicas)
from ...infra.llm.gemini_client import GeminiClient

# Services (orquestradores)
from ...services.chat_service import ChatService

# Controllers (recebem requests)
from ...api.controllers.chat_controller import ChatController

# ========================================
# FUNÇÃO 1: Criar Client do Gemini
# ========================================

@lru_cache()  # Cria só uma vez, reutiliza sempre
def get_gemini_client() -> GeminiClient:
    """
    Cria e retorna client do Gemini.
    
    @lru_cache garante que só cria UMA VEZ.
    Todas chamadas futuras retornam a mesma instância.
    
    Returns:
        GeminiClient configurado e pronto para usar
    """
    return GeminiClient(
        api_key=GEMINI_API_KEY,
        model_name=MODEL_NAME,
        temperature=DEFAULT_TEMPERATURE,
        top_p=DEFAULT_TOKENS_PERCENTAGE,
        top_k=DEFAULT_WORDS_USE,
        max_output_tokens=DEFAULT_OUTPUT_TOKENS
    )

# ========================================
# FUNÇÃO 2: Criar Chat Service
# ========================================

def get_chat_service(
    gemini_client: GeminiClient = Depends(get_gemini_client)
) -> ChatService:
    """
    Cria e retorna Chat Service.
    
    Depends(get_gemini_client) diz:
    "FastAPI, chame get_gemini_client() primeiro e me dê o resultado"
    
    Args:
        gemini_client: Client do Gemini (injetado automaticamente)
        
    Returns:
        ChatService configurado
    """
    return ChatService(
        llm_client=gemini_client,
        system_prompt=SYSTEM_PROMPT
    )

# ========================================
# FUNÇÃO 3: Criar Chat Controller
# ========================================

def get_chat_controller(
    chat_service: ChatService = Depends(get_chat_service)
) -> ChatController:
    """
    Cria e retorna Chat Controller.
    
    Depends(get_chat_service) diz:
    "FastAPI, chame get_chat_service() primeiro e me dê o resultado"
    
    Args:
        chat_service: Service de chat (injetado automaticamente)
        
    Returns:
        ChatController configurado
    """
    return ChatController(chat_service=chat_service)

# ========================================
# EXPLICAÇÃO DO FLUXO DE INJEÇÃO
# ========================================

"""
Quando você usa na rota:

@router.post("/message")
def send_message(
    controller: ChatController = Depends(get_chat_controller)
):
    ...

O FastAPI faz automaticamente:

1. Chama get_chat_controller()
   ↓
2. Vê que precisa de ChatService, chama get_chat_service()
   ↓
3. Vê que precisa de GeminiClient, chama get_gemini_client()
   ↓
4. Cria GeminiClient (uma vez só, @lru_cache)
   ↓
5. Cria ChatService com GeminiClient
   ↓
6. Cria ChatController com ChatService
   ↓
7. Injeta ChatController na sua rota

TUDO AUTOMÁTICO! Você não cria nada manualmente.
"""