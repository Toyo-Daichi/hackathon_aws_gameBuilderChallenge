import pyxel

PLAYER_WIDTH = 8
PLAYER_HEIGHT = 8
PLAYER_SPEED = 2
PLAYER_IMG_BANK = 0

class Player:
    x: float
    y: float
    width: int
    height: int
    speed: int
    is_alive: bool
    img_path: str

    def __init__(self,
        x: float,
        y: float,
        path: str
    ):
        self.x = x
        self.y = y
        self.width = 8
        self.height = 8
        self.speed = 2
        self.is_alive = True
        self.path = path

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(self.x - 1, 0)

    def draw(self):
        pass
