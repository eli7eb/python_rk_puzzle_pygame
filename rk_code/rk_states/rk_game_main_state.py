import pygame
from rk_code.rk_settings.rk_states import State
from rk_code.rk_states.rk_game_end import EndState
# begin game ask player for mood to search
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT_FILE = './rk_data/fasttracker2-style_12x12.png'

class InputBox:
    def __init__(self, x, y, w, h, am_i_active, text=''):
        pygame.font.init()
        FONT = pygame.font.Font(None, 32)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.am_i_active = am_i_active
        self.active = False
        self.search_done = False
        self.look_for_str = ''

    def handle_event(self, event):
        # first field is for display only
        if (self.am_i_active == False):
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.look_for_str = self.text
                    self.search_done = True
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                FONT = pygame.font.Font(None, 32)
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def get_search_done(self):
        return self.search_done

    def get_search_string(self):
        return self.look_for_str

class GameState(State):
    def __init__(self):
        State.__init__(self)
        self.next = 'menu'

        State.__init__(self)
        self.message = "Enter mood for puzzle"
        self.btn = "Click to Play"
        clock = pygame.time.Clock()
        input_box1 = InputBox(100, 200, 140, 32, False, 'Enter your mood')
        input_box2 = InputBox(100, 300, 140, 32, True)

        self.input_boxes = [input_box1, input_box2]
        done = False

    def cleanup(self):
        print('cleaning up Game state stuff')

    def startup(self):
        print('starting Game state stuff')


    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            print('Game State keydown')
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            self.done = True

    def update(self, screen, dt):
        self.draw(screen)

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                for box in self.input_boxes:
                    box.handle_event(event)
                    if box.search_done == True:
                        mood_string = box.get_search_string()
                        self.game.mood_string = mood_string
                        done = True

            for box in self.input_boxes:
                box.update()

            self.game.mainwindow.fill((30, 30, 30))
            for box in self.input_boxes:
                box.draw(self.game.mainwindow)

            pygame.display.flip()
            self.clock.tick(30)

        self.game.changeState(self.playGameState, [self.game.mood_string])

    def draw(self, screen):
        screen.fill((0, 0, 255))