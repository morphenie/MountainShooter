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

            if menu_return in [MENU_OPTION[0]]:  # para entrar no jogo efetivamente
                player_score = [0]
                level = Level(self.window, 'Level1', menu_return, player_score)  # parâmetro para escolher o level
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)  # lvl2
                    level_return = level.run(player_score)


            elif menu_return == MENU_OPTION[2]:
                pygame.quit()  # Close window
                quit()  # End Pygame
            else:  # score
                pass



##