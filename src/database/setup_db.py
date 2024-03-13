from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID



from uuid import uuid4



class BaseBd(DeclarativeBase):
    pass