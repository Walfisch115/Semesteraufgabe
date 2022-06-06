# import and initialization
import pygame
import random

from pygame.locals import *

# Zum erstellen der Highscore Datenbank
import tetris_score_db

pygame.init()

# Display configuration
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris')

# Entities
screen.fill((0, 0, 0))

# Klassen können später ausgelagert werden, find's für den Anfang nur einfacher so zu arbeiten


class Shape:

    # Tetrominoes aka Spielsteine
    O = [[[0, 1, 1],
          [0, 1, 1]],
         [[0, 1, 1],
          [0, 1, 1]]]

    S = [[[0, 1, 1],
          [1, 1, 0]],
         [[0, 1, 0],
          [0, 1, 1],
          [0, 0, 1]],
         [[0, 0, 0],
          [0, 1, 1],
          [1, 1, 0]],
         [[1, 0],
          [1, 1],
          [0, 1]]]

    Z = [[[1, 1, 0],
          [0, 1, 1]],
         [[0, 0, 1],
          [0, 1, 1],
          [0, 1, 0]],
         [[0, 0, 0],
          [1, 1, 0],
          [0, 1, 1]],
         [[0, 1],
          [1, 1],
          [1, 0]]]

    I = [[[0, 0, 0, 0],
          [1, 1, 1, 1]],
         [[0, 0, 1],
          [0, 0, 1],
          [0, 0, 1],
          [0, 0, 1]],
         [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 1]],
         [[0, 1],
          [0, 1],
          [0, 1],
          [0, 1]]]

    J = [[[1, 0, 0],
          [1, 1, 1]],
         [[0, 1, 1],
          [0, 1, 0],
          [0, 1, 0]],
         [[0, 0, 0],
          [1, 1, 1],
          [0, 0, 1]],
         [[0, 1],
          [0, 1],
          [1, 1]]]

    L = [[[0, 0, 1],
          [1, 1, 1]],
         [[0, 1, 0],
          [0, 1, 0],
          [0, 1, 1]],
         [[0, 0, 0],
          [1, 1, 1],
          [1, 0, 0]],
         [[1, 1],
          [0, 1],
          [0, 1]]]

    T = [[[0, 1, 0],
          [1, 1, 1]],
         [[0, 1, 0],
          [0, 1, 1],
          [0, 1, 0]],
         [[0, 0, 0],
          [1, 1, 1],
          [0, 1, 0]],
         [[0, 1],
          [1, 1],
          [0, 1]]]

    # Zugriff auf alle Formen über diese Liste
    shapes = [O, S, Z, I, J, L, T]

    x = 0
    y = 0

    def __init__(self, x, y):
        global bag, next, next_figure
        self.x = x
        self.y = y
        self.rotation = 0

        # Initialisiert ein neues gegenwärtiges und nächstes Stück, falls es noch kein nächstes gibt
        # (wird also eigentlich nur beim Ersten mal aufgerufen)
        if next == -1:
            self.type = (random.randint(0, len(bag)-1))
            self.figure = bag[self.type]
            bag.pop(self.type)

            next = (random.randint(0, len(bag)-1))
            next_figure = bag[next]

        # Falls schon ein nächstes Stück initialisiert ist wird das übernommen
        # und ein neues "nächstes" Stück initialisiert
        else:
            self.type = next
            self.figure = next_figure
            bag.pop(next)

            if len(bag) == 0:
                bag = ["O", "S", "Z", "I", "J", "L", "T"]

            if len(bag) == 1:
                next = 0
            else:
                next = (random.randint(0, len(bag)-1))
            next_figure = bag[next]

        # Zuweisung der Spielfigur
        if self.figure == "O":
            self.piece = 0
        elif self.figure == "S":
            self.piece = 1
        elif self.figure == "Z":
            self.piece = 2
        elif self.figure == "I":
            self.piece = 3
        elif self.figure == "J":
            self.piece = 4
        elif self.figure == "L":
            self.piece = 5
        elif self.figure == "T":
            self.piece = 6

    # Rotationen
    def rotate_right(self):
        self.rotation = (self.rotation+1) % len(self.shapes[self.piece])

    def rotate_left(self):
        self.rotation = (self.rotation-1) % len(self.shapes[self.piece])

    # Gibt gegenwärtige Figur zurück
    def get_image(self):
        return self.shapes[self.piece][self.rotation]

    # Gibt die zugewiesene Farbe der gegenwärtigen Figur zurück
    def get_color(self):
        return self.figure


