import datetime

class ScoreEntity:
    id: int
    user_id: int
    score: int
    created_at: datetime.date
    updated_at: datetime.date

    def __init__(self, id, user_id, score):
        self.id = id
        self.user_id = user_id
        self.score = score

    def __str__(self):
        return f"ScoreEntity(id={self.id}, user_id={self.user_id}, score={self.score})"
