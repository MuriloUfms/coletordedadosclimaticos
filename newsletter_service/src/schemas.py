from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class SubscribeRequest(BaseModel):
    email: EmailStr = Field(..., description='Email do inscrito')
    frequency_hours: float = Field(description='Intervalo de envio em horas')


class SubscribeReponse(BaseModel):
    email: EmailStr = Field(..., description='Email do inscrito')
    frequency: float = Field(description='Intervalo de envio em horas')


class UnsubscribeRequest(BaseModel):
    email: EmailStr = Field(..., description='Email do inscrito')


class MessageResponse(BaseModel):
    message: str = Field(..., description='Mensagem de sucesso')
