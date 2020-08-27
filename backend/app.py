from flask import Flask, request
from flask_restful import Resource, Api

from common.config import LC_bConfig
from common.jwt import jwt
from resource.user import User, Users
from resource.coupon import Coupon

app = Flask(__name__)
api = Api(app)

users = []
# {
#     "Name": string,
#     "Sexual": "Male",
#     "Phone": 0912345678,
#     "email": "test@example.org"
# }

class Auth(Resource):
    def get(self):
        pass

class General(Resource):
    def get(self):
        return "API", 200

api.add_resource(General, '/api')     
api.add_resource(User, '/api/user/<string:userId>')
api.add_resource(Users, '/api/user')
api.add_resource(Coupon, '/api/coupon/<string:Id>')

if( __name__ == '__main__' ):
    from common.ma import ma
    ma.init_app(app)
    app.run(debug=True)
