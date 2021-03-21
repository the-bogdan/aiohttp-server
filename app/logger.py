import os
import logging
from config import config
from logging import handlers


log_level = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "FATAL": logging.FATAL,
}


logs_path = config['logs']['logs_path']
if not os.path.exists(os.path.dirname(logs_path)):
    os.makedirs(os.path.dirname(logs_path))
if not os.path.exists(logs_path):
    os.mknod(logs_path)

logger = logging.getLogger('SteamExchangeBot')
format_str = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s: %(message)s')

logger.setLevel(log_level[config['logs']['logs_level']])

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(format_str)
logger.addHandler(stream_handler)


rotating_file_handler = handlers.RotatingFileHandler(
    filename=logs_path,
    mode='a',
    maxBytes=1024*1024*5,
    backupCount=5
)
rotating_file_handler.setFormatter(format_str)
logger.addHandler(rotating_file_handler)
