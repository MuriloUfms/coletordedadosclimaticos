from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.db import Base, engine
from src.routers.coleta import router as coleta_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(engine)
    yield


app = FastAPI(
    title="Coletor de Dados Climáticos",
    description="API para coletar dados climáticos de uma localização geográfica",
    version="1.0",
    docs_url="/",
    redoc_url="/redoc",
    lifespan=lifespan,
)
add_pagination(app)

app.include_router(coleta_router, prefix="/api/v1/coletas", tags=["Coletas"])
