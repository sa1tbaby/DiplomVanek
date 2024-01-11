from database.declarativeModels import BaseBd
from database.alchemyManager import AlchemyManager
import os.path

project_dir = os.path.abspath(os.path.pardir)
database_dir = os.path.join(project_dir, 'database')
config_dir = os.path.join(project_dir, 'configs')

Manager = AlchemyManager(
    config_path=config_dir
)

BaseBd.metadata.drop_all(Manager.engine)
BaseBd.metadata.create_all(Manager.engine)