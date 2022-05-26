import pygame
import random

import shapes

from pygame.locals import *


# Steuerung:
# LEFT - nach links bewegen
# RIGHT - nach rechts bewegen
# rotate_left - Figur gegen den Uhrzeigersinn drehen
# rotate_right - Figur im Uhrzeigersinn drehen
# SPACE - Figur sofort zum Boden fallen lassen
# (DOWN - Figur doppelt so schnell fallen lassen)

# Spielfeld:
# 10x20 Blöcke Matrix
# Rahmen
# Raster
# Vorschau nächste Spielfigur
# Scoreboard

# Power-Ups:
# 4 Reihen auf einmal löschen
# -> Geschwindigkeit wird etwas verlangsamt
# ...

# Sonstiges:
# Game Over
# Highscore mit Name in Bestenliste speichern
# Menü um aus verschieden Modi zu wählen?
# -> klassischer Modus
# -> ultimativer Modus (mit Power-Ups, Spielfeld evtl. 20x20 Blöcke?)

# Spielfeld als Matrix
# Figuren als Matrix
# Figuren immer eine Reihe runter laufen lassen, bis sie auf bereits eingefrorene Figur stößt
# Wenn eine Reihe komplett ist, Reihe löschen (und "schwebende" Blöcke runterfallen lassen)


# pygame initialisieren
pygame.init()

# window erstellen
screen_width = 720
screen_height = 480
game_width = 200  # 10x20 Blöcke
game_height = 400  # 20x20 Blöcke
block = 20

window = pygame.display.set_mode((screen_width, screen_height))
window.fill((0, 0, 0))
pygame.display.set_caption('Ultimate Tetris')

# spielfeld
# größe 10 x 20

keep_going = True
clock = pygame.time.Clock()

# Gameloop
while keep_going:

    # fps
    clock.tick(30)

    # Steuerung
    for event in pygame.event.get():

        # Game schließen
        if event.type == pygame.QUIT:
            keep_going = False
            break

        '''# Shape rotieren
        if event.type == KEYDOWN and event.key == K_r:


        # Shape nach rechts bewegen
        if event.type == KEYDOWN and event.key == K_RIGHT:


        # Shape nach links bewegen
        if event.type == KEYDOWN and event.key == K_LEFT:


        # Shape fallen lassen
        if event.type == KEYDOWN and event.key == K_SPACE:'''

