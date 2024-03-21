"""
Консольная утилита lsof (List Open Files) выводит информацию о том, какие файлы используют какие-либо процессы.
Эта команда может рассказать много интересного, так как в Unix-подобных системах всё является файлом.

Но нам пока нужна лишь одна из её возможностей.
Запуск lsof -i :port выдаст список процессов, занимающих введённый порт.
Например, lsof -i :5000.

Как мы с вами выяснили, наш сервер отказывается запускаться, если кто-то занял его порт. Напишите функцию,
которая на вход принимает порт и запускает по нему сервер. Если порт будет занят,
она должна найти процесс по этому порту, завершить его и попытаться запустить сервер ещё раз.
"""
from typing import List

from flask import Flask

app = Flask(__name__)


def get_pids(port: int) -> List[int]:
    if not isinstance(port, int):
        raise ValueError

    pids: List[int] = []
    ...

    return pids



def free_port(port: int) -> None:
    pids: List[int] = get_pids(port)
    for pid in pids:
        ...


def run(port: int) -> None:
    free_port(port)
    app.run(port=port)


if __name__ == '__main__':
    run(5000)