class Game:
    global next_figure
    height = 0
    width = 0
    tile = 20  # Feldgröße

    # Obere linke Ecke des Spielfeldes
    x_base = screen_width//2-5*tile
    y_base = screen_height//2-10*tile

    # Obere linke Ecke des Next Kasten
    x_next_base = screen_width//2+7*tile
    y_next_base = screen_height//2-1*tile

    # Matrix
    matrix = []
    next_matrix = []

    # Score und Spielzustand
    play = True
    line_counter = 0
    score = 0
    level = 0

    # Initialisierung der Matrix (auf 0) als Liste aus Listen
    # Eine Liste entspricht immer einer Zeile
    def __init__(self, height, width, tile):
        self.height = height
        self.width = width
        self.tile = tile * self.tile

        # Spawnzone zwei Felder über dem Spielfeld (muss im fertigen Spiel nicht mit angezeigt werden)
        for i in range(2):
            line = []
            for j in range(self.width):
                line.append(0)
            self.matrix.append(line)

        # Spielfeld
        for i in range(self.height):
            line = []
            for j in range(self.width):
                line.append(0)
            self.matrix.append(line)

        # nächsten Stein anzeigen
        for i in range(2):
            line = []
            for j in range(4):
                line.append(0)
            self.next_matrix.append(line)

    # Fügt Spielfigur in die Matrix ein (als 1)
    def create_shape(self):
        global old_color
        if not self.end_game() and self.play:
            if old_color != 0:
                old_color = self.color
            self.shape = Shape(3, 0)
            self.piece = self.shape.get_image()
            self.color = self.shape.get_color()
            if old_color == 0:
                old_color = self.color
            self.set_1(0, 0)
            self.set_new_1()
        else:
            self.set_highscore()
            self.play = False

    # Update für Rotationen
    def update_shape(self, rot, dir):
        self.set_0()
        direction = dir
        start_rot = rot
        self.piece = self.shape.get_image()
        col_shape = self.collision_shape(self.shape.x, self.shape.y)
        if col_shape:
            if direction == 'left':
                old_rot = game.shape.rotation
                self.shape.rotate_right()
                game.update_shape(old_rot, 'right')
            elif direction == 'right':
                old_rot = game.shape.rotation
                game.shape.rotate_left()
                game.update_shape(old_rot, 'left')
        if self.collision_x(self.shape.x) and self.shape.x <= 0:
            if self.shape.x == -2:
                self.set_1(2, 0)
                return
            elif self.shape.x == -1:
                self.set_1(1, 0)
                return
            elif self.shape.piece == 0:
                self.set_1(0, 0)
                return
            elif start_rot == 1:
                self.set_1(1, 0)
                return
        elif self.collision_x(self.shape.x):
            if self.collision_x(self.shape.x-1):
                self.set_1(-2, 0)
                return
            elif self.shape.piece == 3 and start_rot == 1:
                self.set_1(-1, 0)
                return
            elif start_rot == 3:
                self.set_1(-1, 0)
                return
        elif self.collision_y(self.shape.y) and self.shape.piece == 3:
            if self.shape.y == 20 and start_rot == 0:
                self.set_1(0, -2)
                return
            if self.shape.y == 19 and start_rot == 0:
                self.set_1(0, -1)
                return
            elif self.shape.y == 20 and start_rot == 2:
                self.set_1(0, -1)
                return
        self.set_1(0, 0)

    # Steuerung
    def down(self):
        self.set_0()
        self.set_1(0, 1)

    def left(self):
        self.set_0()
        self.set_1(-1, 0)

    def right(self):
        self.set_0()
        self.set_1(1, 0)

    def space(self):
        x = self.shape.x
        y = self.shape.y
        col_y = self.collision_y(y+1)
        col_shape = self.collision_shape(x, y+1)
        while not col_shape and not col_y:
            self.down()
            x = self.shape.x
            y = self.shape.y
            col_y = self.collision_y(y+1)
            if col_y:
                break
            col_shape = self.collision_shape(x, y+1)
        self.down()
        self.draw()

    # Festsetzen der Steine
    def freeze(self):
        run_x = 0
        run_y = 0
        matrix_x = self.shape.x
        matrix_y = self.shape.y
        for i in range(len(self.piece)):
            run_x = 0
            matrix_x = self.shape.x
            for j in range(len(self.piece[run_y])):
                if self.piece[run_y][run_x] == 1:
                    self.matrix[matrix_y][matrix_x] = 2
                run_x += 1
                matrix_x += 1
            run_y += 1
            matrix_y += 1
        self.break_line()
        self.create_shape()

    # volle Line kaputtmachen
    def break_line(self):
        matrix_x = 0
        matrix_y = 0
        lines = 0
        base_points = 0
        for i in range(len(self.matrix)):
            matrix_x = 0
            if self.matrix[matrix_y].count(2) == len(self.matrix[matrix_y]):
                lines += 1
                self.matrix.pop(matrix_y)
                add = []
                for j in range(self.width):
                    add.append(0)
                self.matrix.insert(0, add)
            matrix_y += 1
        if lines == 1:
            base_points = 40
        elif lines == 2:
            base_points = 100
        elif lines == 3:
            base_points = 300
        elif lines >= 4:
            base_points = 1200
        if lines >= 1:
            self.score += base_points * (lines+1)
        self.line_counter += lines
        self.level = self.line_counter // 10

    # Kollision der x Werte testen
    def collision_x(self, x):
        collision_x = x
        border_x = len(self.matrix[0])
        if len(self.piece[0]) + collision_x > border_x:
            return True
        elif collision_x < 0:
            if collision_x == -1:
                for i in range(len(self.piece)):
                    if self.piece[i][0] == 1:
                        return True
            elif collision_x == -2:
                for i in range(len(self.piece)):
                    if self.piece[i][1] == 1:
                        return True
            else:
                return True
        return False

    # Kollision der y Werte Testen
    def collision_y(self, y):
        collision_y = y
        border_y = len(self.matrix)
        if len(self.piece) + collision_y > border_y:
            return True
        return False

    # Kollision mit anderen Figuren testen
    def collision_shape(self, x, y):
        collision_x = x
        collision_y = y
        if collision_y < len(self.matrix)-1:
            run_x = 0
            run_y = 0
            for i in range(len(self.piece)):
                run_x = 0
                collision_x = x
                for j in range(len(self.piece[run_y])):
                    if self.piece[run_y][run_x] == 1 and self.matrix[collision_y][collision_x] == 2:
                        return True
                    run_x += 1
                    collision_x += 1
                run_y += 1
                collision_y += 1
        return False

    # Figur auf 0 setzen
    def set_0(self):
        run_x = 0
        run_y = 0
        matrix_x = self.shape.x
        matrix_y = self.shape.y
        for i in range(len(self.piece)):
            run_x = 0
            matrix_x = self.shape.x
            for j in range(len(self.piece[run_y])):
                if self.matrix[matrix_y][matrix_x] == 1:
                    self.matrix[matrix_y][matrix_x] = 0
                run_x += 1
                matrix_x += 1
            run_y += 1
            matrix_y += 1

    # Figur initialisieren (auf 1 setzen)
    def set_1(self, offset_x, offset_y):
        x = offset_x
        y = offset_y
        run_x = 0
        run_y = 0
        matrix_x = self.shape.x + x
        matrix_y = self.shape.y + y
        col_x = self.collision_x(matrix_x)
        col_y = self.collision_y(matrix_y)
        if col_x:
            self.set_1(0, 0)
        elif col_y:
            self.set_1(0, 0)
            self.freeze()
            return False
        else:
            col_shape = self.collision_shape(matrix_x, matrix_y)
            if col_shape:
                self.set_1(0, 0)
                self.freeze()
                return False
            else:
                for i in range(len(self.piece)):
                    run_x = 0
                    matrix_x = self.shape.x + x
                    for j in range(len(self.piece[run_y])):
                        if self.piece[run_y][run_x] == 1 and self.matrix[matrix_y][matrix_x] != 2:
                            self.matrix[matrix_y][matrix_x] = 1
                        run_x += 1
                        matrix_x += 1
                    run_y += 1
                    matrix_y += 1
                self.shape.x += x
                self.shape.y += y
        return True

    # nächster Stein Figur auf 0 setzen
    def set_new_0(self):
        matrix_x = 0
        matrix_y = 0
        for i in range(len(self.next_matrix)):
            matrix_x = 0
            for j in range(len(self.next_matrix[matrix_y])):
                if self.next_matrix[matrix_y][matrix_x] == 1:
                    self.next_matrix[matrix_y][matrix_x] = 0
                matrix_x += 1
            matrix_y += 1

    # Nächster Stein Figur anzeigen/ initialisieren (auf 1 setzen)
    def set_new_1(self):
        self.set_new_0()
        run_x = 0
        run_y = 0
        matrix_x = 0
        matrix_y = 0

        if next_figure == "O":
            next_piece = 0
        elif next_figure == "S":
            next_piece = 1
        elif next_figure == "Z":
            next_piece = 2
        elif next_figure == "I":
            next_piece = 3
        elif next_figure == "J":
            next_piece = 4
        elif next_figure == "L":
            next_piece = 5
        elif next_figure == "T":
            next_piece = 6

        next_shape = self.shape.shapes[next_piece][0]

        for i in range(len(next_shape)):
            run_x = 0
            matrix_x = 0
            for j in range(len(next_shape[run_y])):
                if next_shape[run_y][run_x] == 1:
                    self.next_matrix[matrix_y][matrix_x] = 1
                matrix_x += 1
                run_x += 1
            matrix_y += 1
            run_y += 1

    # Zeichnet Spielfeld und Spielfiguren und nächsten Stein
    def draw(self):
        x = self.x_base
        y = self.y_base
        matrix_x = 0
        matrix_y = 2

        # Spielfeld
        for i in range(len(self.matrix)-2):
            matrix_x = 0
            x = self.x_base
            for j in range(len(self.matrix[matrix_y])):
                if self.matrix[matrix_y][matrix_x] == 0:
                    game = pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, self.tile, self.tile))
                elif self.matrix[matrix_y][matrix_x] == 1:
                    tetromino = pygame.draw.rect(screen, colors[self.color], pygame.Rect(x, y, self.tile, self.tile))
                elif self.matrix[matrix_y][matrix_x] == 2:
                    settled = pygame.draw.rect(screen, colors[old_color], pygame.Rect(x, y, self.tile, self.tile))
                game_border = pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, self.tile, self.tile), 1)
                matrix_x += 1
                x += self.tile
            matrix_y += 1
            y += self.tile

        # nächstes Stück
        x = self.x_next_base
        y = self.y_next_base
        matrix_x = 0
        matrix_y = 0
        for i in range(len(self.next_matrix)):
            x = self.x_next_base
            matrix_x = 0
            for j in range(len(self.next_matrix[matrix_y])):
                if self.next_matrix[matrix_y][matrix_x] == 0:
                    next_base = pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, self.tile, self.tile))
                elif self.next_matrix[matrix_y][matrix_x] == 1:
                    next_piece = pygame.draw.rect(screen, colors[next_figure], pygame.Rect(x, y, self.tile, self.tile))
                next_border = pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, self.tile, self.tile), 1)
                matrix_x += 1
                x += self.tile
            matrix_y += 1
            y += self.tile

    # Überprüft ob der Spieler verloren hat
    def end_game(self):
        matrix_x = 0
        matrix_y = 0
        for i in range(2):
            matrix_x = 0
            for j in range(self.width):
                if self.matrix[matrix_y][matrix_x] == 2:
                    return True
                matrix_x += 1
            matrix_y += 1
        return False

    # Matrix auf 0 setzen
    def reset(self):
        matrix_x = 0
        matrix_y = 0
        for i in range(len(self.matrix)):
            matrix_x = 0
            for j in range(len(self.matrix[matrix_y])):
                self.matrix[matrix_y][matrix_x] = 0
                matrix_x += 1
            matrix_y += 1

        matrix_x = 0
        matrix_y = 0
        for i in range(len(self.next_matrix)):
            matrix_x = 0
            for j in range(len(self.next_matrix[matrix_y])):
                self.next_matrix[matrix_y][matrix_x] = 0
                matrix_x += 1
            matrix_y += 1
            
    # neuen Highscore setzen, falls eingetreten
    def set_highscore(self):
        global highscore
        tetris_score_db.new_highscore(self.score)
        highscore = tetris_score_db.get_highscore()
        highscore = highscore[0][0]


