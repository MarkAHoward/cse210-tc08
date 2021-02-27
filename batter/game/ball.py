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
        velocity = self.get_velocity()
        y = velocity.get_y()
        x1 = velocity.get_x()
        x = x1 * (-1)
        velocity = Point(x, y)
        self.set_velocity(velocity)

    def bounce_vertical(self):
        velocity = self.get_velocity()
        x = velocity.get_x()
        y1 = velocity.get_y()
        y = y1 * (-1)
        velocity = Point(x, y)
        self.set_velocity(velocity)
