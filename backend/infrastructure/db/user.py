import psycopg2
from psycopg2.extensions import connection, cursor
#
from context.db import Db
from model.user import UserEntity

class UserQuery:
    pool: connection
    _cursor: cursor

    def __init__(self, pool) -> None:
        self.pool = pool
        self._cursor = pool.cursor()
