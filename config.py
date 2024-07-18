"""Файл настройки redis."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    """Класс настройки подключения к redis.

    Args:
        BaseSettings (class): базовые настройки
    """

    model_config = SettingsConfigDict(env_file='.env')

    host_redis: str
    port_redis: int
    db_redis: int


redis_settings = RedisSettings()
