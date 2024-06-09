from datetime import datetime

from pydantic import BaseModel, Field


class ColetaBase(BaseModel):
    latitude: float = Field(
        ..., example=-20.5026554, description="Latitude da localização"
    )
    longitude: float = Field(
        ..., example=-54.6154765, description="Longitude da localização"
    )


class ColetaRequest(ColetaBase):
    pass


class ColetaResponse(BaseModel):
    id: int = Field(..., description="ID da coleta")
    temperatura: float = Field(..., description="Temperatura em graus Celsius")
    umidade: float = Field(..., description="Umidade relativa do ar em %")
    velocidade_vento: float = Field(..., description="Velocidade do vento em m/s")
    direcao_vento: float = Field(..., description="Direção do vento em graus")
    timestamp: datetime = Field(..., description="Data e hora da coleta UTC")
