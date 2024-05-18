import sqlite3
from project import app
from project import DB_NAME

class DataBase:

    @staticmethod
    def conn():
        conn = None
        try:
            conn = sqlite3.connect(DB_NAME)
        except sqlite3.Error as e:
            print("Ошибка подключения к БД" + str(e))
        return conn

    @staticmethod
    def create_db():
        conn = DataBase.conn()
        with app.open_resource("sq_db.sql", mode="r") as f:
            conn.cursor().executescript(f.read())
        conn.commit()
        conn.close()

    @staticmethod
    def get_info_by_name(name: str):
        conn = DataBase.conn()
        cursor = conn.cursor()
        query = "SELECT * FROM places_objects WHERE name = ?"
        try:
            res = cursor.execute(query, (name,)).fetchone()

            if not res:
                print("Место не найдено")
                return None
            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД" + str(e))
            return None
        finally:
            conn.close()

