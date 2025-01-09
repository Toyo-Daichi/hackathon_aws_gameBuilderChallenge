#-*- coding: utf-8 -*-
"""
Created on 2024.12.22
"""

import pyxel
import os

from .context.gamestate import GameState
from .model.ui.background import Background
from .scene.title import Title
from .scene.play import Play
from .scene.result import Result

from .util.state import *
from .util.logger import Logger
logging = Logger(__name__, "DEBUG")

GAME_TITLE = os.environ['GAME_TITLE']
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 250
BACKGROUND_COLOR = 13

class App:
    gamestate: GameState
    #
    title: Title
    play: Play
    result: Result

    def __init__(self):
        logging.info(f"{GAME_TITLE} Game started")
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=60)
        logging.info("Assets loaded mario.pyxres")
        pyxel.load("./assets/pyxres/mario.pyxres")

        self.gamestate = GameState()
        self.title = Title()
        self.play = Play()
        self.result = Result()

        logging.info("pyxel.run")
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.gamestate.state == "START":
            self.title.update()
        elif self.gamestate.state == "PLAY":
            self.play.update()
        elif self.gamestate.state == "RESULT":
            self.result.update()

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        Background(BACKGROUND_COLOR).draw()

        if self.gamestate.state == "START":
            self.title.draw()
        elif self.gamestate.state == "PLAY":
            self.play.draw()
        elif self.gamestate.state == "RESULT":
            self.result.draw()
        
if __name__ == "__main__":
    app = App()
