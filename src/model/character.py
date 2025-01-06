import datetime

from src.infrastructure.db import character

class CharacterEntity:
    id: int
    name: str
    role: str 
    x_coord: int
    y_coord: int
    created_at: datetime.date
    updated_at: datetime.date

    def __init__(self,
        id: int,
        name: str,
        role: str,
        x_coord: int,
        y_coord: int,
        created_at: datetime.date,
        updated_at: datetime.date
    ) -> None:
        self.id = id
        self.name = name
        self.role = role
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.created_at = created_at
        self.updated_at = updated_at
