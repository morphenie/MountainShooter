#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Menu import Menu


class Game:
    def __init__(self):  #construtor da class Game
        pygame.init()  # é necessário para iniciar o pacote do pygame
        self.window = pygame.display.set_mode(size=(600, 480))  # criação de janela do jogo

    def run(self):  #método run

        # ---------- aqui foi copiado do main ---------
#        print('Setup Start')

#        print('Setup End')

#        print('Loop Start')
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


            # Check for all events
            #for event in pygame.event.get():
            #    if event.type == pygame.QUIT:  # o evento do tipo "fechar janela"
            #        pygame.quit()  # Close window
            #        quit()  # End Pygame
