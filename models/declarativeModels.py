from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (DECIMAL,
                        JSON,
                        String)
from decimal import Decimal
from typing import Annotated, Optional
from pydantic import BaseModel


class ConfigDB(BaseModel):
    dialect: str = 'postgresql'
    driver: str = 'psycopg2'
    username: str = 'cesium'
    password: str = 'user'
    host: str = '192.168.1.148'
    port: str = '5432'
    database: str
    engine_echo: bool = True
    engine_pool_size: int = 5

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

class Users(BaseBd):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    phone_number: Mapped[str] = mapped_column(String(20))
    role: Mapped[str]