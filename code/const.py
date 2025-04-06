# Lista de Constantes
import pygame

# C

# Constantes de cores
C_ORANGE = (222, 98, 2)
C_WHITE = (255, 255, 255)
C_LIGHT = (241, 199, 168)
C_PURPLE = (100, 21, 119)
COLOR_DB = (34, 4, 88)
C_VIOLET = (192, 145, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,

    'Player': 1,  # nave do jogador
    'PlayerShot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 25,
    'Enemy2': 1,
    'Enemy2Shot': 25,
    'Enemy1_L2': 10,
    'Enemy1_L2Shot': 30,
    'Enemy2_L2': 10,
    'Enemy2_L2Shot': 30
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 2*0.4,
    'Level1Bg3': 2,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 2 * 0.4,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level2Bg5': 5,

    'Player': 3,
    'PlayerShot': 2,
    'Enemy1': 1,
    'Enemy1Shot': 4,
    'Enemy2': 1,
    'Enemy2Shot': 3,
    'Enemy1_L2': 2,
    'Enemy1_L2Shot': 3,
    'Enemy2_L2': 1,
    'Enemy2_L2Shot': 3

}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,

    'Player': 300,
    'PlayerShot': 1,
    'Enemy1': 60,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
    'Enemy1_L2': 60,
    'Enemy1_L2Shot': 1,
    'Enemy2_L2': 60,
    'Enemy2_L2Shot': 1
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,

    'Player': 0,
    'PlayerShot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
    'Enemy1_L2': 100,
    'Enemy1_L2Shot': 0,
    'Enemy2_L2': 125,
    'Enemy2_L2Shot': 0

}

ENTITY_SHOT_DELAY = {
    'Player': 25,
    'Enemy1': 100,
    'Enemy2': 90,
    'Enemy1_L2': 90,
    'Enemy2_L2': 90,


}

# M

# Para fazer o print do menu
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')


# T
TIMEOUT_LEVEL = 20000  # 20 segundos
TIMEOUT_STEP = 100  # 100 ms


# W

# essa constante irá atualizar os valores do tamanho da imagem do background
WIN_WIDTH = 560
WIN_HEIGHT = 330


# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 30),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290)
}
