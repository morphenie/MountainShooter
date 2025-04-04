#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':   # bg da fase 1
                list_bg = []
                for i in range(6):  # já que são 6 imagens
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))

                return list_bg


##