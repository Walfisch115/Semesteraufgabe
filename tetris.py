import pygame
import random

import shapes

from pygame.locals import *

# pygame initialisieren
pygame.init()

# window erstellen
width = 720
height = 480
window = pygame.display.set_mode((width, height))
window.fill((0, 0, 0))
pygame.display.set_caption('Ultimate Tetris')

# farben
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
YELLOW = pygame.Color(255, 255, 0)
ORANGE = pygame.Color(255, 128, 0)
LIGHT_BLUE = pygame.Color(0, 255, 255)
PURPLE = pygame.Color(255, 0, 255)

# spielfeld
# größe 10 x 20

keepGoing = True
paint = False
clock = pygame.time.Clock()

# gameloop
while keepGoing:

    # fps
    clock.tick(30)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            keepGoing = False
            break

