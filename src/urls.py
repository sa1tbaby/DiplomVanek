from flask import Flask, render_template, request, session, redirect, url_for
from logging import basicConfig
from src.config import Settings
from src.config import LogSettings
from src.database.page_handles import AdminContent, UiContent

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
ui_content = UiContent(settings)

@app.route('/main')
def main():
    page_anchor = ['carousel', 'carousel_active', 'information_block']

    ui_content.get('asdd')

    static_content = {
        'carousel': [],
        'carousel_active': '',
        'information_block': []
    }

    return render_template('main.html', static_content=static_content)


@app.route('/services')
def services():
    page_anchor = ['header', 'information', 'services_list']
    efaf = request.base_url[len(request.host_url):]


    static_content = {
        'header': '',
        'information': '',
        'services_list': []
    }

    return render_template('services.html', static_content=static_content)


@app.route('/masters')
def masters():
    page_anchor = ['header', 'information', 'masters_list']

    static_content = {
        'header': '',
        'information': '',
        'masters_list': []
    }

    return render_template('masters.html', static_content=static_content)


@app.route('/appointment/<int:step>', methods=['get', 'post'])
def appointment(step: int):
    page_anchor = ['services_list']

    if request.method == 'GET':

        static_content = {
            'services_list': []
        }

        return render_template('appointment/step1.html', static_content=static_content)

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

                return render_template('appointment/step1.html', static_content=static_content)

            case 3:
                static_content = {

                }

                return render_template('appointment/step1.html', static_content=static_content)


@app.route('/auth', methods=['get', 'post'])
def auth():
    pass


@app.route('/admin/<point>', methods=['GET', 'POST'])
def admin(point):

    match request.args.get('option'):
        case 'update':
            result = admin_content.update(id=request.form.get('id'), data=request.form)

        case 'insert':
            result = admin_content.insert(data=request.form)

        case 'delete':
            result = admin_content.delete(id=request.args.get('id'))

        case 'schedule':

            result = redirect(
                location=url_for(endpoint='schedule',
                                 master_id=request.args.get('master_id'),
                                 master_schedule=request.args.get('schedule')),
                code=302
            )

    result = render_template(template_name_or_list=f'admin/{point}.html',
                             static_content=admin_content.get(point), asdasd=None)

    return result

@app.route('/admin/schedule/<master_id>')
def schedule(master_id):
    return str(master_id)

@app.route('/base')
def base():

    static_content = {
        'carousel': [],
        'carousel_active': [],
        'information_block': []
    }

    return render_template('admin/admin_base.html')