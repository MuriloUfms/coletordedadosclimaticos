from contextlib import asynccontextmanager

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from settings import Settings
from src.db import Base, engine
from src.routes import router as subscriber_router
from src.services import send_newsletter
from datetime import datetime


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(engine)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        send_newsletter,
        'interval',
        seconds=Settings.NEWSLETTER_INTERVAL_SECONDS,
        next_run_time=datetime.now(),
    )
    scheduler.start()

    yield


app = FastAPI(
    title='Boletim Informativo de Dados Climáticos',
    description='Api de envio de boletim informativo de dados climáticos',
    openapi_url='/newsletter/openapi.json',
    docs_url='/newsletter/docs',
    version='1.0',
    lifespan=lifespan,
)
add_pagination(app)

app.include_router(
    subscriber_router, prefix='/newsletter', tags=['Boletim Informativo']
)
