from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete

from app.models.task import Task as TaskModel
from app.schemas.task import TaskCreate, TaskUpdate


# Busca lista de tarefas com paginação
def get_tasks(db: Session, limit: int = 10, offset: int = 0) -> List[TaskModel]:
    stmt = select(TaskModel).offset(offset).limit(limit).order_by(TaskModel.id)
    result = db.execute(stmt).scalars().all()
    return result

# Busca uma tarefa por ID
def get_task(db: Session, task_id: int) -> Optional[TaskModel]:
    return db.get(TaskModel, task_id) # Usa o método get para buscar por chave primária

# Cria uma nova tarefa
def create_task(db: Session, task_in: TaskCreate) -> TaskModel:
    db_obj = TaskModel(
        title=task_in.title,
        description=task_in.description,
        completed=task_in.completed)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj) # Atualiza o objeto com dados do DB (ex: ID gerado)
    return db_obj

# Atualiza uma tarefa existente
def update_task(db: Session, task_id: int, task_in: TaskUpdate) -> Optional[TaskModel]:
    db_obj = db.get(TaskModel, task_id)
    if not db_obj:
        return None
    
    update_data = task_in.model_dump(exclude_unset=True)
    for key, value in update_data.items(): # Atualiza apenas os campos fornecidos
        setattr(db_obj, key, value) # Define o atributo dinamicamente
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# Deleta uma tarefa por ID
def delete_task(db: Session, task_id: int) -> bool:
    db_obj = db.get(TaskModel, task_id)
    if not db_obj:
        return False
    db.delete(db_obj)
    db.commit()
    return True

