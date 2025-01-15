from context.api import API
from model.api.character import CharacterEntity

END_POINT = "/characters"

class Character:
    api: API

    def __init__(self) -> None:
        self.api = API()

    def find_all_character(self) -> list[CharacterEntity]:
        res = self.api.get(END_POINT)
        return [CharacterEntity(**data) for data in res]

    def find_character_by_id(self, id: int) -> CharacterEntity:
        res = self.api.get(f"{END_POINT}/id/{id}")
        return CharacterEntity(**res)

    def find_character_by_name(self, name: str) -> CharacterEntity:
        res = self.api.get(f"{END_POINT}/name/{name}")
        return CharacterEntity(**res)

    def find_character_by_role(self, role: str) -> list[CharacterEntity]:
        res = self.api.get(f"{END_POINT}/role/{role}")
        return [CharacterEntity(**data) for data in res]
