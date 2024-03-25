from logging import getLogger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



class AlchemyFactory:

    def __init__(self, settings):

        self.settings = settings

        self.engine = create_engine(
            url=settings.get_url_psycopg,
            echo=settings.DB_ECHO,
            logging_name=getLogger(AlchemyFactory.__name__)
        )

        self.session_factory = sessionmaker(
            bind=self.engine
        )

        self.subcls_dict = {subcls.__name__: subcls for subcls in AlchemyFactory.__subclasses__()}

    def get(self, cls_name):

        cls_ = self.subcls_dict.get(cls_name)

        return cls_(self.settings)
