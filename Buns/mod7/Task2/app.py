from module_7.task_1 import utils
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
def show_list_of_commands() -> None:
    logger.info("Доступные команды:\n"
                "\"+\" - сложение\n"
                "\"-\" - вычитание\n"
                "\"*\" - умножение\n"
                "\"/\" - деление\n"
                "\"^\" - возведение в степень\n")

def configure_logging():
    log_format = logging.Formatter('%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logging.basicConfig(handlers=[console_handler], level=logging.INFO)

def get_command_from_user() -> str:
    command: str = input("Введите выражение с пробелами: ")
    return command


def process_command(command: str) -> tuple[float, float, str] | None:
    command_split: [str] = command.split()
    if len(command_split) != 3:
        return None
    number_1 = float(command_split[0])
    number_2 = float(command_split[2])
    operation = command_split[1]
    return number_1, number_2, operation

def get_result(command: tuple[float, float, str] | None) -> str:
    if command is None:
        return "Вы ввели не корректную строку, повторите попытку."
    number_1, number_2, operation = command
    result: float = utils.calculate(number_1, number_2, operation)
    return str(result)

def give_result_to_user(result: str) -> None:
    print(result)

if __name__ == '__main__':
    show_list_of_commands()
    while True:
        command: str = get_command_from_user()
        processed_command = process_command(command)
        result: str = get_result(processed_command)
        give_result_to_user(result)

configure_logging()