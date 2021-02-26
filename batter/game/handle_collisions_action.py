import random
from game import constants
from game.action import Action

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
        marquee = cast["marquee"][0] # there's only one
        robot = cast["robot"][0] # there's only one
        artifacts = cast["artifact"]
        marquee.set_text("")
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                description = artifact.get_description()
                marquee.set_text(description) 