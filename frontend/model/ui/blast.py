import pyxel

BLAST_RADIUS = 1
BLAST_END_RADIUS = 8
BLAST_COLOR_IN = 7
BLAST_COLOR_OUT = 10

class Blast:
    x: float
    y: float
    radius: int
    is_alive: bool

    def __init__(self,
        x: float,
        y: float
    ):
        self.x = x
        self.y = y
        self.radius = BLAST_RADIUS
        self.is_alive = True

    def update(self):
        self.radius += 1
        if self.radius > BLAST_END_RADIUS:
            self.is_alive = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, BLAST_COLOR_IN)
        pyxel.circb(self.x, self.y, self.radius, BLAST_COLOR_OUT)
