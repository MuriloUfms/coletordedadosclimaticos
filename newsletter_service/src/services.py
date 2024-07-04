from datetime import UTC, datetime, timedelta

import httpx
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from sqlalchemy import select
from sqlalchemy.orm import Session

from settings import Settings
from src.db import engine
from src.models import Subscriber

fm = FastMail(
    ConnectionConfig(
        MAIL_FROM_NAME='Coletor de Dados Climáticos',
        MAIL_USERNAME=Settings.MAIL_USERNAME,
        MAIL_PASSWORD=Settings.MAIL_PASSWORD,
        MAIL_FROM=Settings.MAIL_FROM,
        MAIL_PORT=Settings.MAIL_PORT,
        MAIL_SERVER=Settings.MAIL_SERVER,
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False,
    )
)


async def get_data():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f'{Settings.API_COLECTOR_URL}/collect',
            json={'latitude': -20.5026554, 'longitude': -54.6154765},
        )
    response.raise_for_status()
    return response.json()


def get_subscribers_emails():
    session = Session(engine)

    stmt = select(Subscriber)
    subscribers = session.scalars(stmt).all()

    now = datetime.now(UTC)

    emails = []
    for sub in subscribers:
        last_sent_conscious = sub.last_sent.replace(tzinfo=UTC)
        if last_sent_conscious + timedelta(seconds=sub.frequency) < now:
            emails.append(sub.email)
            sub.last_sent = now

    session.commit()
    return emails


async def send_mail(recipients: list[str], data: dict):
    if not recipients:
        return

    message = MessageSchema(
        subject='Clima da FACOM - Newsletter',
        recipients=recipients,
        body=f'Temperatura: {data["temperatura"]}\n'
        f'Umidade: {data["umidade"]}\n'
        f'Velocidade do vento: {data["velocidade_vento"]}\n'
        f'Direção do vento: {data["direcao_vento"]}',
        subtype=MessageType.plain,
    )
    await fm.send_message(message)


async def send_newsletter():
    recipients = get_subscribers_emails()
    data = await get_data()
    await send_mail(recipients, data)
