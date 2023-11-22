from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models.base import Base, BaseModel


class User(BaseModel, Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
