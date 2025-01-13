from context.db import Db
from infrastructure.db.user import UserQuery
from model.db.user import UserEntity

class User:
    database: Db
    query: UserQuery

    def __init__(self, database: Db) -> None:
        self.database = database
        self.query = UserQuery(database.pool)
