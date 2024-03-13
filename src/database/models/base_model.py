from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID, ENUM as PG_ENUM, FLOAT

from typing import Annotated
from uuid import uuid4
from enum import Enum


class RolesEnum(Enum):
    ADMIN = 'admin'
    USER = 'user'


class ServiceTypeEnum(Enum):
    BROWS = 'Брови'
    NAILS = 'Ногти'
    HAIRCUT = 'Стрижка'
    SOLARIUM = 'Солярий'
    SUGARING = 'Шугаринг'
    COLORING = 'Окрашивание'


class MediaTypeEnum(Enum):
    TEXT = 'txt'
    IMAGE = 'img'


class BaseBd(DeclarativeBase):
    pass


uuid_pk = Annotated[
    UUID(as_uuid=True),
    mapped_column(primary_key=True, autoincrement=True, default=uuid4)
]
media_enum = Annotated[
    PG_ENUM(MediaTypeEnum, 'media_enum', create_type=False),
    mapped_column(nullable=False)
]
role_enum = Annotated[
    PG_ENUM(RolesEnum, name='role_enum', create_type=False),
    mapped_column(nullable=False, default=RolesEnum.USER)
]
services_enum = Annotated[
    PG_ENUM(ServiceTypeEnum, name='services_enum', create_type=False),
    mapped_column(nullable=False)
]
int_pk = Annotated[
    int,
    mapped_column(primary_key=True)
]
date_time = Annotated[
    FLOAT,
    mapped_column(nullable=False)
]
opt_str = Annotated[
    str,
    mapped_column(nullable=True)
]




