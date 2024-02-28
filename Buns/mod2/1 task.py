"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""


def get_summary_rss(ps_output_file_path: str) -> str:
    with open(ps_output_file_path, 'r') as f:
        total_rss = 0
        for line in f:
            columns = line.split()
            rss = int(columns[5])
            total_rss += rss

    units = ['B', 'KB', 'MB', 'GB']
    unit_index = 0
    while total_rss >= 1024 and unit_index < len(units) - 1:
        total_rss /= 1024
        unit_index += 1

    return f'{total_rss:.2f} {units[unit_index]}'


if __name__ == '__main__':
    path: str = 'PATH_TO_OUTPUT_FILE'
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)