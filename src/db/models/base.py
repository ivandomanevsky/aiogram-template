from datetime import date, datetime

from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base


Base: DeclarativeMeta = declarative_base()


def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.timestamp()
    return obj


class BaseModel:
    def __str__(self) -> str:
        return f"<{__class__.__name__} ID:{self.id}>"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {c.name: json_serial(getattr(self, c.name)) for c in self.__table__.columns}
