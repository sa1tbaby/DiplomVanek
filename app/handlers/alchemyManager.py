import os.path

from json import load

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import NullPool
from sqlalchemy.engine.base import Engine

from models.schemas import ConfigDB


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







