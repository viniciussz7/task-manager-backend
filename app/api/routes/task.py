from fastapi import APIRouter, HTTPException, Depends, status
from typing import List

from sqlalchemy.orm import Session

from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.services.task_service import get_tasks, get_task, create_task, update_task, delete_task
from app.db.session import get_db

router = APIRouter()

# Cada rota recebe uma sessão de banco de dados via dependência get_db, garantindo que cada requisição tenha seu próprio contexto de banco de dados.
# As operações de CRUD são delegadas aos serviços definidos em task_service.py, mantendo as rotas limpas e focadas na lógica de API.

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED) # response_model define o que a rota deve retornar — e valida isso com Pydantic.
def create(payload: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, payload)


@router.get("/", response_model=List[Task])
def read_all(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    return get_tasks(db, limit=limit, offset=offset)


@router.get("/{task_id}", response_model=Task)
def read_one(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=Task)
def put(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    updated = update_task(db, task_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(task_id: int, db: Session = Depends(get_db)):
    ok = delete_task(db, task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return
