from sqlalchemy.orm import Session
from sqlalchemy import insert, update, delete, select
from models.declarativeModels import Appointments, Users, ContentType, Masters, Services
from app.handlers.alchemyManager import AlchemyManager
from models.schemas import services_name_dict, time_list
import datetime


class AuthLogin:

    @staticmethod
    def get(
            manager: AlchemyManager,
            name
    ):
        try:

            with Session(bind=manager.engine) as session:
                users = session.query(Users).filter(
                    Users.email == name
                ).one()
        except Exception as exc:
            users = False

        finally:
            return users

    @staticmethod
    def _check_values(data: dict):
        for item in data.values():
            if item == '':
                return False
        return data
