from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

users = []
# {
#     "Name": string,
#     "Sexual": "Male",
#     "Phone": 0912345678,
#     "email": "test@example.org"
# }

class User(Resource):
    def get(self, userId):
        return "GET", 200

    def post(self):
        return "POST", 201

    def put(self, userId):
        pass

    def delete(self):
        pass

api.add_resource(User, '/api/user/<string:userId>')

if __name__ == '__main__':
    app.run(debug=True)
