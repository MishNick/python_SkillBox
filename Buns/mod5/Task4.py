"""
Иногда возникает необходимость перенаправить вывод в нужное нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта (например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""

from types import TracebackType
from typing import Type, Literal, IO
import sys
from types import TracebackType
from typing import Type, Literal, IO

class Redirect:
    def __init__(self, stdout: IO = None, stderr: IO = None) -> None:
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        sys.stdout = self._original_stdout
        sys.stderr = self._original_stderr

# Весь вывод stdout и stderr будет перенаправлен в файлы "output.txt" и "error.txt"
with Redirect(stdout=open('output.txt', 'w'), stderr=open('error.txt', 'w')):
    print('Этот текст будет записан в файл "output.txt"')
    print('А этот текст будет записан в файл "error.txt"', file=sys.stderr)