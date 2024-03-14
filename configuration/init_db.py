import json
from src.database.base import AlchemyBase
from src.database.models.declarative_models import *
from sqlalchemy import insert
import os.path

class InitDb(AlchemyBase):

    data = [
        'masters.json',
        'services.json',
        'users.json',
    ]
    tables = [
        Masters,
        Services,
        Users
    ]

    def init(self):
        BaseBd.metadata.create_all(self.engine)

        with self.session_factory() as session:

            for item, table in zip(InitDb.data, InitDb.tables):

                data_path = os.path.join('configuration', 'data', item)

                with open(data_path, 'r', encoding='UTF-8') as file:
                    tmp = json.load(file)

                session.execute(
                    insert(table),
                    tmp.get('data')
                )

            session.commit()

    def drop(self):
        BaseBd.metadata.drop_all(self.engine)


