import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 
from game.ball import Ball
from game.brick import Brick
from game.paddle import Paddle

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}


    paddle = Paddle()
    cast["paddle"] = [paddle]

    bricks = []
    for x in range(5, 75):
        for y in range(2, 6):
            rando = random.randint(1,20)
            if rando == 5:
                brick = Brick(x, y)
                brick.insert_powerup()
                bricks.append(brick)
            else:
                brick = Brick(x, y)
                bricks.append(brick)

    cast["bricks"] = bricks

    ball = Ball()
    cast["ball"] = [ball]
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_acition = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_acition]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)