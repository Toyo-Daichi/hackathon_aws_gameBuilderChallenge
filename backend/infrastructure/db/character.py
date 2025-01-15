import psycopg2
from psycopg2.extensions import connection, cursor

from context.db import Db
from model.character import CharacterEntity

class CharacterQuery:
    pool: connection
    _cursor: cursor

    def __init__(self, pool) -> None:
        self.pool = pool
        self._cursor = pool.cursor()

    def find_all_character(self) -> list[CharacterEntity]:
        self._cursor.execute("SELECT * from characters;")
        res = self._cursor.fetchall()
        return [
            CharacterEntity(
                id=row[0],
                name=row[1],
                role=row[2],
                x_coord=row[3],
                y_coord=row[4],
                created_at=row[5],
                updated_at=row[6],
            ) for row in res
        ]

    def find_character_by_id(self, id: int) -> CharacterEntity:
        self._cursor.execute("SELECT * from characters where id = %s;", (id,))
        res = self._cursor.fetchone()

        if res is None:
            raise ValueError(f"Character with id {id} not found")

        return CharacterEntity(
            id=res[0],
            name=res[1],
            role=res[2],
            x_coord=res[3],
            y_coord=res[4],
            created_at=res[5],
            updated_at=res[6],
        )

    def find_character_by_name(self, name: str) -> CharacterEntity:
        self._cursor.execute("SELECT * from characters where name = %s;", (name,))
        res = self._cursor.fetchone()

        if res is None:
            raise ValueError(f"Character with id {id} not found")

        return CharacterEntity(
            id=res[0],
            name=res[1],
            role=res[2],
            x_coord=res[3],
            y_coord=res[4],
            created_at=res[5],
            updated_at=res[6],
        )

    def find_character_by_role(self, role: str) -> list[CharacterEntity]:
        self._cursor.execute("SELECT * from characters where role = %s;", (role,))
        res = self._cursor.fetchall()
        return [
            CharacterEntity(
                id=row[0],
                name=row[1],
                role=row[2],
                x_coord=row[3],
                y_coord=row[4],
                created_at=row[5],
                updated_at=row[6],
            ) for row in res
        ]
