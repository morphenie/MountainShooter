# Lista de Constantes
import pygame

# C

# Constantes de cores
COLOR_ORANGE = (222, 98, 2)
COLOR_WHITE = (255, 255, 255)
COLOR_LIGHT = (241, 199, 168)
COLOR_PP = (100, 21, 119)
COLOR_DB = (34, 4, 88)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 2*0.4,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Player': 3,
    'PlayerShot': 2,
    'Enemy1': 1,
    'Enemy1Shot': 4,
    'Enemy2': 1,
    'Enemy2Shot': 3

}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player': 300,
    'PlayerShot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player': 20,
    'Enemy1': 100,
    'Enemy2': 80

}

# M

# Para fazer o print do menu
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# W

# essa constante irá atualizar os valores do tamanho da imagem do background
WIN_WIDTH = 560
WIN_HEIGHT = 330

