import psycopg2
from psycopg2.extensions import connection, cursor
#
from ...context.db import Db
from ...model.character import CharacterEntity

class CharacterQuery:
    pool: connection
    _cursor: cursor

    def __init__(self, pool) -> None:
        self.pool = pool
        self._cursor = pool.cursor()

    def find_all_character(self) -> list[CharacterEntity]:
        self._cursor.execute("SELECT * from characters;")
        res = self._cursor.fetchall()
        return res

    def find_character_by_id(self, id: int) -> CharacterEntity:
        self._cursor.execute("SELECT * from characters where id = %s;", (id,))
        res = self._cursor.fetchone()
        return res
