from game.actor import Actor
from game.point import Point

class Brick(Actor):
    def __init__(self, x, y):
        super().__init__()
        position = Point(x, y)
        self.set_text("*")
        self.set_position(position)
    
    def remove_brick(self):
        position = Point(-1, 0)
        self.set_position(position)
    
    def insert_powerup(self):
        self.set_text("O")
