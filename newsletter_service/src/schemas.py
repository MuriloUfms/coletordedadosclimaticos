from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from src.models import FrequencyEnum


class SubscriberSchema(BaseModel):
    email: EmailStr = Field(..., description='Email do inscrito')
    frequency: FrequencyEnum = Field(
        ..., description='Frequência de envio da newsletter'
    )


class UnsubscribeRequest(BaseModel):
    email: EmailStr = Field(..., description='Email do inscrito')


class SubscribeResponse(BaseModel):
    message: str = Field(..., description='Mensagem de sucesso')


class ColetaBase(BaseModel):
    latitude: float = Field(
        ..., example=-20.5026554, description='Latitude da localização'
    )
    longitude: float = Field(
        ..., example=-54.6154765, description='Longitude da localização'
    )


class ColetaRequest(ColetaBase):
    pass


class ColetaResponse(BaseModel):
    id: int = Field(..., description='ID da coleta')
    temperatura: float = Field(..., description='Temperatura em graus Celsius')
    umidade: float = Field(..., description='Umidade relativa do ar em %')
    velocidade_vento: float = Field(..., description='Velocidade do vento em m/s')
    direcao_vento: float = Field(..., description='Direção do vento em graus')
    timestamp: datetime = Field(..., description='Data e hora da coleta UTC')
