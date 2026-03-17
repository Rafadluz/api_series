from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.serie import SerieModel
from app.schema.serie import SerieSchema

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/series")
async def listar_serie(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()

@serie.put("/series/{id}/update")
async def atualizar_serie(id: int, dados: SerieSchema, db: Session = Depends(get_db)):
    serie_existente = db.query(SerieModel).filter(SerieModel.id == id).first()
    if not serie_existente:
        return {"mensagem": "Série não encontrada"}
    for campo, valor in dados.model_dump().items():
        setattr(serie_existente, campo, valor)
    db.commit()
    db.refresh(serie_existente)
    return serie_existente
