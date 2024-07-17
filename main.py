"""Главный файл."""
import os

import redis
from art import tprint
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()

host_redis = os.getenv('HOST_REDIS')
port_redis = os.getenv('PORT_REDIS')
db_redis = os.getenv('DB_REDIS')


def set_key() -> None:
    """Устанавливает ключ/значение в redis."""
    console.print('[bold blue] Введите ключ')
    key = input()
    console.print('[bold blue] Введите значение')
    value = input()
    if redis_client.set(name=key, value=value):
        console.print('[bold green] Успешно!')
    else:
        console.print('[bold red] ОШИБКА')


def get_key() -> None:
    """Функция получения значения по ключу."""
    console.print('[bold blue] Чтобы получить все ключи нажмите Enter')
    console.print('[bold blue] Чтобы получить данные введите ключ')
    key = input()
    if key == '':
        keys = redis_client.keys('*')
        console.print('[bold green] Успешно!')
        console.print(keys)
    else:
        data = redis_client.get(name=key)
        if any(data):
            console.print('[bold green] Успешно!')
            console.print(f'[bold yellow] Данные - {data}')


def delete_key() -> None:
    """Функция для удаления ключа."""
    console.print('[bold blue] Введите ключ')
    key = input()
    result = redis_client.delete(key)
    if result:
        console.print('[bold green] Успешно!')
    else:
        console.print('[bold red] ОШИБКА')


def set_timer() -> None:
    """Функция для создания ключа с жизненым цыклом."""
    console.print('[bold blue] Введите ключ')
    key = input()
    console.print('[bold blue] Введите время для ключа')
    time_data = int(input())
    if redis_client.expire(key, time_data):
        console.print('[bold green] Успешно!')
    else:
        console.print('[bold red] ОШИБКА')


def control() -> None:
    """Управление командами."""
    while True:
        console.print('[bold blue] Выберете действие')
        console.print('[bold blue] 1 - Установить ключ/значение')
        console.print('[bold blue] 2 - Получить данные')
        console.print('[bold blue] 3 - Удалить ключ/значение')
        console.print('[bold blue] 4 - Установить таймер для ключа')
        try:
            result = int(input())
            if result == 1:
                set_key()
            elif result == 2:
                get_key()
            elif result == 3:
                delete_key()
            elif result == 4:
                set_timer()
        except ValueError:
            print('[bold red] ОШИБКА действия')


if __name__ == '__main__':
    console = Console()
    redis_client = redis.Redis(host=host_redis, port=port_redis, db=db_redis)
    tprint('REDIS V- 1')
    console.print('[bold red]-------------------------')
    control()
