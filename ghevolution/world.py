from random import randrange
import neural_network
import genome
from dataclasses import dataclass
from settings import *


@dataclass
class Point:
    x: int
    y: int


test_genome = [
    (False, 0, False, 0, 30000)
]


def start_generation():
    gen_info = []
    for i in range(NUM_ORGANISMS):
        brain = neural_network.generate(genome.encode(test_genome))
        state = {
            "pos": Point(randrange(0, X_SIZE), randrange(0, Y_SIZE))
        }
        gen_info.append((brain, state))

    for i in range(STEPS_PER_GEN):
        step(gen_info, i)


def step(gen_info, i):
    update_org(gen_info[i][0], gen_info[i][1])


def update_org(brain, state):
    # first think, then act on it, updating the state
    neural_network.act(neural_network.think(brain, state), state)
