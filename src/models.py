from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Coletas(Base):
    __tablename__ = "coletas"

    id: Mapped[int] = mapped_column(primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(default=func.now())

    latitude: Mapped[float]
    longitude: Mapped[float]
    temperatura: Mapped[float]
    umidade: Mapped[float]
    velocidade_vento: Mapped[float]
    direcao_vento: Mapped[float]