# Action --> ALTER
# Assign Variables

# Standardfarben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

# Farben der Spielsteine
colors = {
    'I': (0, 255, 255),  # LIGHT_BLUE
    'J': (0, 0, 255),    # BLUE
    'L': (255, 128, 0),  # ORANGE
    'O': (255, 255, 0),  # YELLOW
    'S': (0, 255, 0),    # GREEN
    'T': (255, 0, 255),  # PURPLE
    'Z': (255, 0, 0)     # RED
}

# globale Variablen
bag = ["O", "S", "Z", "I", "J", "L", "T"]
next = -1
next_figure = 0
old_color = 0

# Highscore setzen
highscore = tetris_score_db.get_highscore()
if not highscore:
    highscore = 0
else:
    highscore = highscore[0][0]

# Initialisierungswerte
height = 20
width = 10
tile = 1
game = Game(height, width, tile)
game.create_shape()
game.draw()

# Text
font_1 = pygame.font.Font(None, 40)
level = font_1.render(f'Level: {game.level}', True, WHITE)
score = font_1.render('Score: ', True, WHITE)
points = font_1.render(f'{game.score}', True, WHITE)
incoming = font_1.render('Next: ', True, WHITE)
h_score = font_1.render(f'Highscore: {highscore}', True, WHITE)

