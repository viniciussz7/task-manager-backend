from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Base servirá como a classe base para todos os modelos ORM e por Alembic para gerar migrações