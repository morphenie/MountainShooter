
# Fazer um jogo em phyton, assuntos: bibliotecas, POO, banco de dados, design pattern, Git, etc.
# ctrl alt l = organiza o código remove os erros;

import pygame

print('Setup Start')
pygame.init()  # é necessário para iniciar o pacote do pygame

print('Setup End')

print('Loop Start')
window = pygame.display.set_mode(size=(600, 480))  # criação de janela do jogo
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close window
            quit()  # End Pygame
