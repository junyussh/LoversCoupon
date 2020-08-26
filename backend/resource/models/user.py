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
    def get_user(self, id):
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
        user.id = result[0]
        conn.close()
        return user

    @staticmethod
    def delete_user(self, id):
        conn = sqlite3.connect('main.db')
        cursor = conn.cursor()
        delete_query = 'DELETE FROM users WHERE id=?'
        cursor.execute(delete_query, (id,))
        conn.commit()
        conn.close()

    def update_user(self):
        conn = sqlite3.connect('main.db')
        cursor = conn.cursor()
        update_query = 'UPDATE users SET name=?, password=?, sex=?, birth=?, phone=?, email=? WHERE id=?'
        cursor.execute(update_query, (self.name, self.password, self.sex,
                       self.birth, self.phone, self.email, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_user():
        users = []
        conn = sqlite3.connect('main.db')
        cursor = conn.cursor()
        query_one_query = 'SELECT * FROM users'
        for item in cursor.execute(query_one_query):
            user = UserModel(id=item[0], name=item[1], password=item[2], sex = item[3], birth=item[4], phone=item[5], email=item[6])
            users.append(user)
        conn.close()
        return users