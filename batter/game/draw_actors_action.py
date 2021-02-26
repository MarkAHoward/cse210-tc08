from game.action import Action

# TODO: Define the DrawActorsAction class here

class DrawActorsAction(Action):
    def __init__(self, _output_service):
        self._output_service = _output_service
    

    def execute(self, cast):
        self._output_service.clear_screen()

        marquee = cast["marquee"][0]
        self._output_service.draw_actor(marquee)

        robot = cast["robot"][0]
        self._output_service.draw_actor(robot)

        artifacts = cast["artifact"]

        for actor in artifacts:
            self._output_service.draw_actor(actor)
        
        self._output_service.flush_buffer()