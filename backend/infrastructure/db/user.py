import psycopg2
from psycopg2.extensions import connection, cursor
#
from context.db import Db
from model.db.user import UserEntity

class UserQuery:
    pool: connection
    _cursor: cursor

    def __init__(self, pool) -> None:
        self.pool = pool
        self._cursor = pool.cursor()

    def find_all_user(self) -> list[UserEntity]:
        self._cursor.execute("SELECT * from users;")
        res = self._cursor.fetchall()
        return res

    def find_user_by_id(self, id: int) -> UserEntity:
        self._cursor.execute("SELECT * from users where id = %s;", (id,))
        res = self._cursor.fetchone()
        return res
