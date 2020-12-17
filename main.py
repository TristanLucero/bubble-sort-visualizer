import pygame
import sys
from numpy import random
import time

# Colors
BLACK = (25, 25, 25)
WHITE = (168, 167, 167)
BLUE = (0, 255, 255)
RED = (255, 0, 0)

# Block width / height / margin between them
WIDTH = 10
HEIGHT = 10
MARGIN = 2

# Initialize Grid
rowLen = 60
colLen = 80
grid = []
for row in range(rowLen):
    grid.append([])
    for column in range(colLen):
        grid[row].append(0)

# Init window
pygame.init()
WINDOW_SIZE = [965, 723]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Bubble Sort Visualizer")
clock = pygame.time.Clock()


def draw_line(xs, xf, ys, yf):
    for row in range(xs, xf):
        color = BLUE
        block_is_solid = 0
        pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * ys + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT], block_is_solid)

    for row in range(0, xs-1):
        color = BLACK
        block_is_solid = 0
        pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * ys + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT], block_is_solid)


def draw_wall(pos, state):
    col = pos[0] // (WIDTH + MARGIN)
    row = pos[1] // (HEIGHT + MARGIN)
    print(col, row)
    if col < len(grid[0]) and row < len(grid):
        grid[row][col] = 1


def generate_random_array():
    random.seed()
    values = random.randint(0, 60, 80)
    return values


def print_updated_array(values):
    for i in range(len(values)):
        draw_line(rowLen - values[i], rowLen, i, i)


def print_buble_sort(values):
    for i in range(len(values)):
        for j in range(0, len(values) - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                time.sleep(0.02)
                print_updated_array(values)
                pygame.display.update()
                print(values)

# Grid Array
values = generate_random_array()

# Sort value
arrSorted = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not arrSorted:
                    print_buble_sort(values)
                    arrSorted = True
    screen.fill(BLACK)
    print_updated_array(values)
    clock.tick(144)
    pygame.display.update()

