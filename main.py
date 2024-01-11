import datetime
import os.path

from flask import Flask, render_template, request, redirect, url_for
import os.path

cur_dir = os.path.curdir
app = Flask(__name__)

@app.route('/carousel')
def main():
    menu_list = [
        {
            'number': 1,
            'src': 'img/services/coloring.jpg',
            'title': 'Услуги колориста'
        },
        {
            'number': 2,
            'src': 'img/services/haircut.jpg',
            'title': 'Услуги парикмахера'
        },
        {
            'number': 3,
            'src': 'img/services/lash_brow.jpg',
            'title': 'Услуги бровиста'
        },
        {
            'number': 4,
            'src': 'img/services/nails.jpg',
            'title': 'Услуги ногтевого сервиса'
        },
        {
            'number': 5,
            'src': 'img/services/nails_2.jpg',
            'title': 'Услуги ногтевого сервиса'
        },
        {
            'number': 6,
            'src': 'img/services/solarium.jpg',
            'title': 'Услуги солярия'
        },
        {
            'number': 7,
            'src': 'img/services/sugaring.jpg',
            'title': 'Услуги шугаринга'
        },
    ]
    return render_template('services_carousel.html', menu_list=menu_list)

@app.route('/start')
def start():
    return render_template('start/index.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/prod')
def product():
    return render_template('index_product.html')





@app.route('/masters/<masters_name>')
def masters_grid(masters_name):

    masters_spec = {'haircut', 'sugaring', 'coloring', 'nails', 'eyebrows'}

    if masters_name in masters_spec:
        return render_template('masters/index.html', masters_name=masters_name)



@app.route('/masters')
def masters():
    masters_name = request.values.get('masters_name')

    masters_table = {
        'name': 'some_name',
        'title': 'some_title',
    }

    static_content = [
        {
            'name': 'some_name',
            'title': 'some_title',
            'link': 'img/masters/them1.jpg'
        },
        {
            'name': 'some_name',
            'title': 'some_title',
            'link': 'img/masters/them1.jpg'
        },
        {
            'name': 'some_name',
            'title': 'some_title',
            'link': 'img/masters/them1.jpg'
        },
    ]

    return render_template('masters/index.html',
                           masters_table=masters_table,
                           static_content=static_content)

@app.route('/services')
def services():
    service_name = request.values.get('service_name')


    services_table = {
        'name': 'some_name',
        'title': 'some_title',
    }

    static_content = [
        {
            'name': 'some_name',
            'title': 'some_title'
        },
        {
            'name': 'some_name',
            'title': 'some_title'
        },
        {
            'name': 'some_name',
            'title': 'some_title'
        },
    ]

    return render_template('services/index.html',
                           services_table=services_table,
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


if __name__ == '__main__':
    app.run(debug=True)



