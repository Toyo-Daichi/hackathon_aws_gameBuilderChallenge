from context.api import API
from model.api.score import ScoreEntity

END_POINT = "/scores"

class Score:
    api: API

    def __init__(self):
        self.api = API()

    def find_all_score(self) -> list[ScoreEntity]:
        res = self.api.get(END_POINT)
        return [ScoreEntity(**data) for data in res]

    def find_score_by_id(self, id: int) -> ScoreEntity:
        res = self.api.get(f"{END_POINT}/id/{id}")
        return ScoreEntity(**res)

    def find_score_by_user(self, user: str) -> ScoreEntity:
        res = self.api.get(f"{END_POINT}/user/{user}")
        return ScoreEntity(**res)

    def find_score_by_mode(self, mode: str) -> list[ScoreEntity]:
        res = self.api.get(f"{END_POINT}/mode/{mode}")
        return [ScoreEntity(**data) for data in res]

    def write_score(self, user_id: int, mode: str, score: int):
        data = {
            "user_id": user_id,
            "mode": mode,
            "score": score,
        }
        self.api.post(END_POINT, data)
