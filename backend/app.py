from flask import Flask
from flask_cors import CORS
from file_tmp import DataIO

app = Flask(__name__)
CORS(app)

@app.route("/get/user=<userId>", methods=['GET'])
def getUserData(userId):
    d = DataIO(userId)
    return d.read()

@app.route("/add/cn=<CardName>&ed=<ExpireDate>&fu=<FromUser>&cc=<CardContent>&ui=<UserId>", methods=['GET'])
def addData(CardName, ExpireDate, FromUser, CardContent, UserId):
    d = DataIO(UserId)
    return d.save(CardName, ExpireDate, FromUser, CardContent)

if __name__ == "__main__":
    app.run(debug=True)