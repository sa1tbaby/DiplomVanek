from sqlalchemy.orm import Session

from models.declarativeModels import (
    Content,
    Services,
    ContentType)

from alchemyManager import AlchemyManager


class ContentServices:

    @staticmethod
    def get(
            manager: AlchemyManager,
            services_name: str
    ):
        static_content = {
            "header": services_name
        }

        with Session(bind=manager.engine) as session:

            static_content.update(

                title=session.query(Content).filter(
                    criterion=[Content.type == ContentType.text,
                               Content.page == f"services/{services_name}"]
                ),

                content_list=session.query(Services).filter(
                    criterion=Services.type == services_name
                )
            )

        return static_content