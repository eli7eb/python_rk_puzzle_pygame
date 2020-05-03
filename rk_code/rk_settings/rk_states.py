import pygame,  sys
from rk_code.rk_settings.rk_control import Control

class State(Control):
    def __init__(self):
        self.title = "RK Puzzle"
        self.width = 600
        self.height = 800
        self.message = ""
        self.location = (20, 150)
        self.font = 40
        self.color = "White"
        self.nextState = None
        self.done = False
        self.next = None
        self.quit = False
        self.previousState = None
        self.btn = ""

    def onEnter(self, previousState, params):
        pass

    """
    Called by the game when leaving the state.
    """

    def onExit(self):
        pass

    """
    Called by the game allowing the state to update itself. The game time (in milliseconds) since
    the last call is passed.
    """

    def update(self, gameTime):
        pass

    """
    Called by the game allowing the state to draw itself. The surface that is passed is the
    current drawing surface.
    """

    def draw(self, surface):
        pass

    def start(self):
        pygame.init()
        self.fpsClock = pygame.time.Clock()

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.get_surface()

        self.main_loop()

    def main_loop(self):
        while True:
            self.screen.fill(pygame.Color(self.color))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
#                elif event.type == pygame.MOUSEBUTTONDOWN:
#                    self.transition()

            self.draw()
            pygame.display.update()
            self.fpsClock.tick(30)

    def draw_text(self, text, y_position=36):
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render(text, 1, (10, 10, 10))
            textpos = text.get_rect()
            textpos.centerx = self.screen.get_rect().centerx
            textpos.centery = y_position
            self.screen.blit(text, textpos)


    def draw(self):
        self.draw_text(self.message)
        self.draw_text(self.btn, 72)

    # transition is a base-class method
    def transition(self):
        # derived classes provide their own "nextState". Default is None.
        if self.nextState != None:
            switch_to = self.nextState()
            switch_to.start()