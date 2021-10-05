"""
File-level doc string test
"""
import logging, sys
from logging.handlers import TimedRotatingFileHandler
from logging import FileHandler

logging_config = {
    'log-file-main': 'app.log',
    'log-file-directory': '/'
}

FORMATTER = logging.Formatter("[%(asctime)s] %(module)15s %(funcName)-25s %(levelname)-10s: %(message)s","%Y-%m-%d %H:%M:%S")

def getFileHandler(log_level=logging.NOTSET):
    logger_path = 'app.log'
    file_handler = FileHandler(logger_path)

    file_handler.setLevel(log_level) # Set log level
    file_handler.setFormatter(FORMATTER) # Set format

    return file_handler

def getFileLogger(logger_name,log_level=None):
    '''Creates logger that outputs only to main.log.'''

    if log_level == None : level = logging.NOTSET
    else: 
        log_level = str(log_level)
        level = log_level.upper()

    if level == 'DEBUG': level = logging.DEBUG
    if level == 'INFO': level = logging.INFO
    if level == 'WARNING': level = logging.WARNING
    if level == 'ERROR': level = logging.ERROR
    if level == 'CRITICAL': level = logging.CRITICAL

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    logger.addHandler(getFileHandler(log_level=level))

    logger.propagate = True # with this pattern, it's rarely necessary to propagate the error up to parent
    return logger
    
#logger = getFileLogger("app")