import pygame, os, sys
from pygame.locals import *
from rk_code.rk_settings.rk_states_manager import GameState

class PlayGameState(GameState):

    def __init__(self, game, gameOverState):
        super(PlayGameState, self).__init__(game)
        self.mood_string = ''
        self.player_controller = None
        self.swarm_controller = None
        self.swarmSpeed = 500
        self.gameOverState = gameOverState
        self.initialise()

    def onEnter(self, previousState):
        self.player_controller.pause(False)

    def initialise(self):
        make = self


    def update(self, gameTime):
        for ctrl in self.controllers:
            ctrl.update(gameTime)

        if (self.player_controller.model.lives == 0):
            self.game.changeState(self.gameOverState)

        if (len(self.swarm_controller.invaders) == 0):
            self.swarmSpeed -= 50
            if (self.swarmSpeed < 100):
                self.swarmSpeed = 100

            self.swarm_controller.reset(48, self.swarmSpeed)
#            levelUpMessage = InterstitialState(invadersGame, 'Congratulations! Level Up!', 2000, self)
#            self.game.changeState(levelUpMessage)

    def draw(self, surface):
        for view in self.renderers:
            view.render(surface)