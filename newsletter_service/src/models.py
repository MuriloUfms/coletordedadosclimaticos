from datetime import UTC, datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Subscriber(Base):
    __tablename__ = 'subscribers'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    interval_in_hours: Mapped[int] = mapped_column(default=24)
    last_sent: Mapped[datetime] = mapped_column(
        default=datetime(1970, 1, 1, tzinfo=UTC)
    )
