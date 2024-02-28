"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(ls_output: str) -> float:
    lines = ls_output.split('\n')
    sizes = []
    for line in lines:
        columns = line.split()
        if len(columns) >= 5:
            size = int(columns[4])
            sizes.append(size)

    mean_size = sum(sizes) / len(sizes)
    return mean_size


if __name__ == '__main__':
    data: str = sys.stdin.read()
    mean_size: float = get_mean_size(data)
    print(mean_size)