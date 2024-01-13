import datetime

from flask import render_template, request
from app.handlers.alchemyManager import ContentMasters
from models.declarativeModels import Content
from app import app, Manager

@app.route('/start')
def start():

    gif = Manager.get_table_where(
        Content,
        [Content.page == 'main', Content.type == 'img']
    )

    info = Manager.get_table_where(
        Content,
        [Content.page == 'main/info', Content.type == 'text']
    )

    contacts = Manager.get_table_where(
        Content,
        [Content.page == "main/contacts", Content.type == "text"]
    )

    static_content = {
        "gif": gif,
        "info": info,
        "contacts": contacts
    }

    return render_template('start/index.html', static_content=static_content)


@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/prod')
def product():
    return render_template('index_product.html')







@app.route('/masters')
def masters():

    masters_name = request.values.get('masters_name')

    static_content = ContentMasters.get(masters_name, Manager)

    return render_template('masters/index.html',
                           static_content=static_content)

@app.route('/services')
def services():

    service_name = request.values.get('service_name')

    header = declarativeModels.services_name_dict.get(service_name)

    static_content = {
        "header": header,
        "title": Manager.get_table_where(
            declarativeModels.Content,
            [declarativeModels.Content.type == 'text',
             declarativeModels.Content.page == f'services/{service_name}']
        ),
        "content_list": Manager.get_table_where(
            declarativeModels.Services,
            [declarativeModels.Services.type == service_name]
        )
    }

    return render_template('services/index.html',
                           static_content=static_content)




@app.route('/auth')
def auth():
    return render_template('auth/index.html')

@app.route('/appointment',  methods=['get', 'post'])
def appointment():
    date = datetime.date.today()

    time_list = [
        {
            "id_time":"sad1",
            "time": "09:00"
        },
        {
            "id_time": "sad2",
            "time": "10:00"
        },
        {
            "id_time": "sad3",
            "time": "11:00"
        },
        {
            "id_time": "sad4",
            "time": "12:00"
        },
        {
            "id_time": "sad5",
            "time": "13:00"
        },
        {
            "id_time": "sad6",
            "time": "14:00"
        },
        {
            "id_time": "sad7",
            "time": "15:00"
        },
        {
            "id_time": "sad8",
            "time": "16:00"
        },
    ]
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

        return render_template('appointment/index.html',
                               date=date,
                               time_list=time_list,
                               service_type=service_type,
                               time_hidden_kostil_yopta=time_hidden_kostil_yopta,
                               last_name=last_name,
                               first_name=first_name,
                               phone_input=phone_input,
                               email_input=email_input)
    else:
        return render_template('appointment/index.html',
                               date=date,
                               time_list=time_list,
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
        return render_template('masters/index.html', masters_name=masters_name)


"""

if __name__ == '__main__':
    app.run(debug=True)



