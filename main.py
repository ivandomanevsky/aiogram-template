import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.configuration import conf
from src.bot.handlers import start, user

logger = logging.getLogger(__name__)


async def main():
    engine = create_async_engine(url=conf.db.build_connection_str(), echo=True)
    session_maker = async_sessionmaker(engine, expire_on_commit=False)
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    redis: Redis = Redis(host='localhost')

    storage: RedisStorage = RedisStorage(redis=redis)

    bot: Bot = Bot(token=conf.bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    dp.include_router(start.router)
    dp.include_router(user.router)

    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(send_notification, trigger='cron', hour=12, minute=0,
                      kwargs={'session_maker': session_maker})
    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, session_maker=session_maker)

if __name__ == '__main__':
    asyncio.run(main())
