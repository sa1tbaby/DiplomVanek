from models import declarativeModels
from app.handlers.alchemyManager import AlchemyManager
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import insert
from models.declarativeModels import Users, Appointments, Services, Masters, Content
import os.path

"""project_dir = os.path.abspath(os.path.pardir)
config_dir = os.path.join(project_dir, 'configs')

Manager = AlchemyManager(
    config_path=config_dir
)"""

def create_table():
    declarativeModels.BaseBd.metadata.drop_all(Manager.engine)
    declarativeModels.BaseBd.metadata.create_all(Manager.engine)


def get_table_where(table, criterion):

    with Session(bind=Manager.engine) as session:
        test = session.query(table).where(criterion)

    return test



def insert_data():





    with Session(bind=Manager.engine) as session:

        session.execute(insert(Masters).values(content.get("masters")))
        session.execute(insert(Users).values(content.get("users")))
        session.execute(insert(Services).values(content.get("services")))
        session.execute(insert(Appointments).values(content.get("appointments")))
        session.execute(insert(Content).values(content.get("content")))

        session.commit()

create_table()
insert_data()