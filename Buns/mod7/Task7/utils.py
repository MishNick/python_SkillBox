import math
import logging
import logging.config
from logging_config import dict_config
from logging.handlers import TimedRotatingFileHandler
import logging_tree

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

class ASCIIFilter(logging.Filter):
    def filter(self, record):
        return all(ord(c) < 128 for c in record.msg)
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

def configure_logging():
    log_format = logging.Formatter('%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    utils_logger = logging.getLogger("utils")
    utils_logger.setLevel(logging.INFO)

    utils_file_handler = TimedRotatingFileHandler("utils.log", when="H", interval=1, backupCount=6)
    utils_file_handler.setLevel(logging.INFO)
    utils_file_handler.setFormatter(log_format)

    utils_logger.addHandler(utils_file_handler)

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
logging_tree_str = logging_tree.format.build_description()
with open("logging_tree.txt", "w") as f:
    f.write(logging_tree_str)

__all__ = ["ASCIIFilter"]