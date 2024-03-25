import math
import logging

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

def configure_logging():
    log_format = logging.Formatter('%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logging.basicConfig(handlers=[console_handler], level=logging.INFO)

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