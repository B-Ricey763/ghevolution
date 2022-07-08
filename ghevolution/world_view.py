from math import floor
import sys
from turtle import pos
from matplotlib.pyplot import draw
import pygame


from settings import *

black = 0, 0, 0
display_size = (X_SIZE + 1) * CELL_SIZE, (Y_SIZE + 1) * CELL_SIZE
font = None


def init_display():
    global font
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 32)
    return pygame.display.set_mode(display_size)


def update_display(screen, for_each_org, brains, positions, gen_num):
    global font
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(black)
    pygame.draw.line(screen, (255, 255, 255), (LEFT_BOUND * CELL_SIZE, 0),
                     (LEFT_BOUND * CELL_SIZE, display_size[1]), 2)

    text = font.render("Generation: " + str(gen_num), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (display_size[1] // 2, 20)

    def render_org(_, gene, pos, i):
        hex_nums = [int(''.join(item), 16) for item in zip(*[iter(gene)] * 8)]
        screen.fill(pygame.Color(floor(sum(hex_nums)/len(hex_nums))), pygame.Rect(
            pos.x * CELL_SIZE, pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        return 0
    # We love dependency injection!
    for_each_org(brains, positions, render_org)
    screen.blit(text, textRect)
    pygame.display.flip()
    pygame.time.delay(STEP_DISPLAY_TIME)
