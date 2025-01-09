import datetime
import psycopg2
from psycopg2.extensions import connection, cursor
#
from ...context.db import Db
from ...model.db.score import ScoreEntity

class ScoreQuery:
    pool: connection
    _cursor: cursor

    def __init__(self, pool) -> None:
        self.pool = pool
        self._cursor = pool.cursor()

    def find_all_score(self) -> list[ScoreEntity]:
        self._cursor.execute("SELECT * from scores;")
        res = self._cursor.fetchall()
        return [
            ScoreEntity(
                id=row[0],
                user_id=row[1],
                score=row[2],
                mode=row[3],
                created_at=row[4]
            ) for row in res
        ]

    def find_score_by_id(self, id: int) -> ScoreEntity:
        self._cursor.execute("SELECT * from scores where id = %s;", (id,))
        res = self._cursor.fetchone()

        if res is None:
            raise ValueError(f"Character with id {id} not found")

        return ScoreEntity(
            id=res[0],
            user_id=res[1],
            mode=res[2],
            score=res[3],
            created_at=res[4]
        )

    def find_score_by_user_id(self, user_id: int) -> ScoreEntity:
        self._cursor.execute("SELECT * from scores where user_id = %s;", (user_id,))
        res = self._cursor.fetchone()

        if res is None:
            raise ValueError(f"Character with id {id} not found")

        return ScoreEntity(
            id=res[0],
            user_id=res[1],
            mode=res[2],
            score=res[3],
            created_at=res[4]
        )

    def find_score_by_mode(self, mode: str, limit: int = 5) -> list[ScoreEntity]:
        self._cursor.execute("SELECT * from scores where gamemode = %s ORDER BY value DESC LIMIT %s;", (mode, limit))
        res = self._cursor.fetchall()
        return [
            ScoreEntity(
                id=row[0],
                user_id=row[1],
                mode=row[2],
                score=row[3],
                created_at=row[4]
            ) for row in res
        ]

class ScoreRepository:
    pool: connection
    _cursor: cursor

    def __init__(self, pool):
        self.pool = pool
        self._cursor = pool.cursor()

    def write_score(self, user_id: int, mode: str, score: int):
        self._cursor.execute(
            f"INSERT INTO scores (user_id, gamemode, value, create_at) VALUES (%s, %s, %s, %s);", (
                user_id,
                mode,
                score,
                datetime.datetime.now(),
            )
        )
        self.pool.commit()
