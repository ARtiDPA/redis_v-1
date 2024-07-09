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


def control() -> None:
    """Управление командами."""
    while True:
        console.print('[bold blue] Выберете действие')
        console.print('[bold blue] 1 - Установить ключ/значение')
        console.print('[bold blue] 2 - Удалить ключ значение')
        try:
            result = int(input())
            if result == 1:
                set_key()
            elif result == 2:
                pass
        except ValueError:
            pass


if __name__ == '__main__':
    console = Console()
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    tprint('REDIS V-1')
    console.print('[bold red]-------------------------')
    control()
