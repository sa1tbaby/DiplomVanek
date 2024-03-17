from src.database.base import AlchemyFactory
from src.database.models.declarative_models import Media, Services, Masters, Appointments, Users, TABLES_DICT
from sqlalchemy import select, insert, update, delete
from flask import request
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

class UiContent(AlchemyFactory):

    def get(self, page_anchor):

        cur_page = request.base_url[len(request.host_url):]
        print('assssssssssssssssssssssssssssss')
        stmt = select(Media).where(Media.page == cur_page)


class AdminContent(AlchemyFactory):

    def __init__(self, point, settings):
        super().__init__(settings)

        self.table = TABLES_DICT.get(point)

    def select(self):

        stmt = select(self.table)

        return self._session(stmt)

    def insert(self, data):
        stmt = insert(self.table).returning(self.table)

        return self._session(stmt, data)

    def update(self, id: str, data):
        stmt = (
            update(self.table)
            .where(self.table.id == id)
            .values(data)
            .returning(self.table)
        )

        return self._session(stmt)

    def delete(self, id: str):
        stmt = (
            delete(self.table)
            .where(self.table.id == id)
            .returning(self.table)
        )

        return self._session(stmt)

    def _session(self, stmt, data=None):

        with self.session_factory() as session:
            result = session.scalars(
                stmt, data
            ).all()

        return result


