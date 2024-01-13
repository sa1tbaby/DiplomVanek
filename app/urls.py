import datetime

from flask import render_template, request

from app import app, manager
from app.handlers.contentMasters import ContentMasters
from app.handlers.contentServices import ContentServices
from app.handlers.contentGeneral import ContentGeneral


@app.route('/start')
def start():

    static_content = ContentGeneral.get(manager=manager)

    return render_template('start/step1.html', static_content=static_content)


@app.route('/masters')
def masters():
    masters_name = request.values.get('masters_name')

    static_content = ContentMasters.get(
        manager=manager,
        masters_name=masters_name
    )

    return render_template('masters/step1.html',
                           static_content=static_content)


@app.route('/services')
def services():
    service_name = request.values.get('service_name')

    static_content = ContentServices.get(
        manager=manager,
        services_name=service_name
    )

    return render_template('services/step1.html',
                           static_content=static_content)


@app.route('/auth')
def auth():
    return render_template('auth/step1.html')


@app.route('/appointment', methods=['get', 'post'])
def appointment():
    date = datetime.date.today()


    service_type = 'Выберите услугу'
    time_hidden_kostil_yopta = 'Выберите время'
    first_name = ''
    last_name = ''
    phone_input = ''
    email_input = ''

    if request.method == "POST":

        date = request.form.get('date')
        service_type = request.form.get('service_type')
        time_hidden_kostil_yopta = request.form.get('time_hidden_kostil_yopta')

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        phone_input = request.form.get('phone_input')
        email_input = request.form.get('email_input')

        return render_template('appointment/step1.html',
                               date=date,
                               service_type=service_type,
                               time_hidden_kostil_yopta=time_hidden_kostil_yopta,
                               last_name=last_name,
                               first_name=first_name,
                               phone_input=phone_input,
                               email_input=email_input)
    else:
        return render_template('appointment/step1.html',
                               date=date,
                               service_type=service_type,
                               time_hidden_kostil_yopta=time_hidden_kostil_yopta,
                               last_name=last_name,
                               first_name=first_name,
                               phone_input=phone_input,
                               email_input=email_input)


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
        return render_template('masters/step1.html', masters_name=masters_name)



@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/prod')
def product():
    return render_template('index_product.html')
"""