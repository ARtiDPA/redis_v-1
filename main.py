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
        console.print('[bold blue] 2 - Получить ключ')
        console.print('[bold blue] 3 - Удаление ключа')
        console.print('[bold blue] 0 - Выйти')
        result = int(input())
        if result == 1:
            console.print('[bold blue] Введите название ключа')
            name = input()
            console.print('[bold blue] Введите ключ')
            key = input()
            if redis_client.set_key(name, key):
                console.print('[bold green] Успешно!')

        elif result == 2:
            console.print('[bold blue] Введите название ключа')
            name = input()
            data = redis_client.get_key(name)
            if data:
                console.print('[bold green] Успешно!')
                console.print(f'[bold green] Данные: {data}')
            else:
                console.print('[bold red] Ошибка')
                console.print(f'[bold purple]Нет ключа с названием: {name} ')

        elif result == 3:
            console.print('[bold blue] Введите название ключа')
            name = input()
            if redis_client.delete_key(name):
                console.print('[bold green] Успешно!')
            else:
                console.print('[bold red] Ошибка')
                console.print(f'[bold purple]Нет ключа с названием: {name} ')
        elif result == 0:
            break


if __name__ == '__main__':
    console = Console()
    control(db_redis.RedisRequest())
