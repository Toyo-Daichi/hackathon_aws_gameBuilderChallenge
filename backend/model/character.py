import datetime

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
    ):
        self.id = id
        self.name = name
        self.role = role
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"CharacterEntity(id={self.id}, name={self.name})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "x_coord": self.x_coord,
            "y_coord": self.y_coord,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
