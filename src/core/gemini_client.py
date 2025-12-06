from google import genai
from dotenv import load_dotenv
from .config import *
import os

load_dotenv()

client = genai.Client(api_key=os.getenv(GEMINI_API_KEY))

chat = client.chats.create(
    model=MODEL_NAME,
    history=[
        {
            "role": "user",
            "parts": [{
                "text": (
                    "Você é uma IA especializada em tecnologia, sua função é simplificar documentações de linguagens, frameworks e projetos de GitHub. "
                    "Você irá pegar o input da documentação ou projeto e vai fazer uma simplificação na resposta, usando analogias faceis para quem não entendeu ou nunca viu aquela documentação."
                    "Seu nome é Lib-AI. "
                    "Na primeira resposta, se apresente como Lib-IA. "
                    "Depois disso, não se apresente mais."
                )
            }]
        }
    ]
)