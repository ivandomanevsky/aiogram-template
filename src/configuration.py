from dataclasses import dataclass

from environs import Env
from sqlalchemy import URL


@dataclass
class BotConfig:
    env = Env()
    env.read_env()
    token: str = env('BOT_TOKEN')
    admin_id: str | None = env('ADMIN_ID', None)


@dataclass
class DatabaseConfig:
    env = Env()
    env.read_env()

    name: str | None = env('POSTGRES_DATABASE')
    user: str | None = env('POSTGRES_USER')
    passwd: str | None = env('POSTGRES_PASSWORD', None)
    port: int = int(env('POSTGRES_PORT', 5432))
    host: str = env('POSTGRES_HOST')

    driver: str = 'asyncpg'
    database_system: str = 'postgresql'

    def build_connection_str(self) -> str:
        return URL.create(
            drivername=f'{self.database_system}+{self.driver}',
            username=self.user,
            database=self.name,
            password=self.passwd,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)


@dataclass
class PaymentConfig:
    env = Env()
    env.read_env()
    token: str | None = env('PROVIDER_TOKEN', None)


@dataclass
class Configuration:
    bot = BotConfig()
    db = DatabaseConfig()
    payment = PaymentConfig()


conf = Configuration()
