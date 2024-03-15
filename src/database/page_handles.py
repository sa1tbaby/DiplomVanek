from src.database.base import AlchemyBase
from src.database.models.declarative_models import Media
from sqlalchemy import select
from flask import request
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

class UiContent(AlchemyBase):

    def get(self, keys):

        page = request.base_url[len(request.host_url):]
        stmt = select(Media).where(Media.page == page)


class AdminContent(AlchemyBase):

    def get(self):
