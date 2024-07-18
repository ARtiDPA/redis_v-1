"""Работа с redis."""
import redis

from config import redis_settings


class RedisRequest:
    """Класс для работы с redis."""

    def __init__(self) -> None:
        """Init функция."""
        self.redis_client = redis.Redis(
            host=redis_settings.host_redis,
            port=redis_settings.port_redis,
            db=redis_settings.db_redis,
            )

    def set_key(self, name: str, key: str) -> bool:
        """Функция для установки ключа.

        Args:
            name (str): Название ключа
            key (str): Значение ключа

        Returns:
            bool: резульат запроса в redis.
        """
        return self.redis_client.set(name, key)

    def get_key(self, name: str) -> str:
        """Функция получение значение ключа.

        Args:
            name (str): Название ключа

        Returns:
            str: содержимое ключа
        """
        return self.redis_client.get(name)

    def delete_key(self, name: str) -> bool:
        """Функция удаления ключа.

        Args:
            name (str): Название ключа

        Returns:
            bool: резульат запроса в redis
        """
        return self.redis_client.delete(name)
