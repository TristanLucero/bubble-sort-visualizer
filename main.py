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

    for row in range(0, xs - 1):
        color = BLACK
        block_is_solid = 0
        pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * ys + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT], block_is_solid)


def generate_random_array():
    random.seed()
    values = random.randint(0, 60, 80)
    return values


def print_updated_array(values):
    for i in range(len(values)):
        draw_line(rowLen - values[i], rowLen, i, i)


def print_bubble_sort(values):
    for i in range(len(values)):
        for j in range(0, len(values) - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                time.sleep(0.01)
                print_updated_array(values)
                pygame.display.update()
                pygame.event.get()
    time.sleep(0.04)
    print_updated_array(values)
    pygame.display.update()


def print_selection_sort(values):
    for i in range(len(values)):
        min_idx = i
        for j in range(i + 1, len(values)):
            if values[min_idx] > values[j]:
                min_idx = j
                time.sleep(0.02)
                print_updated_array(values)
                pygame.display.update()
                pygame.event.get()
        values[i], values[min_idx] = values[min_idx], values[i]
    time.sleep(0.04)
    print_updated_array(values)
    pygame.display.update()


def print_insertion_sort(values):
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j -= 1
            time.sleep(0.003)
            print_updated_array(values)
            pygame.display.update()
            pygame.event.get()
        values[j + 1] = key
    time.sleep(0.005)
    print_updated_array(values)
    pygame.display.update()


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
                values = generate_random_array()
                print_updated_array(values)
                arrSorted = False
            elif event.key == pygame.K_1:
                if not arrSorted:
                    print_bubble_sort(values)
                    arrSorted = True
            elif event.key == pygame.K_2:
                if not arrSorted:
                    print_selection_sort(values)
                    arrSorted = True
            elif event.key == pygame.K_3:
                if not arrSorted:
                    print_insertion_sort(values)
                    arrSorted = True

    screen.fill(BLACK)
    print_updated_array(values)
    clock.tick(144)
    pygame.display.update()
