from google import genai
from dotenv import load_dotenv
from .config import *
import os

"""
Criação do cliente Gemini

Função para enviar mensagens cruas para o modelo

Tratamento de exceptions

Configuração da personalidade da IA (persua)

Lidar com o histórico se for no client
Isso faz sentido porque:

Esse módulo é de integração externa.
É onde você cria e controla o acesso à API do Gemini.
"""

load_dotenv()

client = genai.Client(api_key=os.getenv(GEMINI_API_KEY))

chat = client.chats.create(
    model=MODEL_NAME,
    history=[
        {
            "role": "user",
            "parts": [{
                "text": (
                    "Você é uma IA especializada em tecnologia. "
                    "Seu nome é Lib-AI. "
                    "Na primeira resposta, se apresente como Lib-IA. "
                    "Depois disso, não se apresente mais."
                )
            }]
        }
    ]
)