from sqlalchemy.orm import Session
from sqlalchemy import insert, update, delete, select
from models.declarativeModels import Appointments, Users, ContentType, Masters, Services
from app.handlers.alchemyManager import AlchemyManager
from models.schemas import services_name_dict, time_list
import datetime

class AdminOperations:
    def get(
            manager: AlchemyManager,
    ):
        pass

class AdminUsers:

    @staticmethod
    def get(
            manager: AlchemyManager,
    ):
        try:
            with Session(bind=manager.engine) as session:
                users = session.query(Users)


        except:
            users = False

        finally:
            return users

    @staticmethod
    def insert(
            manager: AlchemyManager,
            data: dict
    ):
        try:

            if not AdminUsers._check_values(data):
                raise

            stmt = insert(Users).values(data)

            with Session(bind=manager.engine) as session:
                session.execute(stmt)
                session.commit()

        except:
            return "Введите корректные данные"

        else:
            return 'Успшено'

    @staticmethod
    def update(
            manager: AlchemyManager,
            data: dict
    ):
        try:
            if not AdminUsers._check_values(data):
                raise

            stmt = update(Users).where(Users.id == data.get('id')).values(data)

            with Session(bind=manager.engine) as session:

                session.execute(update(Users), [data])
                session.commit()
        except:
            return "Введите корректные данные"

        else:
            return 'Успшено'

    @staticmethod
    def delete(
            manager: AlchemyManager,
            id
    ):
        try:

            if id == '' or False:
                raise

            stmt = delete(Users).where(Users.id == int(id))

            with Session(bind=manager.engine) as session:

                session.execute(stmt)
                session.commit()
        except:
            return "Введите корректные данные"

        else:
            return 'Успшено'

    @staticmethod
    def _check_values(data: dict):
        for item in data.values():
            if item == '':
                return False
        return data


class AdminAppointments:
    @staticmethod
    def get(
            manager: AlchemyManager,
    ):

        with Session(bind=manager.engine) as session:
            appointments = session.query(Appointments).all()
            services = services_name_dict.values()
            users = session.query(Users)
            masters = session.query(Masters)

        with Session(bind=manager.engine) as session:
            for item in appointments:
                item.user_id = users.filter(Users.id == item.user_id).one().name
                item.master_id = masters.filter(Masters.id == item.master_id).one().name

        return {
            'appointments': appointments,
            'user_list': users.all(),
            'masters_list': masters.all(),
            'services_list': services
        }

    @staticmethod
    def get_masters(
            manager: AlchemyManager,
            service_type,
            date: str
    ):

        day = str(date)
        day = int(day[day.rfind('-')+1:])
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

        with Session(bind=manager.engine) as session:

            masters_list = session.query(Masters).filter(
                *[Masters.type == service_type]
            )

            services = session.query(Services).all()

            masters = []
            date = str(date)
            tmp_time = time_list
            available_time = []

            for master in masters_list:

                if master.work_schedule[day + 1] != '1':
                    continue

                tmp_cur_day = []

                for appointment in master.appointments_list:
                    if date in str(appointment.date_time):
                        cur_day = str(appointment.date_time)
                        cur_day = cur_day[cur_day.rfind(' ') + 1:]
                        tmp_cur_day.append(cur_day)

                for item in tmp_time:
                    if not item.get('time') in tmp_cur_day:
                        tmp = item.get('time')
                        tmp = tmp[:tmp.rfind(':')]
                        available_time.append(tmp)

                tmp_service = []

                for item in services:
                    if item.type == service_type:
                        print(item.name)
                        tmp_service.append(item.name)

                tmp_con = ''

                for item in master.content_list:
                    if item.type == ContentType.img:
                        print(item.extra)
                        tmp_con = item.extra

                masters.append(
                    {
                        'item': master,
                        'available_time': available_time,
                        'services': tmp_service,
                        'img': tmp_con
                    }
                )

        return masters
    @staticmethod
    def insert(
            manager: AlchemyManager,
            static_content
    ):
        try:
            with Session(bind=manager.engine) as session:

                user_id = session.query(Users).filter(
                    Users.name == static_content.get('user_name')
                ).one().id

                session.execute(insert(Appointments).values({
                    'user_id': user_id,
                    'master_id': static_content.get('master_id'),
                    'service_name': static_content.get('service_name'),
                    'date_time': static_content.get('date'),
                    'extra': static_content.get('service_type')
                }))

                session.commit()

            result = True

        except Exception as exc:
            print(exc)
            result = False

        finally:
            return result

    @staticmethod
    def update(
            manager: AlchemyManager,
            data: dict
    ):
        try:
            master_id = data.get('master_id')
            user_id = data.get('user_id')


            if not AdminUsers._check_values(data):
                raise

            with Session(bind=manager.engine) as session:
                data.update(
                    master_id=session.query(Masters).filter(Masters.name == master_id).one().id,
                    user_id=session.query(Users).filter(Users.name == user_id).one().id
                )

                session.execute(update(Appointments), [data])
                session.commit()

        except Exception as exc:
            print(exc)
            return "Введите корректные данные"

        else:
            return 'Успшено'

    @staticmethod
    def delete(
            manager: AlchemyManager,
            id
    ):
        try:

            if id == '' or False:
                raise

            stmt = delete(Appointments).where(Appointments.id == int(id))

            with Session(bind=manager.engine) as session:

                session.execute(stmt)
                session.commit()
        except:
            return "Введите корректные данные"

        else:
            return 'Успшено'
