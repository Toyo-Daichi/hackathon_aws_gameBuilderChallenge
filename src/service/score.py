from context.db import Db
from infrastructure.db.score import ScoreQuery, ScoreRepository
from model.db.score import ScoreEntity

class Score:
    database: Db
    query: ScoreQuery
    repository: ScoreRepository

    def __init__(self, database: Db):
        self.database = database
        self.query = ScoreQuery(database.pool)
        self.repository = ScoreRepository(database.pool)

    def find_all_score(self) -> list[ScoreEntity]:
        return self.query.find_all_score()

    def find_score_by_id(self, id: int) -> ScoreEntity:
        return self.query.find_score_by_id(id)

    def find_score_by_user_id(self, user_id: int) -> ScoreEntity:
        return self.query.find_score_by_user_id(user_id)

    def find_score_by_mode(self, mode: str) -> list[ScoreEntity]:
        return self.query.find_score_by_mode(mode)

    def write_score(self, user_id: int, mode: str, score: int):
        self.repository.write_score(user_id, mode, score)
