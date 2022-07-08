from collections import namedtuple
from turtle import position
import brain_view
from functools import reduce
from enum import Enum
from math import floor
from random import randrange
import neural_network
import genome
from dataclasses import dataclass
from settings import *
import world_view
from actions import action_funcs
import numpy as np


class Cell(Enum):
    ORG = 1


class org_iter():
    def __init__(self, brains, positions):
        self.brains = brains
        self.positions = positions
        self.pos_index = 0  # offset by one
        self.brain_idx_start = 0
        self.brain_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.brain_index < len(self.brains) and self.pos_index < len(self.positions):
            n = self.brains[self.brain_index][1]
            tup = (self.positions[self.pos_index],
                   *self.brains[self.brain_index])
            self.pos_index += 1
            if self.brain_idx_start + n < self.pos_index:
                self.brain_index += 1
                self.brain_idx_start += n
            return tup
        else:
            raise StopIteration


def for_each_org(brains, positions, f):
    num = 0
    pos_index = 0
    for brain, n, gene in brains:
        for i in range(n):
            num += f(brain, gene, positions[pos_index + i], pos_index + i)
        pos_index += n
    return num


def crossover(gene1, gene2):
    crossover_pt = randrange(TOTAL_BYTES * 2)
    new1 = gene1[:crossover_pt] + gene2[crossover_pt:]
    new2 = gene2[:crossover_pt] + gene1[crossover_pt:]
    return (new1, new2)


def start_generation(genes, gen_num, num_s, should_display=False):

    # Remove duplicate genes
    brains = [(neural_network.generate(g), floor(NUM_ORGANISMS * n / num_s), g)
              for g, n in genes.items()]
    # positions = np.zeros((Y_SIZE, X_SIZE), dtype=np.short)
    positions = []
    for i in range(NUM_ORGANISMS):
        # Randomize position for each organism at start
        # positions[randrange(Y_SIZE)][randrange(X_SIZE)] = Cell.ORG.value
        positions.append(Point(randrange(X_SIZE), randrange(Y_SIZE)))

    if gen_num <= 5 or gen_num % (NUM_GENERATIONS // 2) == 0 or gen_num >= NUM_GENERATIONS - 3:
        should_display = True
    if should_display:
        screen = world_view.init_display()

    for i in range(STEPS_PER_GEN):
        # we are currying the step function to send more info
        step(brains, positions)
        if should_display:
            world_view.update_display(
                screen, for_each_org, brains, positions, gen_num)

    return get_survivors(brains, positions)


def get_survivors(brains, positions):
    surviving_genes = dict()
    # for pos, _b, _n, gene in org_iter(brains, positions):
    #     if survivor_condition(pos):
    #         # the ones that surive, their genes are added
    #         if gene not in surviving_genes:
    #             surviving_genes[gene] = 0
    #         surviving_genes[gene] += 1
    #         total_survivors += 1

    # Mutate list to hold proportions, not ints
    # for gene, num in surviving_genes.items():
    #     surviving_genes[gene] = num / total_survivors
    def f(brain, gene, pos, i):
        n = 0
        if survivor_condition(pos):
            # the ones that surive, their genes are added
            if gene not in surviving_genes:
                surviving_genes[gene] = 0
            surviving_genes[gene] += 1
            n += 1
        return n
    total_survivors = for_each_org(brains, positions, f)

    return (surviving_genes, total_survivors)


def survivor_condition(position):
    return position.x < LEFT_BOUND


# ITS A GLOBAL var i know but we want performance
position_grid = np.zeros((Y_SIZE, X_SIZE), dtype=np.short)


def step(brains, positions):
    position_grid.fill(0)
    # Populate the cells with the current positions, for collisions
    for p in positions:
        position_grid[p.y][p.x] = Cell.ORG.value

    def step_org(brain, _, pos, i):
        actions = neural_network.think(brain, pos)
        for action in actions:
            p = action_funcs[action](pos)
            # Verify the cell is not occupied, and then work
            if position_grid[p.y][p.x] != Cell.ORG.value:
                position_grid[p.y][p.x] = Cell.ORG.value
                positions[i] = p
        # stupid state code stuff
        return 0

    for_each_org(brains, positions, step_org)
