from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_produtos, rotas_usuario

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
app.include_router(rotas_produtos.router)

# Rotas de USUARIOS
app.include_router(rotas_usuario.router)
