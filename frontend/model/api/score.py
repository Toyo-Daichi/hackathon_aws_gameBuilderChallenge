import datetime

class ScoreEntity:
    id: int
    user_id: int
    mode: str
    score: int
    created_at: datetime.date

    def __init__(self,
        id: int,
        user_id: int,
        mode: str,
        score: int,
        created_at: datetime.date,
    ) -> None:
        self.id = id
        self.user_id = user_id
        self.mode = mode
        self.score = score
        self.created_at = created_at

    def __str__(self):
        return f"ScoreEntity(id={self.id}, user_id={self.user_id}, score={self.score})"

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "mode": self.mode,
            "score": self.score,
            "created_at": self.created_at,
        }
