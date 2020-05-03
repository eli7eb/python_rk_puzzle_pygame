import pygame,  sys
from rk_code.rk_settings.rk_states import State
#from rk_code.rk_states.rk_game_start import StartState


class EndState(State):
    def __init__(self):
        State.__init__(self)
        self.message = "Congratulations! You won!"
        self.btn = "No buttons in Pygame (yet)."
        self.message2 = "Click anywhere to Play again"
        self.location = (20, 120)
        self.location2 = (20, 180)
#        self.nextState = StartState

    def draw(self):
        State.draw(self)
        self.draw_text(self.message)
        self.draw_text(self.message2, 144)

    # demonstrate that some states need not override my_setup()
