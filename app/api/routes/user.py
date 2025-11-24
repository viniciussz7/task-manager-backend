from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from app.core.jwt import create_access_token, get_current_user
from app.db.session import get_db
from app.schemas.user import TokenResponse, UserCreate, UserRead, UserLogin
from app.services.user_service import create_user, get_user_by_email
from app.core.security import verify_password


router = APIRouter()

security = HTTPBearer()

# rota para criar um novo usuário
@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)) -> UserRead:
    """Registra um novo usuário."""

     # DEBUG TEMPORÁRIO
    print("DEBUG >>> password:", user_data.password, type(user_data.password))
          
    try:
        new_user = create_user(db, user_data)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    

# rota para login do usuário
@router.post("/login", response_model=TokenResponse)
def login_user(user_data: UserLogin, db: Session = Depends(get_db)) -> UserRead:
    """Faz login do usuário e retorna os dados do usuário se bem-sucedido."""
    user = get_user_by_email(db, user_data.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário nao encontrado"
        ) 
    
    if not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos."
        )
    
    access_token = create_access_token({"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# rota para buscar usuário pelo email
@router.get("/by-email/{email}", response_model=UserRead)
def get_user(email: str, db: Session = Depends(get_db)) -> UserRead:
    """Busca um usuário pelo email."""
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário nao encontrado"
        )
    return user

# rota protegida para obter dados do usuário logado
@router.get("/me", response_model=UserRead, dependencies=[Depends(security)])
def get_logged_user(current_user: UserRead = Depends(get_current_user)) -> UserRead:
    """Retorna os dados do usuário logado."""
    return current_user