from game.actor import Actor
from game import constants
from game.point import Point

class Paddle(Actor):
    def __init__(self):
        super().__init__()
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y - 1)
        self.position = Point(x, y)
        self.set_text("===========")
        self.set_position(self.position)

    def get_position(self):
        return self.positiony
    def move_right(self):
        pass
    def move_left(self):
        pass
