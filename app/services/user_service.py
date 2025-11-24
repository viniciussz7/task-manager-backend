from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password


def get_user_by_email(db: Session, email: str) -> User | None:
    """Busca um usuário pelo email se exisitr."""
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int) -> User | None:
    """Busca um usuário pelo ID se existir."""
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user_data: UserCreate) -> User:
    """Cria um novo usuário no banco de dados."""
    
    # Verifica se o email já está em uso
    existin_user = get_user_by_email(db, user_data.email)
    if existin_user:
        raise ValueError("Usuário com esse email já existe.")
    
    # Cria hash da senha
    hashed = hash_password(user_data.password)

    # Cria instância do modelo User
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed
    )

    # Adiciona e comita o novo usuário no banco
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Atualiza o objeto com dados do DB

    return new_user 

