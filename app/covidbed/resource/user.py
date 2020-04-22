import datetime

from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import  Resource
from flask_restful_swagger import swagger

from covidbed.serializer.user import (SignupRequestSerializer, SignupResponseSerializer,
                                      SigninRequestSerializer, SigninResponseSerializer)

from covidbed.repository import user as user_repository

from sqlalchemy.orm.exc import NoResultFound


class LoginApi(Resource):

    @swagger.operation(
        notes='Signin',
        responseClass=SigninResponseSerializer.__name__,
        nickname='signup',
        parameters=[
            {
                "name": "body",
                "description": "signin's parameter",
                "required": True,
                "allowMultiple": False,
                "dataType": SigninRequestSerializer.__name__,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "A session token is provider."
            },
            {
                "code": 404,
                "message": "Email not found"
            },
            {
                "code": 401,
                "message": "Password invalid"
            }


        ])
    def post(self):
        body = request.get_json()
        user = user_repository.get_user_by_email(body.get('email'))
        if not user:
            return {"error": "Email not found"}, 404

        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Password invalid'}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200


class UserListAPI(Resource):

    @jwt_required
    def get(self):
        return jsonify(data=user_repository.find_users())


class UserAPI(Resource):
    method_decorators = [jwt_required]

    def get(self, id):
        user = user_repository.get_user_by_id(id)
        return user.json, 200

    def put(self, id):
        body = request.get_json()
        user = user_repository.get_user_by_id(id)

        for k, v in body.items():
            if v == getattr(user, k):
                continue
            setattr(user, k, v)
        user.save()
        return user.json, 200

    def delete(self, id):
        try:
            user = user_repository.get_user_by_id(id)
            user.remove()
            return {}, 204

        except NoResultFound:
           response = jsonify(data={"errors": [{"user": "Not found"}]})
           response.status_code = 404
           return response



