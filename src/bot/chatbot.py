from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=input("> "),
    config = { 
        "temperature": 0.3, 
        "top_p": 0.9, 
        "top_k": 40, 
        "max_output_tokens": 4800 
        }
    )
print(response.text)