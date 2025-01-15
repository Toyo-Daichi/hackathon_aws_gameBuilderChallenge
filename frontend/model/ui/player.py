import pyxel

from model.ui.blast import Blast
from model.ui.bullet import Bullet

from util.state import *

IMAGE_INDEX = 0
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 16
PLAYER_SPEED = 2
BACKGROUND_COLOR = 6

class Player:
    x: float
    y: float
    x_coord: int
    y_coord: int
    width: int
    height: int
    speed: int
    is_alive: bool
    bullets: list[Bullet]
    blasts: list[Blast]

    def __init__(self,
        x: float,
        y: float,
        x_coord: int,
        y_coord: int,
        bullets: list[Bullet] = [],
        blasts: list[Blast] = []
    ):
        self.x = x
        self.y = y
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.speed = 2
        self.is_alive = True
        self.bullets = bullets 
        self.blasts = blasts

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(self.x - 1, 0)
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.x = min(self.x + 1, pyxel.width - 8)
        elif pyxel.btn(pyxel.KEY_UP):
            self.y = max(self.y - 1, 0)
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.y = min(self.y + 1, pyxel.height - 8)
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.bullets.append(Bullet(self.x + int(PLAYER_WIDTH/2), self.y))

        update_states(self.bullets)
    
    def draw(self):
        pyxel.blt(
            self.x, self.y,
            IMAGE_INDEX,
            self.x_coord, self.y_coord,
            self.width, self.height,
            BACKGROUND_COLOR
        )
        draw_states(self.bullets)
