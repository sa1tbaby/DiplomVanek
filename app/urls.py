import datetime

from flask import render_template, request, redirect, url_for

from app import app, manager
from app.handlers.contentMasters import ContentMasters
from app.handlers.contentServices import ContentServices
from app.handlers.contentGeneral import ContentGeneral
from app.handlers.contentAdmin import AdminOperations, AdminUsers, AdminAppointments
from app.handlers.contentAuth import AuthLogin
from app.handlers.contentAppointment import ContentAppointments
from app.handlers.contentProfile import ContentProfile
from models.declarativeModels import Appointments, Services, Masters, Content, Users
from models.schemas import services_name_dict, con_text

csrf = True
user_id = True
user_role = True
@app.route('/start')
def start():

    static_content = ContentGeneral.get(manager=manager)
    static_content.update(
        us=con_text.get('us'),
        extra=con_text.get('extra')
    )

    return render_template('start/index.html', static_content=static_content, csrf=csrf)

@app.route('/admin/users', methods=['POST', 'GET'])
def admin_users():

    status = ''
    button_method = request.form.get('button_method')
    users_list = AdminUsers.get(manager)

    match request.method:

        case "POST":

            user_value = {
                'name': str(request.form.get('name')),
                'email': str(request.form.get('email')),
                'password': str(request.form.get('password')),
                'phone_number': str(request.form.get('phone_number')),
                'role': str(request.form.get('user_role')),
            }

            if button_method == 'insert':
                status = AdminUsers.insert(manager, user_value)

            elif button_method == 'update':
                user_value.update(
                    id=str(request.form.get('id'))
                )
                status = AdminUsers.update(manager, user_value)

            elif button_method == 'delete':
                id = request.form.get('id')
                status = AdminUsers.delete(manager, id)

            users_list = AdminUsers.get(manager)

    return render_template('admin/users.html', users=users_list, status=status, csrf=csrf)



@app.route('/admin/appointments', methods=['POST', 'GET'])
def admin_appointments():

    status = ''
    static_content = {}
    form_content = {
        'date': datetime.date.today(),
        'button_method': request.form.get('button_method')
    }

    if request.method == 'GET':

        static_content.update(
            **AdminAppointments.get(manager=manager),
            service_types=services_name_dict.values()
        )

        return render_template('admin/appointments.html',
                               status=status,
                               static_content=static_content,
                               form_content=form_content, csrf=csrf)

    if request.method == 'POST':

        form_content.update(
            user_name=request.form.get('user_name'),
            service_type=request.form.get('service_type'),
            date=request.form.get('date')
        )

        match form_content.get('button_method'):

            case 'continue':

                static_content.update(
                    appointments='False',
                    available_time=''
                )

                form_content.update(
                    master_id=request.form.get('master_id'),
                    service_name=request.form.get('service_name'),
                    button_method=request.form.get('button_method'),
                )

                masters = AdminAppointments.get_masters(
                    manager=manager,
                    service_type=form_content.get('service_type'),
                    date=form_content.get('date')
                )

                return render_template('admin/appointments.html',
                                       status=status,
                                       masters=masters,
                                       static_content=static_content,
                                       form_content=form_content, csrf=csrf)

            case 'insert':

                form_content.update(
                    user_name=request.form.get('user_name'),
                    service_name=request.form.get('service_name'),
                    service_type=request.form.get('service_type'),
                    master_id=request.form.get('master_id'),
                    appo_time=request.form.get('available_time'),
                    date=request.form.get('date') + ' ' + request.form.get('available_time')
                )

                status = AdminAppointments.insert(manager, form_content)

                return redirect(url_for('admin_appointments'))


            case 'update':

                form_content = {
                    'id': request.form.get('id'),
                    'user_id': request.form.get('user_id'),
                    'master_id': request.form.get('master_id'),
                    'service_name': request.form.get('service_name'),
                    'date_time': request.form.get('date_time'),
                    'extra': request.form.get('extra')
                }

                status = AdminAppointments.update(manager, form_content)

                return redirect(url_for('admin_appointments'))

            case 'delete':

                id = request.form.get('id')

                status = AdminAppointments.delete(manager, id)

                return redirect(url_for('admin_appointments'))

@app.route('/admin/masters', methods=['POST', 'GET'])
def admin_masters():
    method = request.args.get('button_method')
    static_content = {}
    match method:

        case 'update':
            pass

        case 'insert':
            pass

        case 'delete':
            pass

    return render_template('admin/masters.html', static_content=static_content, csrf=csrf)

