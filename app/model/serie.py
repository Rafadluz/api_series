from sqlalchemy import Column, Integer, String
from app.database import Base

class SerieModel(Base):
    __tablename__ = "serie"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(255))
    ano_lancamento = Column(Integer)