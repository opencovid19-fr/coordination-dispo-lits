from functools import wraps
from flask_restful import reqparse

import constant


def parse_params(*arguments):
    def wrapper(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            parser = reqparse.RequestParser()
            for argument in arguments:
                parser.add_argument(**argument)
            params = parser.parse_args()

            return func(*args, params=params, **kwargs)
        return decorated_function
    return wrapper


def get_error_messages(code, *args):
    if args:
        return {"code": code, "message": constant.ERROR_MESSAGES[code].format(*args)}
    return {"code": code, "message": constant.ERROR_MESSAGES[code]}
