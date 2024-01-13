from sqlalchemy.orm import Session

from models.schemas import services_name_dict
from models.declarativeModels import (
    Content,
    Masters,
    ContentType)

from alchemyManager import AlchemyManager

class ContentMasters:
    @staticmethod
    def get(
            manager: AlchemyManager,
            masters_name: str
    ) -> dict:

        header = services_name_dict.get(masters_name)
        page = f'services/{masters_name}'

        with Session(bind=manager.engine) as session:

            masters_list = session.query(Masters).filter(Masters.type == masters_name)

            masters_list = ContentMasters._type_filtering(masters_list)

            title = session.query(Content).filter(Content.type == ContentType.text, Content.page == page)

            static_content = {
                "header": header,
                "title": str(title),
                "content_list": masters_list
            }

        return static_content
    @staticmethod
    def _type_filtering(masters_list):

        tmp_list = list()

        for masters in masters_list:

            tmp_dict = dict()

            for content in masters.content_list:

                if content.type == ContentType.img:
                    tmp_dict.update(img=content.extra)

                elif content.extra == ContentType.text:
                    tmp_dict.update(text=content.extra)

            tmp_list.append(tmp_dict)
