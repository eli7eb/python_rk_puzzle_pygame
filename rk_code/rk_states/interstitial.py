import pygame, os, sys
from pygame.locals import *
from rk_code.rk_utils.bitmap_font import *
from rk_code.rk_settings.rk_states_manager import *
from rk_code.rk_data.rk_consts import *

"""
----------------------------------------------------------------------------------------------------
	InterstitialState
	
	Displays a message between screens. Can be used for ''Game over'' or ''Get ready'' style
	messages
----------------------------------------------------------------------------------------------------
"""


class InterstitialState(GameState):

    def __init__(self, game, msg, waitTimeMs, nextState):
        super(InterstitialState, self).__init__(game)
        self.nextState = nextState
        self.font = BitmapFont('fasttracker2-style_12x12.png', 12, 12)
        self.message = msg
        self.waitTimer = waitTimeMs
        self.doneImage = False

    def update(self, gameTime):
        self.waitTimer -= gameTime
        if (self.message == GLOBAL_GAME_GET_READY_MSG and self.doneImage == False):
            self.getImageToSplit()
        elif (self.waitTimer < 0):
            self.game.changeState(self.nextState, self.game.params)

    def draw(self, surface):
        self.font.centre(surface, self.message, surface.get_rect().height / 2)

    def getImageToSplit(self):
        self.mood_string = self.game.params[0] if (len(self.game.params[0]) > 0) else 'random'
