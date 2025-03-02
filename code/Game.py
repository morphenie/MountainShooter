#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):  #construtor da class Game
        pygame.init()  # é necessário para iniciar o pacote do pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # criação de janela do jogo com a resolução da imagem

    def run(self):  #método run


        while True:
            menu = Menu(self.window)
            menu.run()
            pass


##