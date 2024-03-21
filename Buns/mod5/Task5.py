"""
Напишите код, который выводит сам себя.
Обратите внимание, что скрипт может быть расположен в любом месте.
"""

import inspect

current_file_path = inspect.getsourcefile(inspect.currentframe())

with open(current_file_path, 'r') as file:
    content = file.read()
    print(content)


# Secret magic code
