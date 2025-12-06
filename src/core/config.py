'''
Variáveis de ambiente

Configs carregadas do .env

Configs de modelo (temperature padrão, top_p, etc)

Nome do modelo Gemini a ser usado

Se usa streaming ou não

Versão da API

Configs globais do app
'''

import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"
DEFAULT_TEMPERATURE = 0.4
DEFAULT_TOKENS_PERCENTAGE = 0.9
DEFAULT_WORDS_USE: 40
DEFAULT_OUTPUT_TOKENS: 2000
