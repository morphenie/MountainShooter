#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Level import Level
from code.Menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):  # construtor da class Game
        pygame.init()  # é necessário para iniciar o pacote do pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # criação de janela do jogo com a resolução da imagem

    def run(self):  # método run
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:  # para entrar no jogo efetivamente
                level = Level(self.window, 'Level1', menu_return)  # parâmetro para escolher o level
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close window
                quit()  # End Pygame
            else:  # score
                pass



##