@app.route('/admin/general', methods=['POST', 'GET'])
def admin_general():
    method = request.args.get('button_method')
    static_content = {}

    match method:

        case 'update':
            pass

        case 'insert':
            pass

        case 'delete':
            pass

    return render_template('admin/general.html', static_content=static_content, csrf=csrf)

@app.route('/admin/services', methods=['POST', 'GET'])
def admin_services():
    method = request.args.get('button_method')

    static_content = ''
    match method:

        case 'update':
            pass

        case 'insert':
            pass

        case 'delete':
            pass

    return render_template('admin/services.html', static_content=static_content, csrf=csrf)



@app.route('/admin', methods=['POST', 'GET'])
def admin():
    user = ContentProfile.get(manager, user_id)
    return render_template('admin/profile.html', csrf=csrf, user=user, user_id=user.id, user_role=user.role)


@app.route('/masters')
def masters():

    service_name = request.values.get('service_name')

    print(service_name)

    static_content = ContentMasters.get(
        manager=manager,
        service_name=service_name
    )
    static_content.update(
        extra=con_text.get('service_name')
    )

    return render_template('masters/index.html',
                           static_content=static_content, csrf=csrf)


@app.route('/services')
def services():
    service_name = request.values.get('service_name')

    static_content = ContentServices.get(
        manager=manager,
        services_name=service_name
    )

    static_content.update(
        extra=con_text.get('service_name')
    )

    return render_template('services/index.html',
                           static_content=static_content, csrf=csrf)

@app.route('/profile', methods=['get', 'post'])
def profile():


    user = ContentProfile.get(manager, user_id)
    static_content = ContentProfile.get_app(manager, user_id)

    if user_role == 'admin':
        return redirect(url_for('admin'))



    return render_template('profile/index.html', csrf=csrf, user=user, static_content=static_content, user_id=user.id, user_role=user.role)


@app.route('/auth', methods=['get', 'post'])
def auth():
    global csrf
    csrf = False
    global user_id
    global user_role

    if request.args.get('logout') == '1':
        csrf = False

    button_method = request.form.get('button_method')

    if button_method == 'logout':
        csrf = False

    if request.method == 'POST':

        email = request.form.get('email')

        user = AuthLogin.get(manager, email)

        if not user:
            err = 'Не верный логин или пароль '
            return render_template('auth/index.html', csrf=csrf, err=err)
        else:
            csrf = True
            user_id = user.id
            user_role = user.role
            if user_role == 'admin':
                return redirect(url_for('admin'))

            return redirect(url_for('profile', user_id=user.id, user_role=user.role))


    return render_template('auth/index.html', csrf=csrf)


@app.route('/appointment', methods=['get', 'post'])
def appointment():

    static_content = {}
    static_content.update(
        services_list=services_name_dict.values(),
        date_input=datetime.date.today(),
        service_type='Выберите тип услуги',
        button_method=False
    )
    masters = {
    }
    user_id = 999

    if request.method == "POST":

        static_content.update(
            first_name=request.form.get('first_name'),
            last_name=request.form.get('last_name'),
            phone_input=request.form.get('phone_input'),
            email_input=request.form.get('email_input'),
            service_type=request.form.get('service_type'),
            button_method=request.form.get('button_method'),
            date_input=request.form.get('date_input')
        )

        if static_content.get('button_method') == 'check':

            masters = ContentAppointments.get_masters(
                manager=manager,
                service_type=static_content.get('service_type'),
                date=static_content.get('date_input')
            )


            return render_template('appointment/index.html',
                               static_content=static_content,
                               masters=masters, csrf=csrf)

        elif static_content.get('button_method') == 'insert':

            static_content.update(
                name=request.form.get('first_name') + ' ' + request.form.get('last_name'),
                service_name=request.form.get('service_name'),
                master_id=request.form.get('master_id'),
                appo_time=request.form.get('available_time'),
                date=request.form.get('date_input') + ' ' + request.form.get('available_time')
            )

            status = ContentAppointments.insert(manager, static_content, user_id)

            return render_template('appointment/index.html',
                                   static_content=static_content,
                                   masters=masters,
                                   status=status, csrf=csrf)

    else:
        return render_template('appointment/index.html',
                               static_content=static_content,
                               masters=masters, csrf=csrf)


@app.route('/dev', methods=['get', 'post'])
def dev():
    date = datetime.date.today()
    some_text = 'пусто'

    if request.method == "POST":
        date = request.form.get('date')
        some_text = str(date)
        return render_template('_tests/datetest.html', date=date, some_text=some_text, csrf=csrf)
    else:
        return render_template('_tests/datetest.html', date=date, some_text=some_text, csrf=csrf)


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