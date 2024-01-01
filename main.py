import datetime
import os.path

from flask import Flask, render_template, request, redirect
import os.path

cur_dir = os.path.curdir
app = Flask(__name__)

@app.route('/carousel')
def main():
    menu_list = [
        {
            'number': 1,
            'src': 'img/menu/menu_coloring.jpg',
            'title': 'Услуги колориста'
        },
        {
            'number': 2,
            'src': 'img/menu/menu_haircut.jpg',
            'title': 'Услуги парикмахера'
        },
        {
            'number': 3,
            'src': 'img/menu/menu_lash_brow.jpg',
            'title': 'Услуги бровиста'
        },
        {
            'number': 4,
            'src': 'img/menu/menu_nails.jpg',
            'title': 'Услуги ногтевого сервиса'
        },
        {
            'number': 5,
            'src': 'img/menu/menu_nails_2.jpg',
            'title': 'Услуги ногтевого сервиса'
        },
        {
            'number': 6,
            'src': 'img/menu/menu_solarium.jpg',
            'title': 'Услуги солярия'
        },
        {
            'number': 7,
            'src': 'img/menu/menu_sufaring.jpg',
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

@app.route('/services')
def services():
    return render_template('services/index.html')

@app.route('/masters')
def masters():
    return render_template('masters/index.html')

@app.route('/auth')
def auth():
    return render_template('auth/index.html')

@app.route('/appointment',  methods=['get', 'post'])
def appointment():
    date = datetime.date.today()
    some_text = 'пусто'
    time_list = [
        {
            "time": "09:00"
        },
        {
            "time": "10:00"
        },
        {
            "time": "11:00"
        },
        {
            "time": "12:00"
        },
        {
            "time": "13:00"
        },
        {
            "time": "14:00"
        },
        {
            "time": "15:00"
        },
        {
            "time": "16:00"
        },
    ]
    service_type = 'Выберите услугу'

    if request.method == "POST":
        date = request.form.get('date')
        service_type = request.form.get('service_type')
        print(request.form)
        some_text = str(date)
        return render_template('appointment/index.html',
                               date=date,
                               some_text=some_text,
                               time_list=time_list,
                               service_type=service_type)
    else:
        return render_template('appointment/index.html', date=date, some_text=some_text,
                               time_list=time_list,service_type=service_type)






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


