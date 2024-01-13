from app.alchemyManager import AlchemyManager
from models.schemas import config_dir
from flask import Flask

app = Flask(__name__)

manager = AlchemyManager(
    config_path=config_dir
)
