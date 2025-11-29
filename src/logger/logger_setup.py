import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

logger_handler = logging.FileHandler('src/logger/shell.log', mode='a')
logger_formater = logging.Formatter(
    '[%(asctime)s] %(levelname)s: %(message)s'
)

logger_handler.setFormatter(logger_formater)

logger.addHandler(logger_handler)