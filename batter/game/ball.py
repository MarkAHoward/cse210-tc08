from game.actor import Actor
from game import constants
from game.point import Point

class Ball(Actor):
    def __init__(self):
        super().__init__()
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)
        velocity = Point(1, -1)
        self.set_text("@")
        self.set_position(position)
        self.set_velocity(velocity)
    
    def bounce_horizantal(self):
        pass

    def bounce_vertical(self):
        pass