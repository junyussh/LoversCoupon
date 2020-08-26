import sqlite3

users = []

class UserModel:
    id = 0

    def __init__(self, name, password, birth, sex, phone, email, id=0):
        if(id == 0):
            self.id = self.id + 1
        else:
            self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.birth = birth
        self.sex = sex
        self.phone = phone

    def add_user(self):
        conn = sqlite3.connect('main.db')
        cursor = conn.cursor()
        insert_query = 'INSERT INTO users (name, password, sex, birth, phone, email) \
        VALUES(?, ?, ?, ?, ?, ?, ?)'
        cursor.execute(insert_query, (self.name, self.password, self.sex,
                       self.birth, self.phone, self.email))
        conn.commit()
        conn.close()
        #users.append(self)

    @staticmethod
    def get_user(id):
        user = None
        conn = sqlite3.connect('main.db')
        cursor = conn.cursor()
        query_one_query = 'SELECT * FROM users WHERE id=?'
        print(query_one_query)
        result = cursor.execute(query_one_query, (str(id),)).fetchone()
        if result is None:
            return None
        print(result)
        user = UserModel(id=result[0], name=result[1], password=result[2], sex = result[3], birth=result[4], phone=result[5], email=result[6])
        #user.id = result[0]
        conn.close()
        return user

    @staticmethod
    def delete_user(id):
        global users
        users = [item for item in users if item.id != id]

    @staticmethod
    def get_all_user():
        return users