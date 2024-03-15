from enum import Enum
from uuid import uuid4
from typing import Annotated
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM


class RolesEnum(Enum):
    ADMIN = 'admin'
    USER = 'user'


class ServiceTypeEnum(Enum):
    BROWS = 'Ресницы и брови'
    NAILS = 'Ногтевой сервис'
    HAIRCUT = 'Стрижки'
    SOLARIUM = 'Солярий'
    SUGARING = 'Шугаринг'
    COLORING = 'Окрашивание'


class MediaTypeEnum(Enum):
    TEXT = 'txt'
    IMAGE = 'img'


class MediaPagesEnum(Enum):
    MAIN = 'main'
    SERVICES = 'services'
    MASTERS = 'masters'
    APPOINTMENT = 'appointment'
    ADMIN = 'admin'
    PERSON = 'person'

uuid_pk = Annotated[
    UUID,
    mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
]
int_pk = Annotated[
    int,
    mapped_column(primary_key=True)
]
date_time = Annotated[
    float,
    mapped_column(nullable=False)
]
opt_str = Annotated[
    str,
    mapped_column(nullable=True)
]
media_type_enum = Annotated[
    Enum,
    mapped_column(
        PG_ENUM(MediaTypeEnum, name='media_type_enum', create_type=True),
        nullable=False
    )
]
media_page_enum = Annotated[
    Enum,
    mapped_column(
        PG_ENUM(MediaPagesEnum, name='media_page_enum', create_type=True),
        nullable=False
    )
]
services_enum = Annotated[
    Enum,
    mapped_column(
        PG_ENUM(ServiceTypeEnum, name='services_enum', create_type=True),
        nullable=False
    )
]
role_enum = Annotated[
    Enum,
    mapped_column(
        PG_ENUM(RolesEnum, name='role_enum', create_type=True),
        nullable=False
    )
]


class BaseBd(DeclarativeBase):
    pass


