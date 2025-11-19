from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_router import api_router
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="API para gereciamento de tarefas.",
    )
    
    @app.get("/")
    def root():
        return {
            "message": f"{settings.APP_NAME} - up and running!",
            "version": settings.APP_VERSION,
        }
    
    app.include_router(api_router)

    return app

app = create_app()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # restringir em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


