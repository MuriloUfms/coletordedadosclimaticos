from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.db import Base, engine
from src.routes import router as coleta_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(engine)
    yield


app = FastAPI(
    title='Coletor de Dados Climáticos',
    description='API para coletar dados climáticos de uma localização geográfica',
    openapi_url='/coletor/openapi.json',
    docs_url='/coletor/docs',
    version='1.0',
    lifespan=lifespan,
)
add_pagination(app)

app.include_router(coleta_router, prefix='/coletor', tags=['Coleta'])
