import sys
from numpy import rec
import pygame

from settings import *

black = 0, 0, 0
display_size = display_width, display_height = X_SIZE * 5, Y_SIZE * 5


def init_display():
    pygame.init()
    return pygame.display.set_mode(display_size)


def update_display(screen, positions):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(black)
    for pos in positions:
        screen.fill(CELL_COLOR, pygame.Rect(
            pos.x * CELL_SIZE, pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()
    pygame.time.delay(10)
