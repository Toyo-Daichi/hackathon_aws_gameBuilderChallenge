#-*- coding: utf-8 -*-
"""
Created on 2024.12.22
"""

import pyxel
import json
import os

GAME_TITLE = os.environ['GAME_TITLE']
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 160

class App:
    gamestate: GameState

    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title=GAME_TITLE)
        self.game_state = Gamestate()
        self.scene_manager = SceneManager()
        pyxel.run(self.update, self.draw)