font_2 = pygame.font.Font(None, 70)
restart = font_2.render("Press R to Restart", True, GREY)
rect_1 = restart.get_rect()
rect_1.center = screen.get_rect().center

# Laufvariablen
counter = 0
pressing_down = False

fps = 30
keepGoing = True
clock = pygame.time.Clock()

# Loop
while keepGoing:

    # Timer
    clock.tick(fps)

    if game.play:
        counter += 1
        # automatisches Bewegen
        if counter >= fps//(game.level + 1):
            game.down()
            game.draw()
            counter = 0
        # gedrückt halten
        if pressing_down:
            game.down()
            game.draw()

    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            keepGoing = False
            break

        if game.play:
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    pass
                if event.key == pygame.K_DOWN:
                    pressing_down = True
                elif event.key == pygame.K_LEFT:
                    game.left()
                    game.draw()
                elif event.key == pygame.K_RIGHT:
                    game.right()
                    game.draw()
                elif event.key == pygame.K_SPACE:
                    game.space()
                    game.draw()
                elif event.key == pygame.K_a:
                    old_rot = game.shape.rotation
                    game.shape.rotate_left()
                    game.update_shape(old_rot, 'left')
                    game.draw()
                elif event.key == pygame.K_s:
                    old_rot = game.shape.rotation
                    game.shape.rotate_right()
                    game.update_shape(old_rot, 'right')
                    game.draw()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False

        # Spiel Reset
        if not game.play:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    bag = ["O", "S", "Z", "I", "J", "L", "T"]
                    next = -1
                    next_figure = 0
                    old_color = 0

                    game.line_counter = 0
                    game.score = 0
                    game.level = 0
                    game.play = True

                    game.reset()
                    game.create_shape()
                    game.draw()

                    counter = 0
                    pressing_down = False

    # Redisplay
    screen.fill(BLACK)
    game.draw()
    screen.blit(score, (10, 10))
    screen.blit(incoming, (game.x_next_base, game.y_next_base-30))
    points = font_1.render(f'{game.score}', True, WHITE)
    level = font_1.render(f'Level: {game.level}', True, WHITE)
    h_score = font_1.render(f'Highscore: {highscore}', True, WHITE)
    screen.blit(points, (10, 40))
    screen.blit(level, (screen_width-125, 10))
    screen.blit(h_score, (10, game.y_base+410))
    if not game.play:
        screen.blit(restart, rect_1)
    pygame.display.flip()
