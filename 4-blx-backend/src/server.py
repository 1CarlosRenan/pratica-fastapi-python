from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_auth, rotas_produto, rotas_pedidos

app = FastAPI()

# CORS
origins = ['http://localhost:3000', 'https://myapp.vercel.com']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Rotas de PRODUTOS
app.include_router(rotas_produto.router)

# Rotas de SEGURANÇA: Autenticação e Autorização
app.include_router(rotas_auth.router, prefix="/auth")

# Rotas de PEDIDOS
app.include_router(rotas_pedidos.router)
