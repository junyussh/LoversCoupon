import os
import json

class DataIO():

    def __init__(self, UserId):
        self.UserId = UserId
        self.data = json.loads(self.read())

    def save(self, CardName, ExpireDate, FromUser, CardContent):
        NewData = {
                    "CardName": CardName,
                    "ExpireDate": ExpireDate,
                    "FromUser": FromUser,
                    "CardContent": CardContent
                }
        try:
            self.data["card"].append(NewData)
            #print(type(self.data))
            try:
                f = open(os.path.join("data", self.UserId + ".txt"), "w", encoding="utf-8")
                f.write(json.dumps(self.data))
                f.close()
            except IOError as identifier:
                return str(identifier)
                
            return str(True)
        except Exception as identifier:
            return str(identifier)

    def read(self):
        try:
            f = open(os.path.join("data", self.UserId + ".txt"), "r", encoding="utf-8")
            return f.read()
        except IOError as identifier:
            return str(identifier)

if __name__ == "__main__":
    d = DataIO("0")
    print(d.read())

