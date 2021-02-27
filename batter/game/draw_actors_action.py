from game.action import Action

class DrawActorsAction(Action):
    def __init__(self, _output_service):
        self._output_service = _output_service
    

    def execute(self, cast):
        self._output_service.clear_screen()

        ball = cast["ball"][0]
        self._output_service.draw_actor(ball)

        paddle = cast["paddle"][0]
        self._output_service.draw_actor(paddle)

        bricks = cast["bricks"]

        for actor in bricks:
            self._output_service.draw_actor(actor)
        
        self._output_service.flush_buffer()