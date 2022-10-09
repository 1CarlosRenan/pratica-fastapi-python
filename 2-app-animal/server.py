from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4, UUID

app = FastAPI()


class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str


# Simulando um banco de dados
banco: List[Animal] = []


@app.get('/animais')
def listar_animais():
    return banco

# UUID dá o tipo ao animal_id


@app.get('/animais/{animal_id}')
def obter_animal(animal_id: UUID):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return {'error': 'Animal não localizado'}


@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str):
    posicao = -1
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {'mensagem': 'Animal removido com sucesso'}
    else:
        return {'error': 'Animal não localizado'}


@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = uuid4()  # sem o UUID, usar str()
    banco.append(animal)
    return None
