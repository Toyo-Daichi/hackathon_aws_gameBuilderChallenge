import datetime

class UserEntity:
    id: int
    name: str
    chararacter_id: int
    created_at: datetime.date
    updated_at: datetime.date

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"UserEntity(id={self.id}, name={self.name})"
