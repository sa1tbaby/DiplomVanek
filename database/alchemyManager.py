import os.path

from json import load

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import NullPool
from sqlalchemy.engine.base import Engine

from app.schemas import (
    ConfigDB,
    services_name_dict
)
from declarativeModels import (
    Content,
    Masters,
    ContentType
)

class BaseDB:

    def __init__(
            self,
            config_path: str,
            config_name: str
    ):
        self._config = self.getConfig(config_path=config_path, config_name=config_name)

    def getConfig(
            self,
            config_path: str,
            config_name: str
    ):
        cur_dir = os.path.abspath(os.path.curdir)
        config_path = os.path.join(cur_dir, config_path, config_name)

        with open(config_path, 'r') as file:
            self._config = ConfigDB(**load(file))

        return self._config


class CreateEngine(BaseDB):

    def getEngine(self) -> Engine:
        return create_engine(
            url=self._getConnStr(),
            echo=self._config.engine_echo,
            poolclass=NullPool
        )

    def _getConnStr(self) -> str:
        return (f'{self._config.dialect}+'
                f'{self._config.driver}://'
                f'{self._config.username}:'
                f'{self._config.password}@'
                f'{self._config.host}:'
                f'{self._config.port}/'
                f'{self._config.database}')


class AlchemyManager(CreateEngine):

    def __init__(
            self,
            config_path='Configs',
            config_name='ConfigDB.json'
    ):
        super().__init__(
            config_path=config_path,
            config_name=config_name
        )
        self.engine = self.getEngine()

    def get_table_where(self, table, criterion:list):
        with Session(bind=self.engine) as session:
            test = session.query(table).where(*criterion)

        return test


class ContentMasters:

    @staticmethod
    def get(
            masters_name: str,
            manager: AlchemyManager
    ) -> dict:

        header = services_name_dict.get(masters_name)
        page = f'services/{masters_name}'

        with Session(bind=manager.engine) as session:

            masters_list = session.query(Masters).filter(Masters.type == masters_name)

            masters_list = ContentMasters._type_filtering(masters_list)

            title = session.query(Content).filter(Content.type == ContentType.text, Content.page == page)

            static_content = {
                "header": header,
                "title": str(title),
                "content_list": masters_list
            }

        return static_content


    @staticmethod
    def _type_filtering(masters_list):

        tmp_list = list()

        for masters in masters_list:

            tmp_dict = dict()

            for content in masters.content_list:

                if content.type == ContentType.img:
                    tmp_dict.update(img=content.extra)

                elif content.extra == ContentType.text:
                    tmp_dict.update(text=content.extra)

            tmp_list.append(tmp_dict)




