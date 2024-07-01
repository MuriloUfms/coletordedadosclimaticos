import httpx

from fastapi import APIRouter
from settings import Settings
from fastapi_pagination.links import Page

from src.schemas import (
    ColetaResponse,
    SubscribeResponse,
    SubscriberSchema,
    UnsubscribeRequest,
)

router = APIRouter()


@router.post('/subscribe', response_model=SubscribeResponse)
async def subscribe(payload: SubscriberSchema):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f'{Settings.API_NEWSLETTER_URL}/subscribe',
            json=payload.model_dump(),
        )
    response.raise_for_status()

    return response.json()


@router.post('/unsubscribe', response_model=SubscribeResponse)
async def unsubscribe(
    payload: UnsubscribeRequest
):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f'{Settings.API_NEWSLETTER_URL}/unsubscribe',
            json=payload.model_dump(),
        )
    response.raise_for_status()

    return response.json()


@router.get('/subscribers', response_model=Page[SubscriberSchema])
async def list_subscribers():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{Settings.API_NEWSLETTER_URL}/subscribers')
    response.raise_for_status()

    return response.json()


@router.get('/collections', response_model=Page[ColetaResponse])
async def list_collections():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{Settings.API_COLECTOR_URL}/collections')
    response.raise_for_status()

    return response.json()
