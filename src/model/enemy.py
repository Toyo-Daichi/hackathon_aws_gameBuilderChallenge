import pyxel

IMAGE_INDEX = 0
ENEMY_WIDTH = 16
ENEMY_HEIGHT = 16
BACKGROUND_COLOR = 6

class Enemy:
    x: float
    y: float
    img_initial_x: int
    img_initial_y: int
    width: int
    height: int
    speed: int
    is_alive: bool

    def __init__(self,
        x: float,
        y: float,
        img_initial_x: int,
        img_initial_y: int
    ):
        self.x = x
        self.y = y
        self.img_initial_x = img_initial_x
        self.img_initial_y = img_initial_y
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.speed = 2
        self.is_alive = True

    def update(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = pyxel.width
        self.y -= self.speed
        if self.y < 0:
            self.y = pyxel.height

    def draw(self):
        pyxel.blt(
            self.x, self.y,
            IMAGE_INDEX,
            self.img_initial_x, self.img_initial_y,
            ENEMY_WIDTH, ENEMY_HEIGHT,
            BACKGROUND_COLOR
        )
