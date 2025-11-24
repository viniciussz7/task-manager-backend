from fastapi import APIRouter, HTTPException, Depends, status
from typing import List

from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.services.task_service import get_tasks, get_task, create_task, update_task, delete_task
from app.db.session import get_db
from app.core.jwt import get_current_user
from app.models.user import User

router = APIRouter()

security = HTTPBearer()

# Cada rota recebe uma sessão de banco de dados via dependência get_db, garantindo que cada requisição tenha seu próprio contexto de banco de dados.
# As operações de CRUD são delegadas aos serviços definidos em task_service.py, mantendo as rotas limpas e focadas na lógica de API.

# Rota para criar uma nova tarefa vinculada ao usuário autenticado
@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED, dependencies=[Depends(security)]) # response_model define o que a rota deve retornar — e valida isso com Pydantic.
def create(payload: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_task(db, payload, current_user.id)

# Rota para ler todas as tarefas do usuário autenticado com paginação
@router.get("/", response_model=List[Task], dependencies=[Depends(security)])
def read_all(limit: int = 10, offset: int = 0, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_tasks(db, current_user.id, limit=limit, offset=offset)

# Rota para ler uma tarefa específica do usuário autenticado
@router.get("/{task_id}", response_model=Task, dependencies=[Depends(security)])
def read_one(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = get_task(db, task_id, current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Rota para atualizar uma tarefa específica do usuário autenticado
@router.put("/{task_id}", response_model=Task, dependencies=[Depends(security)])
def put(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    updated = update_task(db, task_id, payload, current_user.id)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

# Rota para deletar uma tarefa específica do usuário autenticado
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(security)])
def remove(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    ok = delete_task(db, task_id, current_user.id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return
