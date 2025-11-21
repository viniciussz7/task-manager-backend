from pydantic_settings import BaseSettings

class Settings(BaseSettings): # lê automaticamente variáveis de ambiente.
    """Configurações principais da aplicação."""
    APP_NAME: str = "Task Manager API"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"  # Pode ser 'development', 'production', etc.

    DATABASE_URL: str = "sqlite:///./app.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()