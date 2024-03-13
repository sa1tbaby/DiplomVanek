from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from logging import getLogger


class AlchemyBase:

    def __init__(self, settings):

        self.engine = create_engine(
            url=settings.get_url_psycopg,
            echo=settings.DB_ECHO,
            echo_pool=settings.DB_ECHO_POOL,
            logging_name=getLogger(self.__name__)
        )

        self.session_factory = sessionmaker(
            bind=self.engine
        )