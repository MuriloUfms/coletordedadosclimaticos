from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination.links import Page
from sqlalchemy import select

from src.db import Session, get_session
from src.models import Coletas
from src.schemas import ColetaRequest, ColetaResponse
from src.services import coletar_dados_climaticos

router = APIRouter()


@router.post('/collect', response_model=ColetaResponse)
async def coletar_dados(
    payload: ColetaRequest, session: Annotated[Session, Depends(get_session)]
):
    data = coletar_dados_climaticos(payload.latitude, payload.longitude)

    coleta = Coletas(
        latitude=payload.latitude,
        longitude=payload.longitude,
        temperatura=data['temperatura'],
        umidade=data['umidade'],
        velocidade_vento=data['velocidade_vento'],
        direcao_vento=data['direcao_vento'],
    )
    session.add(coleta)
    session.commit()

    return coleta


@router.get('/collections', response_model=Page[ColetaResponse])
async def listar_coletas(session: Annotated[Session, Depends(get_session)]):
    return paginate(session, select(Coletas))
