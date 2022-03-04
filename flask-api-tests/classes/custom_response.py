from flask import Response
from flask import jsonify
from classes.custom_flask import CustomFlask
import sys


class CustomResponse(Response):
    default_mimetype = 'application/json'

    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(CustomResponse, cls).force_type(rv, environ)
