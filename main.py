"""Главный файл."""
import redis
from art import tprint
from rich.console import Console


def set_key():
    """Устанавливает ключ/значение в redis."""
    console.print('[bold blue] Введите ключ')
    key = input()
    console.print('[bold blue] Введите значение')
    value = input()
    if redis_client.set(name=key, value=value):
        console.print('[bold green] Успешно!')
    else:
        console.print('[bold red] ОШИБКА')


def get_key():
    """Функция получения значения по ключу."""
    console.print('[bold blue] Введите ключ')
    key = input()
    data = redis_client.get(name=key)
    if any(data):
        console.print('[bold green] Успешно!')
        console.print(f'[bold yellow] Данные -[/bold yellow] [bold purple]{data}')


def delete_key():
    """Функция для удаления ключа."""
    console.print('[bold blue] Введите ключ')
    key = input()
    result = redis_client.delete(key)
    if result:
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
        try:
            result = int(input())
            if result == 1:
                set_key()
            elif result == 2:
                get_key()
            elif result == 3:
                delete_key()
        except ValueError:
            print('[bold red] ОШИБКА действия')


if __name__ == '__main__':
    console = Console()
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    tprint('REDIS V-1')
    console.print('[bold red]-------------------------')
    control()
