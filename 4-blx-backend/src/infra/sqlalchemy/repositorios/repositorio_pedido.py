from sqlalchemy.orm import Session
from typing import List
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioPedido():

    def __init__(self, session: Session) -> None:
        self.session = session

    def gravar_pedido(self, pedido: schemas.Pedido) -> models.Pedido:
        pedido_db = models.Pedido(quantidade=pedido.quantidade,
                                  local_entrega=pedido.local_entrega,
                                  tipo_entrega=pedido.tipo_entrega,
                                  observacao=pedido.observacao,
                                  usuario_id=pedido.usuario_id,
                                  produto_id=pedido.produto_id
                                  )

        self.session.add(pedido_db)
        self.session.commit()
        self.session.refresh(pedido_db)

        return pedido_db

    def buscar_por_id(self, usuario_id: int) -> models.Pedido:
        pass

    def listar_meus_pedidos_por_usuario_id(self, usuario_id: int) -> List[models.Pedido]:
        pass

    def listar_minhas_vendas_por_usuario_id(self, usuario_id: int) -> List[models.Pedido]:
        pass
