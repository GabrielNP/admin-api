from dataclasses import dataclass
from typing import Any
from flask.helpers import make_response

from http import HTTPStatus

@dataclass
class StdResponse(object):
    data: Any = None
    message: str = None
    error: str = None

    def serialize(self):
        return self.__dict__

def list(data_list):
    return make_response(StdResponse(data=data_list).serialize()), HTTPStatus.OK

def success(message: str, data: Any = None):
    return make_response(StdResponse(message=message, data=data).serialize()), HTTPStatus.OK

def error(error: str, message: str):
    return make_response(StdResponse(error=error, message=message).serialize()), HTTPStatus.BAD_REQUEST
