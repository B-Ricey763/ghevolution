from math import floor
import sys
from matplotlib.pyplot import draw
import pygame
import bounds

from settings import *
import settings

black = 0, 0, 0
white = 255, 255, 255
display_size = (X_SIZE + 1) * CELL_SIZE, (Y_SIZE + 1) * CELL_SIZE
font = None
screen = None
initialized = False


def init_display():
    global font, initialized, screen
    if not initialized:
        pygame.init()
        font = pygame.font.Font('freesansbold.ttf', 32)
        initialized = True
        screen = pygame.display.set_mode(display_size)
    return screen


def update_display(screen, brains, positions, gen_num):
    global font
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(black)
    (pt1, pt2) = bounds.get_bounds()
    # Left vert line
    pygame.draw.line(screen, white, (pt1.x * CELL_SIZE, pt1.y * CELL_SIZE),
                     (pt1.x * CELL_SIZE, pt2.y * CELL_SIZE), 2)
    # Right vert line
    pygame.draw.line(screen, white, (pt2.x * CELL_SIZE, pt1.y * CELL_SIZE),
                     (pt2.x * CELL_SIZE, pt2.y * CELL_SIZE), 2)
    # bottom line
    pygame.draw.line(screen, white, (pt1.x * CELL_SIZE, pt2.y * CELL_SIZE),
                     (pt2.x * CELL_SIZE, pt2.y * CELL_SIZE), 2)
    # top line
    pygame.draw.line(screen, white, (pt1.x * CELL_SIZE, pt1.y * CELL_SIZE),
                     (pt2.x * CELL_SIZE, pt1.y * CELL_SIZE), 2)

    text = font.render("Generation: " + str(gen_num), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (display_size[1] // 2, 20)

    for (brain, gene), pos in zip(brains, positions):
        hex_nums = [int(''.join(item), 16) for item in zip(*[iter(gene)] * 8)]
        screen.fill(pygame.Color(floor(sum(hex_nums)/len(hex_nums))), pygame.Rect(
            pos.x * CELL_SIZE, pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # We love dependency injection!
    screen.blit(text, textRect)
    pygame.display.flip()
    pygame.time.delay(STEP_DISPLAY_TIME)
