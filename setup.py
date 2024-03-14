import json
import os.path

from configuration.init_db import InitDb
from src.config import Settings

InitDb(settings=Settings()).init()
