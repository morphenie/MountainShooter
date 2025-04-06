#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Enemy import Enemy
from code.EntityMediator import EntityMediator
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.const import C_WHITE, WIN_HEIGHT, EVENT_ENEMY, C_VIOLET


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode  # modo de jogo, 1p 2p etc
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 20000  # 20 segundos
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):
        pygame.mixer.music.load(f'./asset/{self.name}.mp3')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

                # hubs
                if ent.name == 'Player':
                    self.level_text(14, f'Player Health: {ent.health} |  Score: {ent.score}', C_VIOLET, (10, 25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))



            # printed text
            self.level_text(12, f'{self.name} - Timeout: {self.timeout / 1000: .1f}s', C_WHITE, (10, 5))
            self.level_text(12, f'FPS: {clock.get_fps() : .0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(12, f'Entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name= "Lucida Sans Typewriter", size= text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

##