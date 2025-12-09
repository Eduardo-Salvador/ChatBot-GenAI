# core/config/settings.py

import os
from dotenv import load_dotenv

# ========================================
# CARREGA VARIÁVEIS DE AMBIENTE
# ========================================

# Carrega arquivo .env (se existir)
# .env é onde você guarda informações sensíveis (API keys, senhas)
load_dotenv()

# ========================================
# SEÇÃO 1: API KEYS (informações sensíveis)
# ========================================

# Pega a chave da API do Gemini do arquivo .env
# os.getenv("NOME") busca a variável de ambiente
# Se não encontrar, retorna None
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Você pode adicionar outras chaves aqui
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # para quando adicionar OpenAI
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")  # com valor padrão
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

# ========================================
# SEÇÃO 2: CONFIGURAÇÕES DO MODELO LLM
# ========================================

# Temperatura: controla "criatividade" da IA
# Valores: 0.0 (muito conservadora) a 1.0 (muito criativa)
# 0.4 = equilibrado, respostas consistentes mas não robóticas
DEFAULT_TEMPERATURE = 0.4

# Top P: controla diversidade das palavras escolhidas
# 0.9 = considera 90% das palavras mais prováveis
# Valor entre 0.0 e 1.0
DEFAULT_TOKENS_PERCENTAGE = 0.9  # também chamado de "top_p"

# Top K: quantas palavras candidatas considerar
# 40 = olha as 40 palavras mais prováveis em cada passo
# Valor inteiro (ex: 20, 40, 100)
DEFAULT_WORDS_USE = 40  # também chamado de "top_k"

# Max output tokens: limite de tokens na resposta
# 2000 tokens ≈ 1500 palavras (aproximadamente)
# Evita respostas muito longas (e caras)
DEFAULT_OUTPUT_TOKENS = 2000

# ========================================
# SEÇÃO 3: NOME DO MODELO
# ========================================

# Nome do modelo Gemini a usar
# "gemini-2.0-flash-exp" = versão experimental mais rápida
MODEL_NAME = "gemini-2.0-flash-exp"

# ========================================
# SEÇÃO 4: PROMPT DE SISTEMA (Personalidade)
# ========================================

# System prompt: define como a IA deve se comportar
# É enviado em TODA conversa (invisível para usuário)
SYSTEM_PROMPT = (
    "You are a technology-specialized AI; your role is to simplify documentation "
    "for languages, frameworks, and GitHub projects. "
    "You will take the input from the documentation or project and simplify the answer "
    "using easy analogies for those who didn't understand or have never seen that documentation. "
    "Your name is Lib-AI. "
    "In your first response, introduce yourself as Lib-AI. "
    "After that, don't introduce yourself again."
)

# Você tinha "PERSUA", mas o nome correto seria SYSTEM_PROMPT ou PERSONA
# PERSUA parece typo de "PERSONA" ou "PERSUASION"

# ========================================
# SEÇÃO 5: CONFIGURAÇÕES DO BANCO DE DADOS
# (para quando adicionar PostgreSQL)
# ========================================

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@localhost:5432/libai_db"  # valor padrão
)

# ========================================
# SEÇÃO 6: CONFIGURAÇÕES DA APLICAÇÃO
# ========================================

# Ambiente (development, production)
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Habilitar debug (só em dev)
DEBUG = ENVIRONMENT == "development"

# Host e porta do servidor
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))

# ========================================
# SEÇÃO 7: LIMITES E CONSTRAINTS
# ========================================

# Tamanho máximo de mensagem do usuário (caracteres)
MAX_MESSAGE_LENGTH = 10000

# Tamanho mínimo de mensagem
MIN_MESSAGE_LENGTH = 1

# Número máximo de mensagens no histórico
MAX_HISTORY_MESSAGES = 50

# ========================================
# VALIDAÇÃO (garante que tem o que precisa)
# ========================================

def validate_settings():
    """
    Valida se todas configurações obrigatórias estão presentes.
    Levanta erro se algo estiver faltando.
    """
    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY não encontrada! "
            "Crie arquivo .env com: GEMINI_API_KEY=sua_chave_aqui"
        )
    
    print(f"✅ Configurações carregadas com sucesso!")
    print(f"   Ambiente: {ENVIRONMENT}")
    print(f"   Modelo: {MODEL_NAME}")
    print(f"   Debug: {DEBUG}")

# Chama validação ao importar settings
validate_settings()