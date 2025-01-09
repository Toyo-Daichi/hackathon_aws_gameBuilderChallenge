import pyxel

BULLET_WIDTH = 2
BULLET_RADIUS = 2
BULLET_COLOR = 8

class Bullet:
    x: float
    y: float
    radius: int
    speed: int
    is_alive: bool

    def __init__(self,
        x: float,
        y: float
    ):
        self.x = x
        self.y = y
        self.radius = BULLET_RADIUS
        self.speed = 2
        self.is_alive = True

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            self.is_alive = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, BULLET_COLOR)
