from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

# conect_args é necessário para SQLite para usar mesma thread
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

# Cria o engine do SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args=connect_args, future=True)

# Cria uma fábrica de sessões
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False, future=True)

# Dependência para obter uma sessão de banco de dados para rotas FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()