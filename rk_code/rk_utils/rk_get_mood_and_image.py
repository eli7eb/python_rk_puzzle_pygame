import pygame, os, sys

import rk_code.rk_data

from pygame.locals import *

from rk_code.rk_states import *
from rk_code.rk_settings.rk_states_manager import *
from rk_code.rk_utils.bitmap_font import *

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT_FILE = './rk_data/fasttracker2-style_12x12.png'
pygame.font.init()
FONT = pygame.font.Font(None, 32)


class InputBox:


    def __init__(self, x, y, w, h, am_i_active, text=''):
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

class GetMoodInput(GameState):

    def __init__(self, game):
        super(GetMoodInput, self).__init__(game)
        self.playGameState = None
        self.font = BitmapFont(FONT_FILE, 12, 12)
        self.index = 0
        self.inputTick = 0

    def setPlayState(self, state):
        self.playGameState = state

    def draw(self, surface):
        clock = pygame.time.Clock()
        input_box1 = InputBox(100, 100, 140, 32, False, 'Your mood : ')
        input_box2 = InputBox(100, 300, 140, 32, True)
        input_boxes = [input_box1, input_box2]
#        self.font.centre(surface, "Your mood is ", 48)
        done = False


        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYUP and box.search_done == True:
                    search_string = box.get_search_string()
                    print(search_string)
                    done = True
                for box in input_boxes:
                    box.handle_event(event)

            for box in input_boxes:
                box.update()

            surface.fill((30, 30, 30))
            for box in input_boxes:
                box.draw(surface)

            pygame.display.flip()
            clock.tick(30)

        count = 0
        y = surface.get_rect().height - len(self.menuItems) * 160
        for item in self.menuItems:
            itemText = "  "

            if (count == self.index):
                itemText = "> "

            itemText += item
            self.font.draw(surface, itemText, 25, y)
            y += 24
            count += 1

