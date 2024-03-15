from flask import Flask, render_template, request
from logging import basicConfig
from src.config import Settings
from src.config import LogSettings
from src.database.page_handles import AdminContent

settings = Settings()

log_settings = LogSettings()

basicConfig(
    filename=log_settings.FILE_NAME,
    filemode=log_settings.FILE_MODE,
    level=log_settings.LOG_LEVEL,
    format=log_settings.LOG_FORMAT
)

app = Flask(__name__)

admin_content = AdminContent(settings)

@app.route('/main')
def main():

    efaf = request.base_url[len(request.host_url):]

    static_content = {
        'carousel': [],
        'carousel_active': '',
        'information_block': []
    }

    return render_template('ui/main.html', static_content=static_content)


@app.route('/services')
def services():

    efaf = request.base_url[len(request.host_url):]


    static_content = {
        'header': '',
        'information': '',
        'services_list': []
    }

    return render_template('ui/services.html', static_content=static_content)


@app.route('/masters')
def masters():

    static_content = {
        'header': '',
        'information': '',
        'masters_list': []
    }

    return render_template('ui/masters.html', static_content=static_content)


@app.route('/appointment/<int:step>', methods=['get', 'post'])
def appointment(step: int):

    if request.method == 'GET':

        static_content = {
            'services_list': []
        }

        return render_template('ui/appointment/step1.html', static_content=static_content)

    elif request.method == 'POST':

        match step:

            case 2:
                client_request = {
                    'service_type': request.form.get('service_type'),
                    'date_input': request.form.get('date_input'),
                }

                static_content = {
                    'masters_list': {}
                }

                return render_template('ui/appointment/step1.html', static_content=static_content)

            case 3:
                static_content = {

                }

                return render_template('ui/appointment/step1.html', static_content=static_content)


@app.route('/auth', methods=['get', 'post'])
def auth():
    pass


@app.route('/admin/<point>', methods=['get', 'post'])
def admin(point):

    static_content = admin_content.get(point)

    return render_template(f'admin/{point}.html', static_content=static_content)


@app.route('/base')
def base():

    static_content = {
        'carousel': [],
        'carousel_active': [],
        'information_block': []
    }

    return render_template('admin/admin_base.html')