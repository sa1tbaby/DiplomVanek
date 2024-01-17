from sqlalchemy.orm import Session
from sqlalchemy import insert, update, delete, select
from models.declarativeModels import Appointments, Users, ContentType, Masters, Services
from app.handlers.alchemyManager import AlchemyManager
from models.schemas import services_name_dict, time_list
import datetime


class ContentProfile:

    @staticmethod
    def get(
            manager: AlchemyManager,
            user_id
    ):
        try:
            user_id = int(user_id)
            with Session(bind=manager.engine) as session:
                user = session.query(Users).filter(
                    Users.id == user_id
                ).one()


        except:
            user = False

        finally:
            return user


    @staticmethod
    def get_app(
            manager: AlchemyManager,
            user_id
    ):
        try:
            with Session(bind=manager.engine) as session:
                content = session.query(Appointments).filter(
                    Appointments.user_id == int(user_id)
                ).all()
        except:
            content = False

        finally:
            return content

    @staticmethod
    def _check_values(data: dict):
        for item in data.values():
            if item == '':
                return False
        return data
