import psycopg2
from psycopg2.extensions import connection, cursor
#
from ...context.db import Db
from ...model.score import ScoreEntity

class ScoreQuery:
    pool: connection
    _cursor: cursor

    def __init__(self, pool) -> None:
        self.pool = pool
        self._cursor = pool.cursor()

    def find_all_score(self) -> list[ScoreEntity]:
        self._cursor.execute("SELECT * from scores;")
        res = self._cursor.fetchall()
        return res

    def find_score_by_id(self, id: int) -> ScoreEntity:
        self._cursor.execute("SELECT * from scores where id = %s;", (id,))
        res = self._cursor.fetchone()
        return res

    def find_score_by_user_id(self, user_id: int) -> ScoreEntity:
        self._cursor.execute("SELECT * from scores where user_id = %s;", (user_id,))
        res = self._cursor.fetchone()
        return res
