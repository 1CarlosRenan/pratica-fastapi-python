from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.schemas.schemas import Usuario


router = APIRouter()


@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado


@router.get('/usuarios', response_model=List[Usuario])
def listar_usuario(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios
