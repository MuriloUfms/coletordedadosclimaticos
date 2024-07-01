from fastapi import FastAPI
from src.routes import router


app = FastAPI(
    title='Api Gateway',
    description='Api gateway do serviço de coleta de dados climáticos',
    version='1.0',
    docs_url='/',
    redoc_url='/redoc',
)

app.include_router(router, prefix='/api/v1', tags=['Main'])
