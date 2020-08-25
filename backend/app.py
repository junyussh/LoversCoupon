from flask import Flask, request, abort
from flask_cors import CORS
from database import *
from config import LC_bConfig

app = Flask(__name__)
CORS(app)

config = LC_bConfig

@app.route("/get/user=<userId>", methods=['GET'])
def getUserData(userId):
    d = DataDB(userId)
    return d.ReadFormateData()

@app.route("/add/cn=<CardName>&ed=<ExpireDate>&fu=<FromUser>&cc=<CardContent>&ui=<userId>", methods=['GET'])
def addData(CardName, ExpireDate, FromUser, CardContent, userId):
    d = DataDB(userId)
    return str(d.write(CardName, ExpireDate, FromUser, CardContent))

@app.route("/delete/id=<id>&user=<userId>", methods=["GET"])
def deleteData(id, userId):
    d = DataDB(userId)
    r = d.delete(id)
    return json.dumps({"status": r})

@app.route("/update/id=<id>&cn=<CardName>&ed=<ExpireDate>&fu=<FromUser>&cc=<CardContent>&ui=<UserId>", methods=["GET"])
def updateData(id, CardName, ExpireDate, FromUser, CardContent, UserId):
    pass

@app.route("/auth", methods=['POST'])
def Auth():
    key = ""
    if(request.method == "POST"):
        key = request.form.get("key")
    else:
        abort(400)
        
    #print(key)
    if(key != config["key"]):
        return json.dumps({"status": False})
    else:
        return json.dumps({"status": True})

if __name__ == "__main__":
    app.run(debug=config["debug"], port=config["port"])