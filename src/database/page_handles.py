from src.database.base import AlchemyBase
from src.database.models.declarative_models import Media, Services, Masters, Appointments, Users, TABLES_DICT
from sqlalchemy import select, insert
from flask import request
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

class UiContent(AlchemyBase):

    def get(self, page_anchor):

        cur_page = request.base_url[len(request.host_url):]

        stmt = select(Media).where(Media.page == cur_page)


class AdminContent(AlchemyBase):

    def get(self, point):

        table = TABLES_DICT.get(point)

        with self.session_factory() as session:
            result = session.scalars(
                select(table)
            ).all()
        return result

    def insert(self, data):

        with self.session_factory() as session:
            result = session.scalars(
                insert()
            )

    def update(self):
        pass

    def delete(self, id):
        pass

    def schedule(self):
        pass
