from flask_restful import Resource

class Coupon(Resource):
    def get(self, Id):
        return "GET", 200

    def post(self):
        return "POST", 201

    def put(self, Id):
        pass

    def delete(self, Id):
        pass