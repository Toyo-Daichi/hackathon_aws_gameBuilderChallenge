#-*- coding: utf-8 -*-
"""
Created on 2024.12.22
"""

import pyxel
import os
#
from .context.gamestate import GameState
from .context.db import Db

GAME_TITLE = os.environ['GAME_TITLE']
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 80

class App:
    gamestate: GameState
    database: Db

    def __init__(self):
        self.gamestate = GameState()
        self.Db = Db()

        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.font(0, 0, GAME_TITLE)

if __name__ == "__main__":
    app = App()
