from database.declarativeModels import BaseBd
from database.alchemyManager import AlchemyManager
import os.path

project_dir = os.path.pardir
database_dir = os.path.join(project_dir, 'database')
config_dir = os.path.join(project_dir, 'configs')

Manager = AlchemyManager(
    config_path=database_dir
)

BaseBd.metadata.create_all()