from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

criar_db()

app = FastAPI()


@app.post('/produtos')
def criar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
def listar_produtos():
    return {'Msg': 'Listagem de Produtos'}
