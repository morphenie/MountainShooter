#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0),  level='Level1'):
        match entity_name:
            case 'Level1Bg':   # bg da fase 1
                list_bg = []
                for i in range(6):  # já que são 6 imagens
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level2Bg':   # bg da fase 2
                list_bg = []
                for i in range(6):  # já que são 6 imagens
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player':
                return Player('Player', (10, WIN_HEIGHT / 3))
            case 'Enemy1':
                enemy_name = 'Enemy1_L2' if level == 'Level2' else 'Enemy1'
                return Enemy(enemy_name, (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                enemy_name = 'Enemy2_L2' if level == 'Level2' else 'Enemy2'
                return Enemy(enemy_name, (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
