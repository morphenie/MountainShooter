#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_LIGHT, COLOR_PP


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')  # para definir a imagem de background do menu
        self.rect = self.surf.get_rect(left=0, top=0)  # cria-se um retângulo

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')  # para carregar a música do menu
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer_music.play(-1)  # para tocar a música com um parâmetro para loop

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # para a imagem aparecer no retângulo
            self.menu_text(40, "Spooky", (50, 50, 50), ((WIN_WIDTH / 2) - 2, 30 + 2))  # Sombra
            self.menu_text(40, "Paws  ", (50, 50, 50), ((WIN_WIDTH / 2) - 2, 60 + 2))  # Sombra

            self.menu_text(40, "Spooky", COLOR_PP, ((WIN_WIDTH / 2), 30))  # Escrever o texto, não pode vir antes da imagem para ele não ficar por baixo dela
            self.menu_text(40, "Paws  ", COLOR_PP, ((WIN_WIDTH / 2), 60))  # Escrever o texto, não pode vir antes da imagem para ele não ficar por baixo dela


            for i in range(len(MENU_OPTION)):
                if i == menu_option:  # loop para mudança de cor ao selecionar
                    self.menu_text(15, MENU_OPTION[i], COLOR_LIGHT, ((WIN_WIDTH / 2), 110 + 18 * i))
                else:
                    self.menu_text(15, MENU_OPTION[i], COLOR_ORANGE, ((WIN_WIDTH / 2), 110+18*i))
            pygame.display.flip()  # para atualizar na tela e aparecer a imagem

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # se o evento for do tipo "fechar janela"
                    pygame.quit()  # Close window
                    quit()  # End Pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        # menu_option += 1 (se deixasse essa variável, ia para baixo infinitamente no menu, sumir)
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  #ENTER
                        return MENU_OPTION[menu_option]




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):  # texto do menu
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


    ##
