"""Главный файл."""
from art import tprint
from rich.console import Console

import db_redis


def control(redis_client) -> None:
    """Интерфейс по.

    Args:
        redis_client (class): класс для работы с redis.
    """
    tprint('REDIS V- 1')
    console.print('[bold red]-------------------------')
    while True:
        console.print('[bold blue] Выберете действие')
        console.print('[bold blue] 1 - Установить ключ/значение')
        result = int(input())
        if result == 1:
            console.print('[bold blue] 1 - Введите название ключа')
            name = input()
            console.print('[bold blue] 1 - Введите ключ')
            key = input()
            if redis_client.set_key(name, key):
                console.print('[bold green] Успешно!')
        elif result == 0:
            break


if __name__ == '__main__':
    console = Console()
    control(db_redis.RedisRequest())
