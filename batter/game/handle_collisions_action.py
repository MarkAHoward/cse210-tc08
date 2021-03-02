import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        bricks = cast["bricks"]
        # marquee.set_text("")

        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                if brick._text == "O":
                    ball.bounce_vertical()
                    brick.remove_brick()
                    paddle.change_paddle()
                else:
                    brick.remove_brick()
                    ball.bounce_vertical()

        if ball.get_position().equals(paddle.get_position()):
            ball.bounce_vertical()

        for i in range(0, constants.MAX_Y + 1):
            if ball.get_position().equals(Point(0,i)):
                ball.bounce_horizantal()
            if ball.get_position().equals(Point(constants.MAX_X,i)):
                ball.bounce_horizantal()
        
        for i in range(0, constants.MAX_X + 1):
            if ball.get_position().equals(Point(i,0)):
                ball.bounce_vertical()
            # if ball.get_position().equals(Point(i,constants.MAX_Y)):
                # ball.bounce_vertical()
        
        for i in range(0, constants.MAX_X + 1):
            if paddle.get_position().equals(Point(i, constants.MAX_Y - 1)):
                    for j in range(i, i + 6):
                        if ball.get_position().equals(Point(j, constants.MAX_Y - 1)):
                            if ball.get_velocity().equals(Point(-1, 1)):
                                ball.bounce_vertical()
                            else:
                                ball.bounce_vertical()
                                ball.bounce_horizantal()
                    num = 10
                    if paddle._text == "=================":
                        num += 6
                    elif paddle._text == "=====":
                        num -= 4
                    else:
                        num == 10
                    for j in range(i + 6, i + num):
                        if ball.get_position().equals(Point(j, constants.MAX_Y - 1)):
                            if ball.get_velocity().equals(Point(1, 1)):
                                ball.bounce_vertical()
                            else:
                                ball.bounce_vertical()
                                ball.bounce_horizantal()