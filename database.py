import psycopg2 as dbapi2

class Database:
    def __init__(self, host="", user="", 
                passwd="", db=""):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
    
    def add_user(self,username,password):
        with dbapi2.connect(host=self.host, user=self.user, password=self.passwd, dbname=self.db) as connection:
            cursor = connection.cursor()
            try:
                statement = """INSERT INTO users(username,password_) VALUES(%s,%s)"""
                cursor.execute(statement,(username,password))
                connection.commit()
                cursor.close()
            except dbapi2.IntegrityError:
                connection.rollback()
                return False
        return True
    
    def get_user(self,username):
        with dbapi2.connect(host=self.host, user=self.user, password=self.passwd, dbname=self.db) as connection:
            cursor = connection.cursor()
            statement = """SELECT * FROM users WHERE username  = %s"""
            cursor.execute(statement,(username,))
            fetch = cursor.fetchall()
            if(len(fetch) == 0):
                cursor.close()
                return None
            cursor.close()
            return fetch

    def addData(self,username,password,application,user):
        with dbapi2.connect(host=self.host, user=self.user, password=self.passwd, dbname=self.db) as connection:
            cursor = connection.cursor()
            user_id = self.get_user(user)
            try:
                statement = """INSERT INTO datas(user_id,username,password_,application) VALUES(%s,%s,%s,%s)"""
                cursor.execute(statement,(user_id[0][0],username,password,application))
                connection.commit()
                cursor.close()
            except dbapi2.IntegrityError:
                connection.rollback()
                return False
        return True
    
    def get_list(self,username):
        with dbapi2.connect(host=self.host, user=self.user, password=self.passwd, dbname=self.db) as connection:
            user_id = self.get_user(username)
            if user_id is not None:
                cursor = connection.cursor()
                statement = """SELECT * FROM datas WHERE user_id = %s"""
                cursor.execute(statement,(user_id[0][0],))
                fetch = cursor.fetchall()
                if(len(fetch) == 0):
                    cursor.close()
                    return None
                cursor.close()
                return fetch
            return None
    
    def delete_data(self, data_id):
        with dbapi2.connect(host=self.host, user=self.user, password=self.passwd, dbname=self.db) as connection:
            cursor = connection.cursor()
            try:
                statement = """DELETE FROM datas WHERE data_id = %s"""
                cursor.execute(statement,(data_id,))
                connection.commit()
                cursor.close()
            except dbapi2.IntegrityError:
                connection.rollback()
                return False
        return True
