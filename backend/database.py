import sqlite3
import os
import json
import logging

LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
DATE_FORMAT = '%Y%m%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT, datefmt=DATE_FORMAT)

class DataDB():
    def __init__(self, _UserId):
        self.UserId = _UserId
        self.DBPath = os.path.join("data", "main.db")
        self.DataTemplate = {
            "user": "",
            "card": [{
                	"Id": 0,
	                "UserId":"0",
                    "CouponName": "template",
                    "CouponContent": "template",
                    "ExpireDate": "template",
                    "FromUser": "1",
                    "CouponStatus":0
            }]
        }

    #https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
    def _dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d    

    def RunDBCommand(self, cmd):
        try:
            conn = sqlite3.connect(self.DBPath)
            c = conn.cursor()
            c.execute(cmd)
            conn.commit()
            conn.close()
            return "ok"
        except Exception as identifier:
            return str(identifier)

    def write(self, CardName, ExpireDate, FromUser, CardContent):
        cmd = 'insert into coupon(UserId, CouponName, CouponContent, ExpireDate, FromUser, CouponStatus) values ("{0}", "{1}", "{2}", "{3}", "{4}", "1")'.format(
            self.UserId, CardName, CardContent, ExpireDate, FromUser)

        response = self.RunDBCommand(cmd)
        if(response != "ok"):
            logging.error("Err: " + response)
            return False
        return True

    def read(self):

        cmd = 'SELECT * FROM coupon WHERE UserId="{0}"'.format(self.UserId)
        logging.debug(cmd)

        try:
            conn = sqlite3.connect(self.DBPath)
            conn.row_factory = self._dict_factory
            c = conn.cursor()
            c.execute(cmd)
            self.rows = c.fetchall()
        except Exception as identifier:
            logging.error("Err: " + str(identifier))
            return False

        logging.debug(self.rows)
        return self.rows

    def delete(self, id):
        cmd = 'DELETE FROM coupon WHERE Id="{0}"'.format(id)

        response = self.RunDBCommand(cmd)
        if(response != "ok"):
            logging.error("Err: " + response)
            return False
        return True

    def update(self):
        pass

    def ReadFormateData(self):
        data = self.DataTemplate
        data["user"] = self.UserId
        data["card"] = self.read()

        return json.dumps(data)

if __name__ == "__main__":
    d = DataDB("0")
    #print(d.write( "CardName", "ExpireDate", "FromUser", "CardContent"))
    logging.debug(d.ReadFormateData())
