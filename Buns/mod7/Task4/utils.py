import math
import logging
import logging.config
from logging_config import dict_config

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
def calculate(a: float, b: float, operation: str) -> float:
    match operation:
        case "+":
            return _addition(a, b)
        case "-":
            return _subtraction(a, b)
        case "*":
            return _multiplication(a, b)
        case "/":
            return _division(a, b)
        case "^":
            return _pow(a, b)

"""def configure_logging():
    log_format = logging.Formatter('%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    file_handler_debug = logging.FileHandler("calc_debug.log")
    file_handler_debug.setLevel(logging.DEBUG)
    file_handler_debug.setFormatter(log_format)
    file_handler_error = logging.FileHandler("calc_error.log")
    file_handler_error.setLevel(logging.ERROR)
    file_handler_error.setFormatter(log_format)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler_debug)
    logger.addHandler(file_handler_error)"""
logging.config.dictConfig(dict_config)
logger = logging.getLogger(__name__)

def _addition(a: float, b: float) -> float:
    result: float = a + b
    return result


def _subtraction(a: float, b: float) -> float:
    result: float = a - b
    return result


def _multiplication(a: float, b: float) -> float:
    result: float = a * b
    return result


def _division(a: float, b: float) -> float:
    result: float = a / b
    return result


def _pow(a: float, b: float) -> float:
    result: float = math.pow(a, b)
    return result

configure_logging()