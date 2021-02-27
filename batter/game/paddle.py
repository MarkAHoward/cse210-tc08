from game.actor import Actor
from game import constants
from game.point import Point

class Paddle:
    def __init__(self)
        super().__init__()
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y - 1)
        position = Point(x, y)
        self.set_text("===========")
        self.set_position(position)


