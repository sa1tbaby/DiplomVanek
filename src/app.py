from logging import basicConfig, getLogger

from flask import Flask, render_template, request
from src.configs.config import Settings, LogSettings
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

settings = Settings()
log_settings = LogSettings()

basicConfig(
    filename=log_settings.FILE_NAME,
    filemode=log_settings.FILE_MODE,
    level=log_settings.LOG_LEVEL,
    format=log_settings.LOG_FORMAT
)




@app.route('/')
def main():

    static_content = {
        "carousel": [],
        "carousel_active": "",
        "information_block": []
    }

    return render_template('ui/main.html', static_content=static_content)


@app.route('/services')
def services():

    static_content = {
        "header": "",
        "information": "",
        "services_list": []
    }

    return render_template('ui/services.html', static_content=static_content)


@app.route('/masters')
def masters():

    static_content = {
        "header": "",
        "information": "",
        "masters_list": []
    }

    return render_template('ui/masters.html', static_content=static_content)


@app.route('/appointment/<int:step>', methods=['get', 'post'])
def appointment(step: int):

    if request.method == "GET":

        static_content = {
            "services_list": []
        }

        return render_template('ui/appointment/step1.html', static_content=static_content)

    elif request.method == "POST":

        match step:

            case 2:
                client_request = {
                    "service_type": request.form.get('service_type'),
                    "date_input": request.form.get('date_input'),
                }

                static_content = {
                    "masters_list": {}
                }

                return render_template('ui/appointment/step1.html', static_content=static_content)

            case 3:
                static_content = {

                }

                return render_template('ui/appointment/step1.html', static_content=static_content)


@app.route('/base')
def base():

    static_content = {
        "carousel": [],
        "carousel_active": [],
        "information_block": []
    }

    return render_template('base.html')