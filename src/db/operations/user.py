from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from src.db.models.user import User


async def create_user(user_id, session_maker: sessionmaker) -> None:
    async with session_maker() as session:
        async with session.begin():
            user = User(
                id=user_id,
            )
            session.add(user)


async def select_user(user_id, session_maker: sessionmaker) -> None:
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.id == user_id))

            user = result.scalar()

            return user
