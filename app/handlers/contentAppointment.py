import datetime

from sqlalchemy.orm import Session
from sqlalchemy import insert, update, delete, select
from models.declarativeModels import Masters, ContentType, Services, Appointments
from app.handlers.alchemyManager import AlchemyManager
from models.schemas import time_list


class ContentAppointments:

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
            static_content,
            user_id
    ):
        try:
            with Session(bind=manager.engine) as session:

                session.execute(insert(Appointments).values({
                    'user_id': user_id,
                    'master_id': static_content.get('master_id'),
                    'service_name': static_content.get('service_name'),
                    'date_time': static_content.get('date'),
                    'extra': ''
                }))

                session.commit()

            result = True

        except Exception as exc:
            print(exc)
            result = False

        finally:
            return result