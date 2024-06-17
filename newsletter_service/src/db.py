from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

from settings import Settings


class Base(DeclarativeBase):
    pass


engine = create_engine(Settings.DATABASE_URI)


def get_session() -> Session:
    yield Session(engine)
