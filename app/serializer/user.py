from flask_restful_swagger import  swagger
from flask_restful import fields


@swagger.model
class SignupRequestSerializer:
    resource_fields = {
        'email': fields.String,
        'username': fields.String,
        'password': fields.String,
    }
    required = ["email", 'username', "password"]


@swagger.model
class SignupResponseSerializer:
    resource_fields = {
        'id': fields.String
    }


@swagger.model
class SigninRequestSerializer:
    resource_fields = {
        'email': fields.String,
        'password': fields.String,
    }
    required = ["email", 'username']


@swagger.model
class SigninResponseSerializer:
    resource_fields = {
        'token': fields.String
    }
