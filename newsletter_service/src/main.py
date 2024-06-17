from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.db import Base, engine
from src.routes import router as subscriber_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(engine)
    yield


app = FastAPI(
    title='Boletim Informativo de Dados Climáticos',
    description='Api de envio de boletim informativo de dados climáticos',
    version='1.0',
    docs_url='/',
    redoc_url='/redoc',
    lifespan=lifespan,
)
add_pagination(app)

app.include_router(subscriber_router, prefix='/api/v1', tags=['Boletim Informativo'])
