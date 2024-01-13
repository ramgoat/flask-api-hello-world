import json
import os
from flask import blueprints
from flask.json import jsonify

blueprint_main = blueprints.Blueprint('main', __name__)

@blueprint_main.route('/', methods=['GET'])
def main():
    return jsonify("Hello, World!")

@blueprint_main.get('/env')
def getEnvVars():
    try:
        FLASK_APP = os.getenv('FLASK_APP')
    except:
        FLASK_APP = None
    try:
        FLASK_ENV = os.getenv('FLASK_ENV')
    except:
        FLASK_ENV = None
    # try:
    #     FLASK_OBJ = os.getenv('FLASK_OBJ')
    # except:
    #     FLASK_OBJ = None
    try:
        KEY_ENV = os.getenv('KEY_ENV')
    except:
        KEY_ENV = None
        
    response = {
        'FLASK_APP': FLASK_APP,
        'FLASK_ENV': FLASK_ENV,
        # 'FLASK_OBJ': json.loads(FLASK_OBJ),
        'KEY_ENV': KEY_ENV}
    return jsonify(response)