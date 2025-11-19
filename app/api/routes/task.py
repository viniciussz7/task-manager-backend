from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime

from app.schemas.task import Task, TaskCreate, TaskUpdate

router = APIRouter()

# Simulação de um banco de dados em memória
fake_db = []
current_id = 1


@router.post("/", response_model=Task) # response_model define o que a rota deve retornar — e valida isso com Pydantic.
def crate_task(payload: TaskCreate):
    global current_id

    new_task = Task(
        id=current_id,
        title=payload.title,
        description=payload.description,
        completed=payload.completed,
        created_at=datetime.utcnow()
    )

    current_id += 1
    fake_db.append(new_task)
    
    return new_task

@router.get("/", response_model=List[Task])
def list_tasks(limit: int = 10, offset: int = 0): # Paginação simples em memória
    return fake_db[offset: offset + limit]

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in fake_db:
        if task.id == task_id:
            return task
        
@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate):
    # 1. Encontrar a tarefa no "banco"
    for index, task in enumerate(fake_db):
        if task.id == task_id:

            # 2. Converter o Task para dict
            task_data = task.model_dump()

            # 3. Atualizar somente campos enviados no payload
            update_data = payload.model_dump(exclude_unset=True)

            # 4. Atualizar o dicionário da tarefa
            updated_task = Task(**task_data, **update_data)

            # 5. Salvar de volta no "banco"
            fake_db[index] = updated_task

            return updated_task

    # Se não achar o id
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(fake_db):
        if task.id == task_id:
            del fake_db[index] # deletar a tarefa
            return # 204 No Content
    
    raise HTTPException(status_code=404, detail="Task not found")