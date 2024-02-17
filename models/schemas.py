from pydantic import BaseModel
from typing import Annotated
from uuid import uuid4
import os.path

project_dir = os.path.abspath(os.path.curdir)
config_dir = os.path.join(project_dir, 'configs')
content = {
        "appointments": [
            {
                "id": 1,
                "user_id": 3,
                "master_id": 222,
                "service_name": "Окрашивание прикорневое",
                "date_time": "2024-01-10 10:00:00",
                "extra": None
            },
            {
                "id": 2,
                "user_id": 2,
                "master_id": 222,
                "service_name": "Сложное окрашивание",
                "date_time": "2024-01-10 11:00:00",
                "extra": None
            },
            {
                "id": 3,
                "user_id": 2,
                "master_id": 111,
                "service_name": "Стрижка каскад",
                "date_time": "2024-01-10 10:00:00",
                "extra": None
            },
            {
                "id": 4,
                "user_id": 2,
                "master_id": 222,
                "service_name": "Окрашивание прикорневое",
                "date_time": "2024-01-10 12:00:00",
                "extra": None
            },
            {
                "id": 5,
                "user_id": 3,
                "master_id": 333,
                "service_name": "Стрижка фэйд",
                "date_time": "2024-01-10 10:00:00",
                "extra": None
            },
            {
                "id": 6,
                "user_id": 4,
                "master_id": 444,
                "service_name": "Маникюр дизайнерский",
                "date_time": "2024-01-10 10:00:00",
                "extra": None
            },
            {
                "id": 7,
                "user_id": 5,
                "master_id": 444,
                "service_name": "Маникюр без покрытия",
                "date_time": "2024-01-10 11:00:00",
                "extra": None
            },
            {
                "id": 8,
                "user_id": 6,
                "master_id": 555,
                "service_name": "Маникюр дизайнерский",
                "date_time": "2024-01-10 11:00:00",
                "extra": None
            },
            {
                "id": 9,
                "user_id": 7,
                "master_id": 666,
                "service_name": "Бёдра",
                "date_time": "2024-01-10 10:00:00",
                "extra": None
            },
            {
                "id": 10,
                "user_id": 8,
                "master_id": 777,
                "service_name": "Наращивание ресниц",
                "date_time": "2024-01-10 10:00:00",
                "extra": None
            },
            {
                "id": 11,
                "user_id": 9,
                "master_id": 888,
                "service_name": "Ламинирование ресниц",
                "date_time": "2024-01-10 11:00:00",
                "extra": None
            },
            {
                "id": 12,
                "user_id": 10,
                "master_id": 999,
                "service_name": "Стандарт",
                "date_time": "2024-01-10 12:00:00",
                "extra": None
            },
            {
                "id": 13,
                "user_id": 1,
                "master_id": 999,
                "service_name": "Премиум",
                "date_time": "2024-01-10 13:00:00",
                "extra": None
            }
        ],
        "content": [
            {
                "id": 1,
                "master_id": 111,
                "service_name": None,
                "page": "masters",
                "type": "img",
                "extra": "img/masters/Tatyana.jpg"
            },
            {
                "id": 2,
                "master_id": 111,
                "service_name": None,
                "page": "masters",
                "type": "text",
                "extra": "парикмахер"
            },
            {
                "id": 3,
                "master_id": 222,
                "service_name": None,
                "page": "masters",
                "type": "img",
                "extra": "img/masters/svetlana.jpg"
            },
            {
                "id": 4,
                "master_id": 222,
                "service_name": None,
                "page": "masters",
                "type": "text",
                "extra": "топ мастер-парикмахер"
            },
            {
                "id": 5,
                "master_id": 333,
                "service_name": None,
                "page": "masters",
                "type": "img",
                "extra": "img/masters/Dima.jpg"
            },
            {
                "id": 6,
                "master_id": 333,
                "service_name": None,
                "page": "masters",
                "type": "text",
                "extra": "барбер"
            },
            {
                "id": 7,
                "master_id": 444,
                "service_name": None,
                "page": "masters",
                "type": "img",
                "extra": "img/masters/Marina.jpg"
            },
            {
                "id": 8,
                "master_id": 444,
                "service_name": None,
                "page": "masters",
                "type": "text",
                "extra": "мастер ногтевого сервиса"
            },
            {
                "id": 9,
                "master_id": 555,
                "service_name": None,
                "page": "masters",
                "type": "img",
                "extra": "img/masters/Anna.jpg"
            },
            {
                "id": 10,
                "master_id": 555,
                "service_name": None,
                "page": "masters",
                "type": "text",
                "extra": "мастер ногтевого сервиса"
            },
            {
                "id": 11,
                "master_id": 666,
                "service_name": None,
                "page": "masters",
                "type": "img",
                "extra": "img/masters/alena.jpg"
            },
            {
                "id": 12,
                "master_id": 666,
                "service_name": None,
                "page": "masters",
                "type": "text",
                "extra": "Шугаринг"
            },
            {
                "id": 13,
                "master_id": 777,
                "service_name": None,
                "page": "masters",
                "type": "img",
                "extra": "img/masters/Efros.jpg"
            },
            {
                "id": 14,
                "master_id": 777,
                "service_name": None,
                "page": "masters",
                "type": "text",
                "extra": "Бровист"
            },
            {
                "id": 15,
                "master_id": 888,
                "service_name": None,
                "page": "masters",
                "type": "img",
                "extra": "img/masters/Lubava.jpg"
            },
            {
                "id": 16,
                "master_id": 888,
                "service_name": None,
                "page": "masters",
                "type": "text",
                "extra": "Бровист"
            },
            {
                "id": 17,
                "master_id": None,
                "service_name": None,
                "page": "masters",
                "type": "text",
                "extra": "Бровист"
            },
            {
                "id": 18,
                "master_id": None,
                "service_name": None,
                "page": "main",
                "type": "img",
                "extra": "img/main/haircut_2.gif"
            },
            {
                "id": 19,
                "master_id": None,
                "service_name": None,
                "page": "main",
                "type": "img",
                "extra": "img/main/haircut_3.gif"
            },
            {
                "id": 20,
                "master_id": None,
                "service_name": None,
                "page": "main",
                "type": "img",
                "extra": "img/main/haircut_1.gif"
            },
            {
                "id": 21,
                "master_id": None,
                "service_name": None,
                "page": "services",
                "type": "text",
                "extra": "Титульная страница раздела Услуг"
            },

        ],
        "masters": [
            {
                "id": 111,
                "name": "Татьяна",
                "email": "tati_master@gmail.ru",
                "phone_number": "+79992223342",
                "work_schedule": "110110110110110110110110110110",
                "type": "Стрижка"
            },
            {
                "id": 222,
                "name": "Марина ",
                "email": "mari_master@gmail.ru",
                "phone_number": "+79992223343",
                "work_schedule": "110110110110110110110110110110",
                "type": "Окрашивание"
            },
            {
                "id": 333,
                "name": "Анна",
                "email": "anna_master@gmail.ru",
                "phone_number": "+79992223344",
                "work_schedule": "011011011011011011011011011011",
                "type": "Стрижка"
            },
            {
                "id": 444,
                "name": "Светлана",
                "email": "sveta_master@gmail.ru",
                "phone_number": "+79992223345",
                "work_schedule": "011011011011011011011011011011",
                "type": "Ногтевой сервис"
            },
            {
                "id": 555,
                "name": "Дмитрий ",
                "email": "dima_master@gmail.ru",
                "phone_number": "+79992223346",
                "work_schedule": "101101101101101101101101101101",
                "type": "Ногтевой сервис"
            },
            {
                "id": 666,
                "name": "Алена",
                "email": "anna_master@gmail.ru",
                "phone_number": "+79992223347",
                "work_schedule": "101101101101101101101101101101",
                "type": "Шугаринг"
            },
            {
                "id": 777,
                "name": "Ефросинья",
                "email": "efro_master@gmail.ru",
                "phone_number": "+79992223348",
                "work_schedule": "110110110110110110110110110110",
                "type": "Ресницы и брови"
            },
            {
                "id": 888,
                "name": "Любава",
                "email": "luba_master@gmail.ru",
                "phone_number": "+79992223349",
                "work_schedule": "101101101101101101101101101101",
                "type": "Ресницы и брови"
            },
            {
                "id": 999,
                "name": "Солярий",
                "email": "",
                "phone_number": "",
                "work_schedule": "111111111111111111111111111111",
                "type": "Солярий"
            }
        ],
        "services": [
            {"type": "Ресницы и брови", "name": "Наращивание ресниц", "cost": "2300"},
            {"type": "Ресницы и брови", "name": "Наращивание ресниц 2D", "cost": "2600"},
            {"type": "Ресницы и брови", "name": "Наращивание ресниц 3D", "cost": "2900"},
            {"type": "Ресницы и брови", "name": "Снятие ресниц", "cost": "500"},
            {"type": "Ресницы и брови", "name": "Ламинирование ресниц", "cost": "2300"},
            {"type": "Ресницы и брови", "name": "Ламинирование бровей", "cost": "2000"},
            {"type": "Ресницы и брови", "name": "Архитектура бровей", "cost": "1800"},
            {"type": "Ресницы и брови", "name": "Коррекция бровей (без окрашивания)", "cost": "700"},
            {"type": "Окрашивание", "name": "Окрашивание в 1 тон", "cost": "3500"},
            {"type": "Окрашивание", "name": "Сложное окрашивание", "cost": "5200"},
            {"type": "Окрашивание", "name": "Окрашивание прикорневое", "cost": "2200"},
            {"type": "Окрашивание", "name": "Скрытое окрашивание", "cost": "3000"},
            {"type": "Окрашивание", "name": "Осветление + тонирование", "cost": "5000"},
            {"type": "Окрашивание", "name": "Мелирование", "cost": "3500"},
            {"type": "Окрашивание", "name": "Тонирование", "cost": "1700"},
            {"type": "Окрашивание", "name": "Химия", "cost": "2500"},
            {"type": "Окрашивание", "name": "Мужское тонирование седины", "cost": "2000"},
            {"type": "Ногтевой сервис", "name": "Маникюр без покрытия", "cost": "1000"},
            {"type": "Ногтевой сервис", "name": "Маникюр дизайнерский", "cost": "2000"},
            {"type": "Ногтевой сервис", "name": "Маникюр мужской", "cost": "1300"},
            {"type": "Ногтевой сервис", "name": "Укрепление ногтей", "cost": "700"},
            {"type": "Ногтевой сервис", "name": "Педикюр", "cost": "1700"},
            {"type": "Стрижка", "name": "Стрижка одной насадкой", "cost": "700"},
            {"type": "Стрижка", "name": "Стрижка модельная", "cost": "1200"},
            {"type": "Стрижка", "name": "Стрижка фэйд", "cost": "1000"},
            {"type": "Стрижка", "name": "Стрижка каскад", "cost": "1000"},
            {"type": "Стрижка", "name": "Стрижка детская (от 6 до 9 лет)", "cost": "700"},
            {"type": "Солярий", "name": "Премиум", "cost": "200"},
            {"type": "Солярий", "name": "Стандарт", "cost": "100"},
            {"type": "Шугаринг", "name": "Бикини", "cost": "900"},
            {"type": "Шугаринг", "name": "Бёдра", "cost": "600"},
            {"type": "Шугаринг", "name": "Ноги", "cost": "1500"},
            {"type": "Шугаринг", "name": "Руки", "cost": "1000"},
            {"type": "Шугаринг", "name": "Лицо", "cost": "700"},
            {"type": "Шугаринг", "name": "Ягодицы", "cost": "300"}
        ],
        "users": [
            {
                "id": 1,
                "name": "Иванова Анна Михайловна",
                "password": "master",
                "email": "anna_example@gmail.ru",
                "phone_number": "+79261234567",
                "role": "guest"
            },
            {
                "id": 2,
                "name": "Петров Сергей Викторович",
                "password": "master",
                "email": "petr_example@gmail.ru",
                "phone_number": "+79181234567",
                "role": "guest"
            },
            {
                "id": 3,
                "name": "Смирнова Екатерина Александровна",
                "password": "master",
                "email": "kate_example@gmail.ru",
                "phone_number": "+79031234567",
                "role": "guest"
            },
            {
                "id": 4,
                "name": "Кузнецов Дмитрий Иванович",
                "password": "master",
                "email": "dima_example@gmail.ru",
                "phone_number": "+79341234567",
                "role": "guest"
            },
            {
                "id": 5,
                "name": "Васильева Ольга Петровна",
                "password": "master",
                "email": "olga_example@gmail.ru",
                "phone_number": "+79551234567",
                "role": "guest"
            },
            {
                "id": 6,
                "name": "Попов Александр Михайлович",
                "password": "master",
                "email": "aleks_example@gmail.ru",
                "phone_number": "+79661234567",
                "role": "guest"
            },
            {
                "id": 7,
                "name": "Соколова Елена Сергеевна",
                "password": "master",
                "email": "helena_example@gmail.ru",
                "phone_number": "+79771234567",
                "role": "guest"
            },
            {
                "id": 8,
                "name": "Михайлов Игорь Валерьевич",
                "password": "master",
                "email": "igor_example@gmail.ru",
                "phone_number": "+79881234567",
                "role": "guest"
            },
            {
                "id": 9,
                "name": "Новикова Татьяна Владимировна",
                "password": "master",
                "email": "tati2_example@gmail.ru",
                "phone_number": "+79991234567",
                "role": "guest"
            },
            {
                "id": 10,
                "name": "Федоров Андрей Алексеевич",
                "password": "master",
                "email": "andrey_example@gmail.ru",
                "phone_number": "+79901234567",
                "role": "guest"
            },
            {
                "id": 11,
                "name": "Иванов Иван",
                "password": "master",
                "email": "admin@gmail.ru",
                "phone_number": "+79992223341",
                "role": "admin"
            }
        ]

    }
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



