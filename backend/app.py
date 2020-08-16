from flask import Flask
from flask_cors import CORS
from database import *

app = Flask(__name__)
CORS(app)

@app.route("/get/user=<userId>", methods=['GET'])
def getUserData(userId):
    d = DataDB(userId)
    return d.ReadFormateData()

@app.route("/add/cn=<CardName>&ed=<ExpireDate>&fu=<FromUser>&cc=<CardContent>&ui=<UserId>", methods=['GET'])
def addData(CardName, ExpireDate, FromUser, CardContent, UserId):
    d = DataDB(UserId)
    return str(d.write(CardName, ExpireDate, FromUser, CardContent))

if __name__ == "__main__":
    app.run(debug=True)