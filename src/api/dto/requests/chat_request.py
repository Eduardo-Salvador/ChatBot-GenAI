from pydantic import BaseModel, Field
'''
Pydantic:
Biblioteca Python para validação de dados
Integrada ao FastAPI
Valida automaticamente tipos, limites, formatos
'''

class ChatRequest(BaseModel): #Classe base do Pydantic -> Todos DTOs Herdam ela
    message: str = Field( #Funcao para validacoes extras (Uma string com regras)
        ...,  #Mensagem eh obrigatoria, rejeita se nao enviar nada, (min 1)
        min_length=1,
        max_length=10000,  #Protege meus tokens
        description="User message" #Aparece no swagger apenas (Doc autoimatica)
    )
    user_id: str | None = Field( #Recebe com ID do Usuario ou Nao
        None, 
        description="User ID (Optional)"
    )

"""
DTO ChatRequest:
recebe uma mensagem: obrigatorio com Field aplicando filtros (obrigatorio).
recebe um user_id: que pode ser None.
"""