from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination.links import Page
from sqlalchemy import select

from src.db import Session, get_session
from src.models import Subscriber
from src.schemas import (
    SubscriberSchema,
    UnsubscribeRequest,
    SubscribeResponse,
)
from src.services import get_data

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

    subscriber = Subscriber(email=payload.email, frequency=payload.frequency)
    session.add(subscriber)
    session.commit()

    return {
        'message': f'{payload.email} subscribed successfully '
                   f'with frequency {payload.frequency}'
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


@router.post('/send-newsletter')
async def send_newsletter(session: Annotated[Session, Depends(get_session)]):
    subscribers = session.execute(select(Subscriber)).scalars().all()
    data = get_data()

    # TODO: Implement email sending logic
    for subscriber in subscribers:
        print(f'Sending newsletter to {subscriber.email}: {data}')

    return {'message': 'Newsletter sent successfully'}
