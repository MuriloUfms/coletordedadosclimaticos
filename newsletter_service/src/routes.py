from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination.links import Page
from sqlalchemy import select

from src.db import Session, get_session
from src.models import Subscriber
from src.schemas import (
    SubscribeResponse,
    SubscriberSchema,
    UnsubscribeRequest,
)

router = APIRouter()


@router.post('/subscribe', response_model=SubscribeResponse)
async def subscribe(
    payload: SubscriberSchema, session: Annotated[Session, Depends(get_session)]
):
    stmt = select(Subscriber).where(Subscriber.email == payload.email)

    if session.scalar(stmt):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Email already subscribed'
        )

    subscriber = Subscriber(
        email=payload.email, interval_in_hours=payload.interval_in_hours
    )
    session.add(subscriber)
    session.commit()

    return {
        'message': f'{payload.email} subscribed successfully '
        f'and will receive the newsletter every {payload.interval_in_hours} hours'
    }


@router.post('/unsubscribe', response_model=SubscribeResponse)
async def unsubscribe(
    payload: UnsubscribeRequest, session: Annotated[Session, Depends(get_session)]
):
    stmt = select(Subscriber).where(Subscriber.email == payload.email)

    if not (subscriber := session.scalar(stmt)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Email not subscribed'
        )

    session.delete(subscriber)
    session.commit()

    return {'message': 'Unsubscribed successfully'}


@router.get('/subscribers', response_model=Page[SubscriberSchema])
async def list_subscribers(session: Annotated[Session, Depends(get_session)]):
    return paginate(session, select(Subscriber))
