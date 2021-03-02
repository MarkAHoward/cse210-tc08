from game.actor import Actor
from game import constants
from game.point import Point
import random

class Paddle(Actor):
    def __init__(self):
        super().__init__()
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y - 1)
        self.position = Point(x, y)
        self.set_text("===========")
        self.set_position(self.position)

    def change_paddle(self):
        rando = random.randint(1,2)
        if rando == 1:
            self.set_text("=================")
        else:
            self.set_text("=====")

        