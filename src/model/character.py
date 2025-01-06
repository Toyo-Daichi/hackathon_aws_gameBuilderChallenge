import datetime

class CharacterEntity:
    id: int
    name: str
    role: str 
    path: str
    created_at: datetime.date
    updated_at: datetime.date

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"CharacterEntity(id={self.id}, name={self.name})"
