from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from enum import Enum as enumEnum

from datetime import datetime
from typing import List, Annotated, Optional

from app.schemas import uuid_, str_20, str_50

uuid_pk = Annotated[uuid_, mapped_column(primary_key=True)]

class BaseBd(DeclarativeBase):
    pass

class Users(BaseBd):
    __tablename__ = "users"
    id: Mapped[uuid_pk]
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    phone_number: Mapped[str_20]
    role: Mapped[str]

    appointment: Mapped[List['Appointments']] = relationship()


class Masters(BaseBd):
    __tablename__ = "masters"
    id: Mapped[uuid_pk]
    name: Mapped[str]
    email: Mapped[str]
    phone_number: Mapped[str_20]
    work_schedule: Mapped[str]
    type: Mapped[str_50] = mapped_column()

    appointments_list: Mapped[List['Appointments']] = relationship()
    content_list: Mapped[List['Content']] = relationship()


class Services(BaseBd):
    __tablename__ = "services"
    name: Mapped[str_50] = mapped_column(primary_key=True)
    type: Mapped[str_50] = mapped_column()
    cost: Mapped[int]

    masters_list: Mapped[List['MastersService']] = relationship()
    appointments_list: Mapped[List['Appointments']] = relationship()
    content: Mapped[List['Content']] = relationship()


class Appointments(BaseBd):
    __tablename__ = "appointments"
    id: Mapped[uuid_pk]
    user_id: Mapped[uuid_] = mapped_column(ForeignKey("users.id"))
    master_id: Mapped[Optional[uuid_]] = mapped_column(ForeignKey("masters.id"))
    service_name: Mapped[str_50] = mapped_column(ForeignKey("services.name"))
    date_time: Mapped[datetime]
    extra: Mapped[Optional[str]]

class ContentType(enumEnum):
    img: "img"
    text: "text"

class Content(BaseBd):
    __tablename__ = "content"
    id: Mapped[uuid_pk]
    master_id: Mapped[Optional[uuid_]] = mapped_column(ForeignKey("masters.id"))
    service_name: Mapped[Optional[str_50]] = mapped_column(ForeignKey("services.name"))
    page: Mapped[str]
    type: Mapped[ContentType]
    extra: Mapped[Optional[str]]

class MastersService(BaseBd):
    __tablename__ = "masters_service"
    master_id: Mapped[int] = mapped_column(ForeignKey("masters.id"))
    service_name: Mapped[str_50] = mapped_column(ForeignKey("services.name"))
