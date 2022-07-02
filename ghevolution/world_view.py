import sys
from numpy import rec
import pygame
from world import Point

from settings import *


def draw_cells(surface, positions):
    for pos in positions:
        surface.fill(CELL_COLOR, pygame.Rect(
            pos.x * CELL_SIZE, pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def display():
    pygame.init()

    black = 0, 0, 0
    display_size = display_width, display_height = X_SIZE * 5, Y_SIZE * 5

    screen = pygame.display.set_mode(display_size)

    rect = pygame.Rect(0, 0, 100, 100)

    for _ in range(STEPS_PER_GEN):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(black)
        draw_cells(screen, [
            Point(1, 2),
            Point(2, 2),
            Point(5, 10)
        ])
        pygame.display.flip()
        pygame.time.delay(10)
