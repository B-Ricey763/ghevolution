from random import randrange
import neural_network
import genome
from dataclasses import dataclass
from settings import *
import world_view


@dataclass
class Point:
    x: int
    y: int


test_genome = [
    (False, 0, False, 0, 30000)
]


def start_generation(genes, should_display=False):
    genes = list(set(genes))
    brains = []
    positions = []
    for i in range(NUM_ORGANISMS):
        brains.append(neural_network.generate(genome.encode(test_genome)))
        positions.append(Point(randrange(0, X_SIZE), randrange(0, Y_SIZE)))

    if should_display:
        screen = world_view.init_display()

    for i in range(STEPS_PER_GEN):
        step(brains, positions, i)
        if should_display:
            world_view.update_display(screen, positions)


def step(brains, positions, _step_num):
    for brain, pos in zip(brains, positions):
        update_org(brain, pos)


def update_org(brain, pos):
    # first think, then act on it, updating the state
    neural_network.act(neural_network.think(brain, pos), pos)
