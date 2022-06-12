import logging as l
from logging import StreamHandler, Formatter
from flask import json
from fluent import sender

LOG_FORMAT = {"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}

def createLogger(extra:dict={}):
    logger = l.getLogger('main')
    logger.setLevel(l.INFO)

    stream_handler = StreamHandler()
    stream_handler.setFormatter(Formatter(json.dumps(LOG_FORMAT)))

    logger.addHandler(stream_handler)
    # logger = l.LoggerAdapter(logger, extra)
    
    return logger

logger = createLogger()
flogger = sender.FluentSender('web', host='fluentd', port=24224)