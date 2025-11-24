from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.task import router as task_router
from app.api.routes.user import router as user_router

api_router = APIRouter()

# agrupando todas as rotas da API com prefixos e tags apropriadas
api_router.include_router(health_router, prefix="/health", tags=["Health"])
api_router.include_router(task_router, prefix="/tasks", tags=["Tasks"])
api_router.include_router(user_router, prefix="/users", tags=["Users"])