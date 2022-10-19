from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.schemas.schemas import Produto, ProdutoSimples, Usuario
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario

# criar_db()

app = FastAPI()


# PRODUTOS

@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[ProdutoSimples])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


# USUARIOS

@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado


@app.get('/usuarios')
def listar_usuario(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios
