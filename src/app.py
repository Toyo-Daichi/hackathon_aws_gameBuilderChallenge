#-*- coding: utf-8 -*-
"""
Created on 2024.12.22
"""

import pyxel
import json
import os
#
from .context.gamestate import GameState
from .context.db import Db
from .infrastructure.db.user import UserQuery

GAME_TITLE = os.environ['GAME_TITLE']
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 160

class App:
    gamestate: GameState
    database: Db

    def __init__(self):
        self.gamestate = GameState()
        self.Db = Db()

    def read(self):
        test = UserQuery(self.Db.pool)
        print(test.read_user())
    
if __name__ == "main":
    App()
