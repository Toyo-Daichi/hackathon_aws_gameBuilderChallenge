import datetime

class UserEntity:
    id: int
    name: str
    chararacter_id: int
    created_at: datetime.date
    updated_at: datetime.date

    def __init__(self,
        id: int,
        name: str,
        chararacter_id: int,
        created_at: datetime.date,
        updated_at: datetime.date
    ):
        self.id = id
        self.name = name
        self.chararacter_id = chararacter_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"UserEntity(id={self.id}, name={self.name})"
