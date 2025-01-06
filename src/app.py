#-*- coding: utf-8 -*-
"""
Created on 2024.12.22
"""

import pyxel
import os

from src.infrastructure.db import character
#
from .context.gamestate import GameState
from .context.db import Db
from .model.enemy import Enemy
from .service.character import Character
from src.model import enemy
#
from .util.logger import Logger
logging = Logger(__name__, "DEBUG")

GAME_TITLE = os.environ['GAME_TITLE']
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 250

class App:
    gamestate: GameState
    database: Db
    #
    character: Character
    #
    enemy: list[Enemy]

    def __init__(self):
        self.gamestate = GameState()
        self.Db = Db()

        self.character = Character(self.Db)
        enemies = self.character.find_all_character()

        self.enemy = []

        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=60)
        logging.info(f"Game started: {GAME_TITLE}")
        pyxel.load("./assets/pyxres/mario.pyxres")
        logging.info("Assets loaded")

        for index, enemy in enumerate(enemies):
            self.enemy.append(Enemy(
                28 + index*16,
                8,
                enemy.x_coord,
                enemy.y_coord
            ))
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        for enemy in self.enemy:
            enemy.update()

    def update_player(self):
        if pyxel.btn(pyxel.KEY_R):
            self.player_x = max(self.player_x - 2, 0)

        if pyxel.btn(pyxel.KEY_L):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)

        if pyxel.btn(pyxel.KEY_2) :
            self.player_y = max(self.player_y - 2, 0)

        if pyxel.btn(pyxel.KEY_3):
            self.player_y = min(self.player_y + 2, pyxel.height - 16)

    def draw(self):
        pyxel.cls(0)
        for enemy in self.enemy:
            enemy.draw()
    #    pyxel.rect(self.x, 0, self.x + 7, 7, 9)
    #    pyxel.blt(self.player_x, self.player_y, 0, 64, 0, 16, 16, 6)

if __name__ == "__main__":
    app = App()
