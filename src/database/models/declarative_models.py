from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID

from typing import List
from base_model import (BaseBd,
                        uuid_pk, int_pk, opt_str, date_time,
                        media_enum, role_enum, services_enum)


masters_service = Table(
    'masters_services_associate',
    BaseBd.metadata,
    Column('masters_id', ForeignKey('masters.id'), primary_key=True),
    Column('services_id', ForeignKey('services.id'), primary_key=True)
)


class Users(BaseBd):
    __tablename__ = 'users'
    id: Mapped[uuid_pk]
    first_name: Mapped[str]
    second_name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    phone_number: Mapped[str]
    role: Mapped[role_enum]

    appointments_list: Mapped[List['Appointments']] = relationship()


class Services(BaseBd):
    __tablename__ = 'services'
    id: Mapped[int_pk]
    service_name: Mapped[str]
    service_type: Mapped[services_enum]
    type_cost: Mapped[int]
    masters_id: Mapped

    masters_list: Mapped[List['Masters']] = relationship(secondary=masters_service, back_populates='services_list')
    appointments_list: Mapped[List['Appointments']] = relationship()


class Masters(BaseBd):
    __tablename__ = 'masters'
    id: Mapped[uuid_pk]
    first_name: Mapped[str]
    second_name: Mapped[str]
    email: Mapped[str]
    phone_number: Mapped[str]
    work_schedule: Mapped[bytes]
    service_id: Mapped

    services_list: Mapped[List['Services']] = relationship(secondary=masters_service, back_populates='masters_list')
    appointments_list: Mapped[List['Appointments']] = relationship()


class Appointments(BaseBd):
    __tablename__ = 'appointments'
    id: Mapped[uuid_pk]
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    master_id: Mapped[UUID] = mapped_column(ForeignKey('masters.id'))
    service_id: Mapped[UUID] = mapped_column(ForeignKey('services.id'))
    date_time: Mapped[date_time]
    extra: Mapped[opt_str]


class Media(BaseBd):
    __tablename__ = 'media'
    id: Mapped[uuid_pk]
    page: Mapped[str]
    link: Mapped[str]
    type: Mapped[media_enum]
    content: Mapped[opt_str]
