from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"mensagem": "Olá, mundo!"}

@app.get("/itens/{item_id}")
async def read_item(item_id: int, q: Optional [str] | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/soma")
async def soma(a: int, b: int):
    return {"resultado": a + b}

@app.get("/adicao/{a}/{b}")
async def adicao(a: int, b: int):
    return {"resultado": a + b}

# Crie uma rota que retorne a soma de dois numeros passados por caminho (path de url)

# extra: melhore a tipagem do codigo usando tipos do modulo typing onde for necessário