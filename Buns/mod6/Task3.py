import logging
import json

class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        json_msg = json.dumps(msg)
        return json_msg, kwargs

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('skillbox_json_messages.log')

formatter = logging.Formatter('{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

json_adapter = JsonAdapter(logger, {})

json_adapter.info('Сообщение')
