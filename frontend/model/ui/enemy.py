import pyxel
import random

IMAGE_INDEX = 0
ENEMY_WIDTH = 16
ENEMY_HEIGHT = 16
BACKGROUND_COLOR = 6

class Enemy:
    x: float
    y: float
    x_coord: int
    y_coord: int
    width: int
    height: int
    speed: int
    is_alive: bool

    def __init__(self,
        x: float,
        y: float,
        x_coord: int,
        y_coord: int
    ):
        self.x = x
        self.y = y
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.speed = 2
        self.is_alive = True

    def update(self):
        self.x = self.x + self.speed*random.choice([-1, 0, 1])
        if self.x < 0:
            self.x = pyxel.width
        elif self.x > pyxel.width:
            self.x = 0
        self.y += self.speed
        if self.y < 0:
            self.y = pyxel.height
        elif self.y > pyxel.height:
            self.y = 0

    def draw(self):
        pyxel.blt(
            self.x, self.y,
            IMAGE_INDEX,
            self.x_coord, self.y_coord,
            ENEMY_WIDTH, ENEMY_HEIGHT,
            BACKGROUND_COLOR
        )
