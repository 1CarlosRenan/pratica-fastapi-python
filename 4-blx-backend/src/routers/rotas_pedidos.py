from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Pedido, ProdutoSimples

router = APIRouter()


@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, session: Session = Depends(get_db)):
    pass


@router.get('/pedidos/{id}', response_model=ProdutoSimples)
def exibir_pedido(id: int, session: Session = Depends(get_db)):
    pass


@router.get('/pedidos', response_model=List[Pedido])
def listar_pedidos(session: Session = Depends(get_db)):
    pass
