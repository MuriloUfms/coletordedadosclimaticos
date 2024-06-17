from enum import StrEnum

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class FrequencyEnum(StrEnum):
    weekly = 'weekly'
    biweekly = 'biweekly'
    monthly = 'monthly'
    semiannual = 'semiannual'


class Subscriber(Base):
    __tablename__ = 'subscribers'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    frequency: Mapped[FrequencyEnum] = mapped_column(Enum(FrequencyEnum))
