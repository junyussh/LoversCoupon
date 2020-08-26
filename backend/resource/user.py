from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from .models.schema.user_schema import UserSchema
from .models.user import UserModel

user_schema = UserSchema(many=False)

def get_param():
    data = request.get_json(force=False)
    if data is None:
        data = request.form
    return data

class User(Resource):
    def get(self, userId):
        user = UserModel.get_user(userId)
        if not user:
            return {
                'successe': False,
            }, 403
        return {
            'successe': True,
            'user': user_schema.dump(user)
        }, 200

    def post(self, userId):
        result = user_schema.load(request.json)

        # if len(result.errors) > 0:
        #     return result.errors, 433

        print(result)
        user = UserModel(name=result["name"], email=result['email'], password=result['password'], sex=result["sex"], birth=result["birth"], phone=result["phone"])
        user.add_user()
        return {
            'successe': True,
            'user': user_schema.dump(user)
        }, 201


    def put(self, userId):
        pass

    def delete(self, userId):
        pass