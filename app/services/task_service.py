from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete

from app.models.task import Task as TaskModel
from app.schemas.task import TaskCreate, TaskUpdate


# Busca lista de tarefas com paginação
def get_tasks(
        db: Session,
        user_id: int,
        limit: int = 10,
        offset: int = 0
    ) -> List[TaskModel]:
        stmt = (
            select(TaskModel)
            .filter(TaskModel.owner_id == user_id)
            .offset(offset)
            .limit(limit).
            order_by(TaskModel.id)
        )   
        return db.execute(stmt).scalars().all()

# Busca uma tarefa por ID, garantindo que pertence ao usuário
def get_task(db: Session, task_id: int, user_id: int) -> Optional[TaskModel]:
    stmt = (
        select(TaskModel)
        .filter(TaskModel.id == task_id)
        .filter(TaskModel.owner_id == user_id)
    )
    return db.execute(stmt).scalar_one_or_none()

# Cria uma nova tarefa
def create_task(db: Session, task_data: TaskCreate, user_id: int) -> TaskModel:
    new_task = TaskModel(
        title=task_data.title,
        description=task_data.description,
        completed=task_data.completed,
        owner_id=user_id
    )
        
    db.add(new_task)
    db.commit()
    db.refresh(new_task) # Atualiza o objeto com dados do DB (ex: ID gerado)
    return new_task

# Atualiza uma tarefa existente
def update_task(db: Session, task_id: int, task_data: TaskUpdate, user_id: int) -> Optional[TaskModel]:
    updated_task = get_task(db, task_id, user_id)
    if not updated_task:
        return None
    
    update_data = task_data.model_dump(exclude_unset=True)

    for key, value in update_data.items(): # Atualiza apenas os campos fornecidos
        setattr(updated_task, key, value) # Define o atributo dinamicamente

    db.add(updated_task)
    db.commit()
    db.refresh(updated_task)
    return updated_task

# Deleta uma tarefa por ID
def delete_task(db: Session, task_id: int, user_id: int) -> bool:
    deleted_task = get_task(db, task_id, user_id)
    if not deleted_task:
        return False
    
    db.delete(deleted_task)
    db.commit()
    return True

