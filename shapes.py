import pygame
import random

from pygame.locals import *

# spielfiguren
# I, J, L, O, S, T und Z

# bausteine rendern

# name der shapes ist hier in der schleife noch falsch, ich hatte die nochmal umbenannt
'''for h in range(len(shapes.shape_i)):
    for w in range(len(shapes.shape_i[0])):
        if shapes.shape_i[h][w] != 0:
            pygame.draw.rect(window, (255, 0, 255), (w * 10, h * 10, 10, 10))'''


def shape(name, rotation=0):

    if name == 'i':

        if rotation == 0 or rotation == 180:

            shape_i = [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]

        elif rotation == 90 or rotation == 270:

            shape_i = [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0]
            ]

    elif name == 'j':

        if rotation == 0:

            shape_j = [
                [1, 0, 0],
                [1, 1, 1],
                [0, 0, 0]
            ]

        elif rotation == 90:

            shape_j = [
                [0, 1, 1],
                [0, 1, 0],
                [0, 1, 0]
            ]

        elif rotation == 180:

            shape_j = [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 1]
            ]

        elif rotation == 270:

            shape_j = [
                [0, 1, 0],
                [0, 1, 0],
                [1, 1, 0]
            ]

    elif name == 'l':

        if rotation == 0:

            shape_l = [
                [0, 0, 1],
                [1, 1, 1],
                [0, 0, 0]
            ]

        elif rotation == 90:

            shape_l = [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 1]
            ]

        elif rotation == 180:

            shape_l = [
                [0, 0, 0],
                [1, 1, 1],
                [1, 0, 0]
            ]

        elif rotation == 270:

            shape_l = [
                [1, 1, 0],
                [0, 1, 0],
                [0, 1, 0]
            ]

    elif name == 'o':

        if rotation == 0 or rotation == 90 or rotation == 180 or rotation == 270:

            shape_o = [
                [1, 1],
                [1, 1]
            ]

    elif name == 's':

        if rotation == 0 or rotation == 180:

            shape_s = [
                [0, 1, 1],
                [1, 1, 0],
                [0, 0, 0]
            ]

        elif rotation == 90 or rotation == 270:

            shape_s = [
                [0, 1, 0],
                [0, 1, 1],
                [0, 0, 1]
            ]

    elif name == 't':

        if rotation == 0:

            shape_t = [
                [0, 1, 0],
                [1, 1, 1],
                [0, 0, 0]
            ]

        elif rotation == 90:

            shape_t = [
                [0, 1, 0],
                [0, 1, 1],
                [0, 1, 0]
            ]

        elif rotation == 180:

            shape_t = [
                [0, 0, 0],
                [1, 1, 1],
                [0, 1, 0]
            ]

        elif rotation == 270:

            shape_t = [
                [0, 1, 0],
                [1, 1, 0],
                [0, 1, 0]
            ]

    elif name == 'z':

        if rotation == 0 or rotation == 180:

            shape_z = [
                [1, 1, 0],
                [0, 1, 1],
                [0, 0, 0]
            ]

        elif rotation == 90 or rotation == 270:

            shape_z = [
                [0, 0, 1],
                [0, 1, 1],
                [0, 1, 0]
            ]
