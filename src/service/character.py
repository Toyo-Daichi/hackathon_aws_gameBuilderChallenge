from ..context.db import Db
from ..infrastructure.db.character import CharacterQuery
from ..model.db.character import CharacterEntity

class Character:
    database: Db
    query: CharacterQuery

    def __init__(self, database: Db) -> None:
        self.database = database
        self.query = CharacterQuery(database.pool)

    def find_all_character(self) -> list[CharacterEntity]:
        return self.query.find_all_character()

    def find_character_by_id(self, id: int) -> CharacterEntity:
        return self.query.find_character_by_id(id)

    def find_character_by_name(self, name: str) -> CharacterEntity:
        return self.query.find_character_by_name(name)

    def find_character_by_role(self, role: str) -> list[CharacterEntity]:
        return self.query.find_character_by_role(role)
