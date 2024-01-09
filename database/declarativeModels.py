import datetime
from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (DECIMAL,
                        JSON,
                        String,
                        B)
from decimal import Decimal
from typing import Annotated, Optional


intpk = Annotated[int, mapped_column(primary_key=True)]

class BaseBd(DeclarativeBase):
    pass

class Users(BaseBd):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    phone_number: Mapped[str] = mapped_column(String(20))
    role: Mapped[str]

class Masters(BaseBd):
    __tablename__ = "masters"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    phone_number: Mapped[str] = mapped_column(String(20))
    work_schedule: Mapped[bytearray]
    content_id: Mapped[int]

class Services(BaseBd):
    __tablename__ = "services"
    name: Mapped[str] = mapped_column(String(50), primary_key=True)
    type: Mapped[str] = mapped_column(String(20))
    cost: Mapped[int]
    content_id: Mapped[int]

class Appointments(BaseBd):
    __tablename__ = "appointments"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    master_id: Mapped[int]
    service_name: Mapped[str] = mapped_column(String(20))
    date_time: Mapped[datetime]
    extra: Mapped[str]

class Content(BaseBd):
    __tablename__ = "content"
    id: Mapped[int] = mapped_column(primary_key=True)
    target_name: Mapped[str]
    page: Mapped[str]
    type: Mapped[str]
    extra: Mapped[str]

class mastersService(BaseBd):
    __tablename__ = "content"
    master_id: Mapped[int] = mapped_column(primary_key=True)
    service_name: Mapped[str] = mapped_column(String(20), primary_key=True)