from pydantic import BaseModel
from typing import Annotated
from uuid import uuid4
import os.path

project_dir = os.path.abspath(os.path.curdir)
config_dir = os.path.join(project_dir, 'configs')

uuid4_len = len(str(uuid4()))
uuid_ = int

str_50 = Annotated[str, uuid4_len]
str_20 = Annotated[str, uuid4_len]

services_name_dict = {
    "eyebrows": "Ресницы и брови",
    "nails": "Ногтевой сервис",
    "coloring": "Окрашивание",
    "sugaring": "Шугаринг",
    "haircut": "Стрижка",
    "solarium": "Солярий"
}

con_text = {
    "Ресницы и брови": 'aefawfawf',
    "Ногтевой сервис": '',
    "Окрашивание": '',
    "Шугаринг": '',
    "Стрижка": '',
    "Солярий": '',
    "us": '',
    "extra": ''
}


time_list = [ dict(index=item, time=f"{item}:00:00") for item in range(12, 22, 1)]

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



