import datetime

from flask import render_template, request, redirect, url_for

from app import app, manager
from app.handlers.contentMasters import ContentMasters
from app.handlers.contentServices import ContentServices
from app.handlers.contentGeneral import ContentGeneral
from app.handlers.contentAdmin import AppointmentsTable

@app.route('/start')
def start():

    static_content = ContentGeneral.get(manager=manager)

    return render_template('start/index.html', static_content=static_content)


@app.route('/starts', methods=['POST', 'GET'])
def starts():



    if request.method == 'POST':

        form_data = request.form

        print(form_data)

        if 'update_appointment' in form_data.keys():
            AppointmentsTable.update()





    static_content = {
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
            {"type": "Стрижки", "name": "Стрижка одной насадкой", "cost": "700"},
            {"type": "Стрижки", "name": "Стрижка модельная", "cost": "1200"},
            {"type": "Стрижки", "name": "Стрижка фэйд", "cost": "1000"},
            {"type": "Стрижки", "name": "Стрижка детская (от 6 до 9 лет)", "cost": "700"},
            {"type": "Солярий", "name": "Премиум", "cost": "200"},
            {"type": "Солярий", "name": "Стандарт", "cost": "100"},
            {"type": "Шугаринг", "name": "Бикини", "cost": "900"},
            {"type": "Шугаринг", "name": "Бёдра", "cost": "600"},
            {"type": "Шугаринг", "name": "Ноги", "cost": "1500"},
            {"type": "Шугаринг", "name": "Руки", "cost": "1000"},
            {"type": "Шугаринг", "name": "Лицо", "cost": "700"},
            {"type": "Шугаринг", "name": "Ягодицы", "cost": "300"}
        ],
        "masters": [
            {
                "id": 111,
                "name": "Татьяна",
                "email": "tati_master@gmail.ru",
                "phone_number": "+79992223342",
                "work_schedule": "110110110110110110110110110110",
                "type": "Стрижки",
            },
            {
                "id": 222,
                "name": "Марина ",
                "email": "mari_master@gmail.ru",
                "phone_number": "+79992223343",
                "work_schedule": "110110110110110110110110110110",
                "type": "Ногти",
            },
            {
                "id": 333,
                "name": "Анна",
                "email": "anna_master@gmail.ru",
                "phone_number": "+79992223344",
                "work_schedule": "011011011011011011011011011011",
                "type": "Ногти",
            },
            {
                "id": 444,
                "name": "Светлана",
                "email": "sveta_master@gmail.ru",
                "phone_number": "+79992223345",
                "work_schedule": "011011011011011011011011011011",
                "type": "Стрижки",
            },
            {
                "id": 555,
                "name": "Дмитрий ",
                "email": "dima_master@gmail.ru",
                "phone_number": "+79992223346",
                "work_schedule": "101101101101101101101101101101",
                "type": "Стрижки",
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
                "type": "Шугаринг",
            },
            {
                "id": 888,
                "name": "Любава",
                "email": "luba_master@gmail.ru",
                "phone_number": "+79992223349",
                "work_schedule": "101101101101101101101101101101",
                "type": "Ногти",
            },
            {
                "id": 999,
                "name": "Солярий",
                "email": "",
                "phone_number": "",
                "work_schedule": "",
                "type": "Солярий",
            }
        ],
        "contentttt": [
            {
                "id": 1,
                "master_id": 111,
                "service_name": '',
                "page": "masters",
                "type": "img",
                "extra": "img/masters/Tatyana.jpg"
            },
            {
                "id": 2,
                "master_id": 111,
                "service_name": '',
                "page": "masters",
                "type": "text",
                "extra": "парикмахер"
            },
            {
                "id": 3,
                "master_id": 222,
                "service_name": '',
                "page": "masters",
                "type": "img",
                "extra": "img/masters/svetlana.jpg"
            },
            {
                "id": 4,
                "master_id": 222,
                "service_name": '',
                "page": "masters",
                "type": "text",
                "extra": "топ мастер-парикмахер"
            },
            {
                "id": 5,
                "master_id": 333,
                "service_name": '',
                "page": "masters",
                "type": "img",
                "extra": "img/masters/Dima.jpg"
            },
            {
                "id": 6,
                "master_id": 333,
                "service_name": '',
                "page": "masters",
                "type": "text",
                "extra": "барбер"
            },
            {
                "id": 7,
                "master_id": 444,
                "service_name": '',
                "page": "masters",
                "type": "img",
                "extra": "img/masters/Marina.jpg"
            },
            {
                "id": 8,
                "master_id": 444,
                "service_name": '',
                "page": "masters",
                "type": "text",
                "extra": "мастер ногтевого сервиса"
            },
            {
                "id": 9,
                "master_id": 555,
                "service_name": 'null',
                "page": "masters",
                "type": "img",
                "extra": "img/masters/Anna.jpg"
            },
            {
                "id": 10,
                "master_id": 555,
                "service_name": 'null',
                "page": "masters",
                "type": "text",
                "extra": "мастер ногтевого сервиса"
            },
            {
                "id": 11,
                "master_id": 666,
                "service_name": 'null',
                "page": "masters",
                "type": "img",
                "extra": "img/masters/alena.jpg"
            },
            {
                "id": 12,
                "master_id": 666,
                "service_name": 'null',
                "page": "masters",
                "type": "text",
                "extra": "Шугаринг"
            },
            {
                "id": 13,
                "master_id": 777,
                "service_name": 'null',
                "page": "masters",
                "type": "img",
                "extra": "img/masters/Efros.jpg"
            },
            {
                "id": 14,
                "master_id": 777,
                "service_name": 'null',
                "page": "masters",
                "type": "text",
                "extra": "Бровист"
            },
            {
                "id": 15,
                "master_id": 888,
                "service_name": 'null',
                "page": "masters",
                "type": "img",
                "extra": "img/masters/Lubava.jpg"
            },
            {
                "id": 16,
                "master_id": 888,
                "service_name": '',
                "page": "masters",
                "type": "text",
                "extra": "Бровист"
            },
            {
                "id": 17,
                "master_id": 'null',
                "service_name": 'null',
                "page": "masters",
                "type": "text",
                "extra": "Бровист"
            },
            {
                "id": 18,
                "master_id": 'null',
                "service_name": 'null',
                "page": "main",
                "type": "img",
                "extra": "img/main/haircut_2.gif"
            },
            {
                "id": 19,
                "master_id": 'null',
                "service_name": 'null',
                "page": "main",
                "type": "img",
                "extra": "img/main/haircut_3.gif"
            },
            {
                "id": 20,
                "master_id": 'null',
                "service_name": 'null',
                "page": "main",
                "type": "img",
                "extra": "img/main/haircut_1.gif"
            },
            {
                "id": 21,
                "master_id": 'null',
                "service_name": 'null',
                "page": "services",
                "type": "text",
                "extra": "Титульная страница раздела Услуг"
            },
            {
                "id": 22,
                "master_id": 'null',
                "service_name": "Ресницы и брови",
                "page": "services",
                "type": "img",
                "extra": "img/services/lash_brow.jpg"
            },
            {
                "id": 23,
                "master_id": 'null',
                "service_name": "Окрашивание",
                "page": "services",
                "type": "img",
                "extra": "img/services/coloring.jpg"
            },
            {
                "id": 24,
                "master_id": 'null',
                "service_name": "Ногтевой сервис",
                "page": "services",
                "type": "img",
                "extra": "img/services/nails.jpg"
            },
            {
                "id": 25,
                "master_id": 'null',
                "service_name": "Стрижки",
                "page": "services",
                "type": "img",
                "extra": "img/services/haircut.jpg"
            },
            {
                "id": 26,
                "master_id": 'null',
                "service_name": "Солярий",
                "page": "services",
                "type": "img",
                "extra": "img/services/solarium.jpg"
            },
            {
                "id": 27,
                "master_id": '',
                "service_name": "Шугаринг",
                "page": "services",
                "type": "img",
                "extra": "img/services/sugaring.jpg"
            }

        ],
        "appointments": [
            {
                "id": 1,
                "user_id": "Иванова Анна Михайловна",
                "master_id": "Татьяна",
                "service_name": "Окрашивание прикорневое",
                "date_time": "2024-01-10 10:00:00",
                "extra": "+79261234567",
            },
            {
                "id": 2,
                "user_id": "Петров Сергей Викторович",
                "master_id": "Татьяна",
                "service_name": "Сложное окрашивание",
                "date_time": "2024-01-10 11:00:00",
                "extra": "+79181234567",
            },
            {
                "id": 3,
                "user_id": "Смирнова Екатерина Александровна",
                "master_id": "Татьяна",
                "service_name": "Стрижка каскад",
                "date_time": "2024-01-10 10:00:00",
                "extra": "+79031234567",
            },
            {
                "id": 4,
                "user_id": "Кузнецов Дмитрий Иванович",
                "master_id": "Татьяна",
                "service_name": "Окрашивание прикорневое",
                "date_time": "2024-01-10 12:00:00",
                "extra": "+79341234567",
            },
            {
                "id": 5,
                "user_id": "Васильева Ольга Петровна",
                "master_id": "Татьяна",
                "service_name": "Стрижка фэйд",
                "date_time": "2024-01-10 10:00:00",
                "extra": "+79551234567",
            },
            {
                "id": 6,
                "user_id": "Попов Александр Михайлович",
                "master_id": "Любава",
                "service_name": "Маникюр дизайнерский",
                "date_time": "2024-01-10 10:00:00",
                "extra": "+79661234567",
            },
            {
                "id": 7,
                "user_id": "Соколова Елена Сергеевна",
                "master_id": "Анна",
                "service_name": "Маникюр без покрытия",
                "date_time": "2024-01-10 11:00:00",
                "extra": "+79771234567",
            },
            {
                "id": 8,
                "user_id": "Михайлов Игорь Валерьевич",
                "master_id": "Анна",
                "service_name": "Маникюр дизайнерский",
                "date_time": "2024-01-10 11:00:00",
                "extra": "+79881234567",
            },
            {
                "id": 9,
                "user_id": "Новикова Татьяна Владимировна",
                "master_id": "Алена",
                "service_name": "Бёдра",
                "date_time": "2024-01-10 10:00:00",
                "extra": "+79991234567"
            },
            {
                "id": 10,
                "user_id": "Федоров Андрей Алексеевич",
                "master_id": "Светлана",
                "service_name": "Наращивание ресниц",
                "date_time": "2024-01-10 10:00:00",
                "extra": "+79901234567",
            },
            {
                "id": 11,
                "user_id": "Иванов Иван",
                "master_id": "Светлана",
                "service_name": "Ламинирование ресниц",
                "date_time": "2024-01-10 11:00:00",
                "extra": "+79992223341",
            },
            {
                "id": 2,
                "user_id": "Петров Сергей Викторович",
                "master_id": "Солярий",
                "service_name": "Стандарт",
                "date_time": "2024-01-10 12:00:00",
                "extra": "+79181234567",
            },
            {
                "id": 1,
                "user_id": "Иванова Анна Михайловна",
                "master_id": "Солярий",
                "service_name": "Премиум",
                "date_time": "2024-01-10 13:00:00",
                "extra": "+79261234567",
            },


        ],
    }





    return render_template('admin/start.html', static_content=static_content)


