import pyxel
import os

from context.gamestate import GameState

GAME_TITLE = 'PACKET SHOOTING GAME'

class Title:
    gamestate: GameState

    def __init__(self):
        self.gamestate = GameState()

    def update(self):
        if pyxel.btnp(pyxel.KEY_N):
            self.gamestate.set_mode("Normal")
            self.gamestate.set_state("PLAY")
        elif pyxel.btnp(pyxel.KEY_D):
            self.gamestate.set_mode("DoS")
            self.gamestate.set_state("PLAY")
        elif pyxel.btnp(pyxel.KEY_S):
            self.gamestate.set_mode("DDoS")
            self.gamestate.set_state("PLAY")

    def draw(self):
        pyxel.text(
            int(pyxel.width/2) - 40,
            int(pyxel.height/2) - 30,
            GAME_TITLE,
            pyxel.frame_count % 4
        )
        pyxel.text(
            30,
            int(pyxel.height/2) + 10,
            " - CHOICE GAME MODE [N]ormal, [D]oS, [S]pecial mode DDoS - ",
            7
        )
