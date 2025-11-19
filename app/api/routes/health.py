from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    """Rota de verificação de saúde da API."""
    return {"ping": "pong"}

# Permite monitoramento simples (/health/ping) e checagens por orquestradores ou serviços de deploy.