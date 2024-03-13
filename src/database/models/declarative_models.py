from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from base_model import BaseBd, uuid_pk, role_enum, int_pk, services_enum, date_time, opt_str
from sqlalchemy.orm import mapped_column
from typing import List
from sqlalchemy import ForeignKey


class Users(BaseBd):
    __tablename__ = "users"
    id: Mapped[uuid_pk]
    first_name: Mapped[str]
    second_name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    phone_number: Mapped[str]
    role: Mapped[role_enum]

    appointments_list: Mapped[List['Appointments']] = relationship()


class Services(BaseBd):
    __tablename__ = "services"
    id: Mapped[int_pk]
    service_name: Mapped[str]
    service_type: Mapped[services_enum]
    type_cost: Mapped[int]
    masters_id: Mapped

    appointments_list: Mapped[List['Appointments']] = relationship()


class Masters(BaseBd):
    __tablename__ = "masters"
    id: Mapped[uuid_pk]
    first_name: Mapped[str]
    second_name: Mapped[str]
    email: Mapped[str]
    phone_number: Mapped[str]
    work_schedule: Mapped[bytes]
    service_type: Mapped

    appointments_list: Mapped[List['Appointments']] = relationship()


class Appointments(BaseBd):
    __tablename__ = "appointments"
    id: Mapped[uuid_pk]
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    master_id: Mapped[UUID] = mapped_column(ForeignKey('masters.id'))
    service_id: Mapped[UUID] = mapped_column(ForeignKey('services.id'))
    date_time: Mapped[date_time]
    extra: Mapped[opt_str]


class Content(BaseBd):
    pass