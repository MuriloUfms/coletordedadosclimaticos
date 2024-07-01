from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class SubscriberSchema(BaseModel):
    email: EmailStr = Field(..., description='Email do inscrito')
    interval_in_hours: int = Field(24, description='Intervalo de envio em horas')


class UnsubscribeRequest(BaseModel):
    email: EmailStr = Field(..., description='Email do inscrito')


class SubscribeResponse(BaseModel):
    message: str = Field(..., description='Mensagem de sucesso')


class ColetaRequest(BaseModel):
    latitude: float = Field(
        ..., example=-20.5026554, description='Latitude da localização'
    )
    longitude: float = Field(
        ..., example=-54.6154765, description='Longitude da localização'
    )


class ColetaResponse(BaseModel):
    id: int = Field(..., description='ID da coleta')
    temperatura: float = Field(..., description='Temperatura em graus Celsius')
    umidade: float = Field(..., description='Umidade relativa do ar em %')
    velocidade_vento: float = Field(..., description='Velocidade do vento em m/s')
    direcao_vento: float = Field(..., description='Direção do vento em graus')
    timestamp: datetime = Field(..., description='Data e hora da coleta UTC')
