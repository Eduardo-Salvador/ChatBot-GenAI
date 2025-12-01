from google import genai
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from src.bot.input import Input

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model="gemini-2.5-flash",
    history=[
        {
            "role": "user",
            "parts": [{
                "text": (
                    "Você é uma IA especializada em tecnologia. "
                    "Seu nome é Lib-AI. "
                    "Na primeira resposta, se apresente como Lib-IA. "
                    "Depois disso, não se apresente mais. "
                    "Nunca responda temas fora de tecnologia."
                )
            }]
        }
    ]
)

app = FastAPI() #Crio o Objeto app, que vai receber todas as rotas HTTPS
@app.post('/response')
def responses(dados:Input):
    response_stream = chat.send_message(
            dados.msg,
            config={
                "temperature": 0.4,
                "top_p": 0.9,
                "top_k": 40,
                "max_output_tokens": 1000
            }
        )
    return response_stream.text

#@app.get('/lib_ai')
    