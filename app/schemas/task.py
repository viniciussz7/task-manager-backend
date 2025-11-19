from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Schema base para tarefas
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    completed: bool = False

class TaskCreate(TaskBase):
    """Schema para criação de tarefas. Herda de TaskBase."""
    pass

class TaskUpdate(BaseModel):
    """Schema usado para atualizações parciais de tarefas."""
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None
    completed: Optional[bool] = None

class Task(TaskBase):
    """Schema para leitura de tarefas, incluindo ID e timestamps."""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True # Permite conversão automática de objetos ORM para Pydantic
