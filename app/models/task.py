from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks" # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


# se futuramente ligar com User:
# owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
# owner = relationship("User", back_populates="tasks")