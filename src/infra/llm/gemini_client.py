from google import genai
from dotenv import load_dotenv
from ...core.config.deppendencies import *
import os

load_dotenv()

client = genai.Client(api_key=os.getenv(GEMINI_API_KEY))