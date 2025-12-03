from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Centraliza todas as configurações da aplicação.
    Valores sensíveis devem ser definidos APENAS no arquivo .env.
    """

    # Informações da aplicação
    APP_NAME: str = "Task Manager API"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"  # Ou "production"

    # Banco de Dados
    DATABASE_URL: str  # Obrigatório no .env

    # JWT / Segurança
    SECRET_KEY: str  # Obrigatório no .env
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 horas por padrão

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
