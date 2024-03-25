import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('stderr.txt')

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%H:%M:%S')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.info('Пример записи лога уровня INFO')
logger.warning('Пример записи лога уровня WARNING')
logger.error('Пример записи лога уровня ERROR')
