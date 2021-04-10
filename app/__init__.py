import logging

from app.config import Config


def setup_logging():
    if config.DEBUG:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(level=level)


config = Config()
setup_logging()
