from pydantic import BaseModel
from typing import Annotated
from uuid import uuid4
import os.path

project_dir = os.path.abspath(os.path.pardir)
config_dir = os.path.join(project_dir, 'configs')

uuid4_len = len(str(uuid4()))
uuid_ = Annotated[str, uuid4_len]

str_50 = Annotated[str, uuid4_len]
str_20 = Annotated[str, uuid4_len]

services_name_dict = {
    "eyebrows": "Брови",
    "nails": "Ногти",
    "coloring": "Окрашивание",
    "sugaring": "Шугаринг",
    "haircut": "Стрижка",
    "solarium": "Солярий"
}

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


