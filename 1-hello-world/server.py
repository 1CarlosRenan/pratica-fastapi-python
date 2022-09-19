from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/") # decorator
async def home():
    return {"mensagem": "Olá, FastAPI"}


@app.get("/saudacao/{nome}") # decorator
async def saudar(nome: str):
    texto = f'Olá, {nome}! Tudo bem?'
    return {"mensagem": texto}


@app.get("/dobro") # decorator
async def dobro(valor: int):
    resultado = 2 * valor
    return {"resultado": f'O dobro de {valor} é {resultado}'}


@app.get('/area-retangulo') # decorator
async def area_retangulo(largura: int, altura: int = 1):
    area = largura * altura
    return {'area': area}


class Produto(BaseModel):
    nome: str
    valor: float


@app.post('/produtos') # decorator
def produtos(produto: Produto):
    return {'mensagem': 'Produto (Espetinho) cadastrado com sucesso!'}
