import pyxel

from context.api import API
from context.gamestate import GameState
from service.score import Score
from util.state import *

class Result:
    gamestate: GameState
    api: API
    ranking: list
    ranking_fetched: bool

    def __init__(self):
        self.gamestate = GameState()
        self.api = API()
        self.ranking = []
        self.ranking_fetched = False

    def update(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.gamestate.state = "START"
            self.ranking_fetched = False

    def draw(self):
        if not self.ranking_fetched:
           score = Score()
           self.ranking = score.find_score_by_mode(self.gamestate.get_mode())
           self.ranking_fetched = True 

        pyxel.text(55, 55, "GAME OVER ...", 1)
        pyxel.text(55, 70, f"YOUR SCORE is", 1)
        pyxel.text(120, 70, f"{self.gamestate.get_score()}", pyxel.frame_count % 4)

        pyxel.text(55, 100, f"RANKING of {self.gamestate.get_mode()} MODE", 1)
        for index, _ranking in enumerate(self.ranking):
            if _ranking.score == self.gamestate.get_score():
                pyxel.text(55, 110 + index*10, f"{index+1}: {_ranking.score}", pyxel.frame_count % 4)
            else:
                pyxel.text(55, 110 + index*10, f"{index+1}: {_ranking.score}", 1)
