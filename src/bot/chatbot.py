from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model="gemini-2.5-flash",
    history=[
        {
            "role": "user",
            "parts": [{
                "text": (
                    "Você é uma IA especializada em confeitaria. "
                    "Seu nome é Diolia. "
                    "Na primeira resposta, se apresente como Diolia. "
                    "Depois disso, não se apresente mais. "
                    "Nunca responda temas fora de confeitaria."
                )
            }]
        }
    ]
)

while True:
    msg = input("> ")
    if msg.lower() == "exit":
        break

    response_stream = chat.send_message_stream(
        msg,
        config={
            "temperature": 0.4,
            "top_p": 0.9,
            "top_k": 40,
            "max_output_tokens": 1000
        }
    )

    full_text = ""
    for chunk in response_stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            full_text += chunk.text
    print()