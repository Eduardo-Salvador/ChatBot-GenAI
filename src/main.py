# src/main.py
from fastapi import FastAPI
from api.routes import chat_routes
from core.config.settings import settings

# Cria aplicação aqui (raiz)
app = FastAPI(
    title="Lib-AI",
    description="API de chat com IA e RAG",
    version="1.0.0"
)

# Registra routers
app.include_router(chat_routes.router)

# Rota de health check
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Iniciar servidor (quando rodar python main.py)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )