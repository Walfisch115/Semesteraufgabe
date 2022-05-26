import pygame
import random

from pygame.locals import *


# Spielfiguren
shapeColors = {
    'I': (0, 255, 255),  # LIGHT_BLUE
    'J': (0, 0, 255),    # BLUE
    'L': (255, 128, 0),  # ORANGE
    'O': (255, 255, 0),  # YELLOW
    'S': (0, 255, 0),    # GREEN
    'T': (255, 0, 255),  # PURPLE
    'Z': (255, 0, 0)     # RED
}


# Gibt Matrix der Spielfigur zurück
# Parameter: Name und Rotation (0 Grad, 90 Grad, 180 Grad, 270 Grad)
def shape_matrix(name, rotation):

    if name == 'I':

        if rotation == 0 or rotation == 180:

            shape_i = [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]

            return shape_i

        elif rotation == 90 or rotation == 270:

            shape_i = [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0]
            ]

            return shape_i

    elif name == 'J':

        if rotation == 0:

            shape_j = [
                [1, 0, 0],
                [1, 1, 1],
                [0, 0, 0]
            ]

            return shape_j

        elif rotation == 90:

            shape_j = [
                [0, 1, 1],
                [0, 1, 0],
                [0, 1, 0]
            ]

            return shape_j

        elif rotation == 180:

            shape_j = [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 1]
            ]

            return shape_j

        elif rotation == 270:

            shape_j = [
                [0, 1, 0],
                [0, 1, 0],
                [1, 1, 0]
            ]

            return shape_j

    elif name == 'L':

        if rotation == 0:

            shape_l = [
                [0, 0, 1],
                [1, 1, 1],
                [0, 0, 0]
            ]

            return shape_l

        elif rotation == 90:

            shape_l = [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 1]
            ]

            return shape_l

        elif rotation == 180:

            shape_l = [
                [0, 0, 0],
                [1, 1, 1],
                [1, 0, 0]
            ]

            return shape_l

        elif rotation == 270:

            shape_l = [
                [1, 1, 0],
                [0, 1, 0],
                [0, 1, 0]
            ]

            return shape_l

    elif name == 'O':

        if rotation == 0 or rotation == 90 or rotation == 180 or rotation == 270:

            shape_o = [
                [1, 1],
                [1, 1]
            ]

            return shape_o

    elif name == 'S':

        if rotation == 0 or rotation == 180:

            shape_s = [
                [0, 1, 1],
                [1, 1, 0],
                [0, 0, 0]
            ]

            return shape_s

        elif rotation == 90 or rotation == 270:

            shape_s = [
                [0, 1, 0],
                [0, 1, 1],
                [0, 0, 1]
            ]

            return shape_s

    elif name == 'T':

        if rotation == 0:

            shape_t = [
                [0, 1, 0],
                [1, 1, 1],
                [0, 0, 0]
            ]

            return shape_t

        elif rotation == 90:

            shape_t = [
                [0, 1, 0],
                [0, 1, 1],
                [0, 1, 0]
            ]

            return shape_t

        elif rotation == 180:

            shape_t = [
                [0, 0, 0],
                [1, 1, 1],
                [0, 1, 0]
            ]

            return shape_t

        elif rotation == 270:

            shape_t = [
                [0, 1, 0],
                [1, 1, 0],
                [0, 1, 0]
            ]

            return shape_t

    elif name == 'Z':

        if rotation == 0 or rotation == 180:

            shape_z = [
                [1, 1, 0],
                [0, 1, 1],
                [0, 0, 0]
            ]

            return shape_z

        elif rotation == 90 or rotation == 270:

            shape_z = [
                [0, 0, 1],
                [0, 1, 1],
                [0, 1, 0]
            ]

            return shape_z


'''function* randomGenerator() {
  let bag = [];

  while (true) {
    if (bag.length === 0) {
      bag = ["I", "J", "L", "O", "S", "T", "Z"];
      bag = shuffle(bag);
    }
    yield bag.pop();
  }
}'''


# Packt alle 7 Spielfiguren in einen Beutel und zieht eine nach der anderen, bis der Beutel leer ist.
# Beginnt dann wieder von vorne.
def random_shape():

    beutel = []
    keep_going = True

    while keep_going:

        if len(beutel) == 0:
            beutel = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']

        shape = beutel[random.randint(0, 6)]
        beutel.remove(shape)

        next_shape = beutel[random.randint(0, 6)]
        beutel.remove(next_shape)

        return shape, next_shape


class Shape:

    def __init__(self, x_coordinate, y_coordinate, name):
        self.x = x_coordinate
        self.y = y_coordinate
        self.shape = name
        self.color = name
        self.rotation = 0  # default

    # Gibt Matrix der Spielfigur zurück
    def image_of_shape(self):
        return shape_matrix(self.shape, self.rotation)

    # im Uhrzeigersinn drehen
    def rotate_right(self):
        if self.rotation == 0 or self.rotation == 90 or self.rotation == 180:
            self.rotation += 90

        elif self.rotation == 270:
            self.rotation = 0

    # gegen den Uhrzeigersinn drehen
    def rotate_left(self):
        if self.rotation == 270 or self.rotation == 180 or self.rotation == 90:
            self.rotation -= 90

        elif self.rotation == 0:
            self.rotation = 270
