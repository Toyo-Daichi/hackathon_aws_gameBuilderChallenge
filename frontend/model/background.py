import pyxel

class Background:
    color: int 

    def __init__(self, color: int):
        self.color = color

    def draw(self):
        pyxel.cls(self.color)
