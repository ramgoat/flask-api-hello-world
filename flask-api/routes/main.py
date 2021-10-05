from flask import blueprints
from flask.json import jsonify
from init_redis_rq import rq
from init_logger import getFileLogger

blueprint_main = blueprints.Blueprint('main', __name__)
logger = getFileLogger(__name__, log_level='DEBUG')

@rq.job
def reverse(val):
    val_reversed = val[::-1]
    logger.info(f"{val} --> {val_reversed}")
    return val_reversed

@blueprint_main.route('/<val>', methods=['GET'])
def main(val):
    logger.info(f'String received: {val}')
    job = reverse.queue(val)
    return jsonify("Hello, World!")