from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

criar_db()

app = FastAPI()


@app.post('/produtos', status_code=status.HTTP_201_CREATED)
def criar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos', status_code=status.HTTP_200_OK)
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos
