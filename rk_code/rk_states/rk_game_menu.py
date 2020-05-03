import pygame, os, sys
from pygame.locals import *

from rk_code.rk_settings.rk_states import State
from rk_code.rk_utils.bitmap_font import *

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT_FILE = './rk_data/fasttracker2-style_12x12.png'
pygame.font.init()
FONT = pygame.font.Font(None, 32)


class MenuManager:
    def __init__(self):
        self.selected_index = 0
        self.last_option = None
        self.selected_color = (255, 255, 0)
        self.deselected_color = (255, 255, 255)

    def draw_menu(self, screen):
        '''handle drawing of the menu options'''
        for i, opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom + i * self.spacer)
            if i == self.selected_index:
                rend_img, rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                screen.blit(rend_img, rend_rect)
            else:
                screen.blit(opt[0], opt[1])

    def update_menu(self):
        self.mouse_hover_sound()
        self.change_selected_option()

    def get_event_menu(self, event):
        if event.type == pygame.KEYDOWN:
            '''select new index'''
            if event.key in [pygame.K_UP, pygame.K_w]:
                self.change_selected_option(-1)
            elif event.key in [pygame.K_DOWN, pygame.K_s]:
                self.change_selected_option(1)

            elif event.key == pygame.K_RETURN:
                self.select_option(self.selected_index)
        self.mouse_menu_click(event)

    def mouse_hover_sound(self):
        '''play sound when selected option changes'''
        for i, opt in enumerate(self.rendered["des"]):
            if opt[1].collidepoint(pygame.mouse.get_pos()):
                if self.last_option != opt:
                    self.last_option = opt

    def mouse_menu_click(self, event):
        '''select menu option '''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, opt in enumerate(self.rendered["des"]):
                if opt[1].collidepoint(pygame.mouse.get_pos()):
                    self.selected_index = i
                    self.select_option(i)
                    break

    def pre_render_options(self):
        '''setup render menu options based on selected or deselected'''
        font_deselect = pygame.font.SysFont("arial", 50)
        font_selected = pygame.font.SysFont("arial", 70)

        rendered_msg = {"des": [], "sel": []}
        for option in self.options:
            d_rend = font_deselect.render(option, 1, self.deselected_color)
            d_rect = d_rend.get_rect()
            s_rend = font_selected.render(option, 1, self.selected_color)
            s_rect = s_rend.get_rect()
            rendered_msg["des"].append((d_rend, d_rect))
            rendered_msg["sel"].append((s_rend, s_rect))
        self.rendered = rendered_msg

    def select_option(self, i):
        '''select menu option via keys or mouse'''
        if i == len(self.next_list):
            self.quit = True
        else:
            self.next = self.next_list[i]
            self.done = True
            self.selected_index = 0

    def change_selected_option(self, op=0):
        '''change highlighted menu option'''
        for i, opt in enumerate(self.rendered["des"]):
            if opt[1].collidepoint(pygame.mouse.get_pos()):
                self.selected_index = i
        if op:
            self.selected_index += op
            max_ind = len(self.rendered['des']) - 1
            if self.selected_index < 0:
                self.selected_index = max_ind
            elif self.selected_index > max_ind:
                self.selected_index = 0


class Menu(State, MenuManager):
    def __init__(self):
        State.__init__(self)
        MenuManager.__init__(self)
        self.next = 'game'
        self.options = ['Play', 'Options', 'Quit']
        self.next_list = ['game', 'options']
        self.pre_render_options()
        self.from_bottom = 200
        self.spacer = 75

    def cleanup(self):
        print('cleaning up Main Menu state stuff')

    def startup(self):
        print('starting Main Menu state stuff')

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        self.get_event_menu(event)

    def update(self, screen, dt):
        self.update_menu()
        self.draw(screen)

    def draw(self, screen):
        screen.fill((255, 0, 0))
        self.draw_menu(screen)


class Options(State, MenuManager):
    def __init__(self):
        State.__init__(self)
        MenuManager.__init__(self)
        self.next = 'menu'
        self.options = ['Music', 'Sound', 'Graphics', 'Controls', 'Main Menu']
        self.next_list = ['options', 'options', 'options', 'options', 'menu']
        self.from_bottom = 200
        self.spacer = 75
        self.deselected_color = (150, 150, 150)
        self.selected_color = (0, 0, 0)
        self.pre_render_options()

    def cleanup(self):
        print('cleaning up Options state stuff')

    def startup(self):
        print('starting Options state stuff')

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        self.get_event_menu(event)

    def update(self, screen, dt):
        self.update_menu()
        self.draw(screen)

    def draw(self, screen):
        screen.fill((255, 0, 0))
        self.draw_menu(screen)
