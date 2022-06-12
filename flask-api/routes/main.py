from flask import blueprints
from flask.json import jsonify
from init_logger import logger, flogger
from test_helpers import randomFunction

blueprint_main = blueprints.Blueprint('main', __name__)

@blueprint_main.route('/', methods=['GET'])
def main():
    logger.info("Logging from main()!")
    # flogger.emit('follow', {"Lorem": "ipsum"})
    print("Printing from main()!")

    import socket

    randomFunction("random_val")

    log_message = {
        "method": "GET",
        "route": "/",
        "blueprint": "main",
        "response": "Hello, World!"
    }
    if not flogger.emit('follow', log_message):
        print(flogger.last_error)
        logger.error(flogger.last_error)
        flogger.clear_last_error() # clear stored error after handled errors
    return jsonify(log_message)