import psycopg2
from psycopg2.extensions import connection, cursor
from ...context.db import Db


class UserQuery:
    pool: connection

    def __init__(self, pool) -> None:
        self.pool = pool
        self._cursor = pool.cursor()

    def read_user(self):
        res = self._cursor.cur("SELECT * from users;")
        return res
