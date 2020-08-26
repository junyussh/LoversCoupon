from flask_restful import Resource

class User(Resource):
    def get(self, userId):
        return "GET", 200

    def post(self):
        return "POST", 201

    def put(self, userId):
        pass

    def delete(self, userId):
        pass