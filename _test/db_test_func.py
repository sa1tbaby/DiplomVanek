from database import declarativeModels
from database.alchemyManager import AlchemyManager
from sqlalchemy.orm import sessionmaker, Session
import os.path

project_dir = os.path.abspath(os.path.pardir)
database_dir = os.path.join(project_dir, 'database')
config_dir = os.path.join(project_dir, 'configs')

Manager = AlchemyManager(
    config_path=config_dir
)

sss = sessionmaker(bind=Manager.engine)

def create_table():
    declarativeModels.BaseBd.metadata.drop_all(Manager.engine)
    declarativeModels.BaseBd.metadata.create_all(Manager.engine)


def get_table_where(table, criterion):

    with Session(bind=Manager.engine) as session:
        test = session.query(table).where(criterion)

    return test

