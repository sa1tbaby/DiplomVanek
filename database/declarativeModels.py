from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import String

from datetime import datetime
from typing import List


class BaseBd(DeclarativeBase):
    pass


class Users(BaseBd):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    phone_number: Mapped[str] = mapped_column(String(20))
    role: Mapped[str]

    appointment: Mapped[List['Appointments']] = relationship()


class Masters(BaseBd):
    __tablename__ = "masters"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    phone_number: Mapped[str] = mapped_column(String(20))
    work_schedule: Mapped[bytearray]

    appointment: Mapped[List['Appointments']] = relationship()
    master_service: Mapped[List['MastersService']] = relationship()
    content: Mapped[List['Content']] = relationship()


class Services(BaseBd):
    __tablename__ = "services"
    name: Mapped[str] = mapped_column(String(50), primary_key=True)
    type: Mapped[str] = mapped_column(String(20))
    cost: Mapped[int]

    appointment: Mapped[List['Appointments']] = relationship()
    master_service: Mapped[List['MastersService']] = relationship()
    content: Mapped[List['Content']] = relationship()


class Appointments(BaseBd):
    __tablename__ = "appointments"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    master_id: Mapped[int] = mapped_column(ForeignKey("masters.id"))
    service_name: Mapped[str] = mapped_column(
        String(20),
        ForeignKey("services.name")
    )
    date_time: Mapped[datetime]
    extra: Mapped[str] = mapped_column(nullable=True)

class Content(BaseBd):
    __tablename__ = "content"
    id: Mapped[int] = mapped_column(primary_key=True)
    master_id: Mapped[str] = mapped_column(
        ForeignKey("masters.id"),
        nullable=True
    )
    service_name: Mapped[str] = mapped_column(
        ForeignKey("services.name"),
        nullable=True
    )
    page: Mapped[str]
    type: Mapped[str]
    extra: Mapped[str] = mapped_column(nullable=True)

class MastersService(BaseBd):
    __tablename__ = "content"
    master_id: Mapped[int] = mapped_column(
        ForeignKey("masters.id"),
        primary_key=True
    )
    service_name: Mapped[str] = mapped_column(
        String(20),
        ForeignKey("services.name"),
        primary_key=True
    )