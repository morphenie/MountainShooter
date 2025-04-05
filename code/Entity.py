#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):  # nome é para inicializar o objeto entity

    def __init__(self, name: str, position: tuple):  # e posição que o objeto deve aparecer na tela
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()  # caminho genérico para pegar as imagens
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # tbm genérico pq o asset pode aparecer em qqr lugar na tela
        self.speed = 0

    @abstractmethod  # decorator (?)
    def move(self, ):
        pass

##