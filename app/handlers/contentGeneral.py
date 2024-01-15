from app.handlers.alchemyManager import AlchemyManager
from sqlalchemy.orm import Session

from models.declarativeModels import Content, ContentType
from app.handlers.alchemyManager import AlchemyManager


class ContentGeneral:

    @staticmethod
    def get(
            manager: AlchemyManager
    ):

        static_content = dict()

        with Session(bind=manager.engine) as session:

            static_content.update(
                gif=session.query(Content).filter(
                    *[Content.page == 'main',
                     Content.type == ContentType.img]
                ),

                info=session.query(Content).filter(
                    *[Content.page == 'main/info',
                      Content.type == ContentType.text]
                ),

                contacts=session.query(Content).filter(
                    *[Content.page == "main/contacts",
                      Content.type == ContentType.text]
                )
            )

        return static_content