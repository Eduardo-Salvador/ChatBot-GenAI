from fastapi import HTTPException
from fastapi.responses import StreamingResponse
from ..dto.requests.chat_request import ChatRequest
from ...services.chat_service import ChatService

class ChatController:
    """
    Controller de chat.
    
    Responsabilidade:
    - Receber requisições HTTP
    - Validar dados de entrada
    - Chamar service apropriado
    - Retornar resposta HTTP
    """
    
    def __init__(self, chat_service: ChatService):
        """
        Injeta o service no controller.
        Controller não cria service, recebe pronto.
        """
        self.chat_service = chat_service
    
    async def send_message(self, request: ChatRequest) -> StreamingResponse:
        """
        Processa mensagem do usuário e retorna resposta em streaming.
        
        Args:
            request: Dados da requisição (mensagem do usuário)
            
        Returns:
            StreamingResponse com texto da IA
            
        Raises:
            HTTPException: Se houver erro no processamento
        """
        try:
            # Valida se mensagem não está vazia (já validado pelo Pydantic, mas double check)
            if not request.message.strip():
                raise HTTPException(
                    status_code=400,
                    detail="Message cannot be empty"
                )
            
            # Chama service que retorna generator
            stream = self.chat_service.process_message(
                message=request.message,
                user_id=request.user_id
            )
            
            # Retorna streaming response
            return StreamingResponse(
                stream,
                media_type="text/plain"
            )
            
        except ValueError as e:
            # Erro de validação
            raise HTTPException(status_code=400, detail=str(e))
        
        except Exception as e:
            # Erro inesperado
            raise HTTPException(
                status_code=500,
                detail=f"Internal error: {str(e)}"
            )