@app.route('/masters')
def masters():
    masters_name = request.values.get('masters_name')

    static_content = ContentMasters.get(
        manager=manager,
        masters_name=masters_name
    )

    return render_template('masters/index.html',
                           static_content=static_content)


@app.route('/services')
def services():
    service_name = request.values.get('service_name')

    static_content = ContentServices.get(
        manager=manager,
        services_name=service_name
    )

    return render_template('services/index.html',
                           static_content=static_content)


@app.route('/auth')
def auth():
    return render_template('auth/index.html')


@app.route('/appointment', methods=['get', 'post'])
def appointment():



















    first_name = request.form.get('first_name')
    print(first_name)













    date = datetime.date.today()

    service_type = 'Выберите услугу'
    time_hidden_kostil_yopta = 'Выберите время'
    first_name = ''
    last_name = ''
    phone_input = ''
    email_input = ''
    masters_list = []

    if request.method == "POST":

        available_time = request.form.get('available_time')
        service_name = request.form.get('service_name')
        print(request.form.get('service_type'))

        if (available_time != None
                and service_name != None):
            print('ssssssssssssssss')
            print(available_time)

            return redirect(
                url_for('я еще не придумал сори ',
                        available_time=available_time,
                        service_name=service_name, )
            )


        date = request.form.get('date')
        service_type = request.form.get('service_type')
        time_hidden_kostil_yopta = request.form.get('time_hidden_kostil_yopta')

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        phone_input = request.form.get('phone_input')
        email_input = request.form.get('email_input')

        return render_template('appointment/index.html',
                               date=date,
                               service_type=service_type,
                               time_hidden_kostil_yopta=time_hidden_kostil_yopta,
                               last_name=last_name,
                               first_name=first_name,
                               phone_input=phone_input,
                               email_input=email_input,
                               masters_list=masters_list)
    else:
        return render_template('appointment/index.html',
                               date=date,
                               service_type=service_type,
                               time_hidden_kostil_yopta=time_hidden_kostil_yopta,
                               last_name=last_name,
                               first_name=first_name,
                               phone_input=phone_input,
                               email_input=email_input,
                               masters_list=masters_list)


@app.route('/dev', methods=['get', 'post'])
def dev():
    date = datetime.date.today()
    some_text = 'пусто'

    if request.method == "POST":
        date = request.form.get('date')
        some_text = str(date)
        return render_template('_tests/datetest.html', date=date, some_text=some_text)
    else:
        return render_template('_tests/datetest.html', date=date, some_text=some_text)


"""
@app.route('/masters/<masters_name>')
def masters_grid(masters_name):

    masters_spec = {'haircut', 'sugaring', 'coloring', 'nails', 'eyebrows'}

    if masters_name in masters_spec:
        return render_template('masters/index.html', masters_name=masters_name)



@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/prod')
def product():
    return render_template('index_product.html')
"""