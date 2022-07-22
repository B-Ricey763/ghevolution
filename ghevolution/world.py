from collections import namedtuple
from turtle import pos, position
import brain_view
from functools import reduce
from enum import Enum
from math import floor
from random import random, randrange
from ghevolution.survivor_plot import dyn_graph_survivors
import neural_network
import genome
from dataclasses import dataclass
from settings import *
import settings
import world_view
from actions import action_funcs
import numpy as np
import bounds
import survivor_plot


class Cell(Enum):
    ORG = 1


def crossover(gene1, gene2):
    crossover_pt = randrange(TOTAL_BYTES * 2)
    new1 = gene1[:crossover_pt] + gene2[crossover_pt:]
    new2 = gene2[:crossover_pt] + gene1[crossover_pt:]
    return (new1, new2)


def start_generation(genes, gen_num):
    brains = [(neural_network.generate(gene), gene) for gene in genes]
    positions = [Point(randrange(X_SIZE), randrange(Y_SIZE))
                 for _ in range(NUM_ORGANISMS)]

    is_displaying = False
    if SHOULD_DISPLAY and gen_num % 10 == 0:
        is_displaying = True
        screen = world_view.init_display()

    for i in range(STEPS_PER_GEN):
        # we are currying the step function to send more info
        step(brains, positions)
        if is_displaying:
            world_view.update_display(screen, brains, positions, gen_num)

    return get_survivors(brains, positions)


def get_survivors(brains, positions):
    surviving_genes = dict()
    total_survivors = 0
    for (_brain, gene), pos in zip(brains, positions):
        if survivor_condition(pos):
            # the ones that surive, their genes are added
            if gene not in surviving_genes:
                surviving_genes[gene] = 0
            surviving_genes[gene] += 1
            total_survivors += 1

        # this was sorted to use the best organisms to reproduce, but
    # I ended up just mixing them randomly
    sorted_genes = sorted(
        surviving_genes, key=surviving_genes.get, reverse=True)
    best_genes = []

    if len(sorted_genes) > 0:
        while len(best_genes) < NUM_ORGANISMS:
            gene1 = sorted_genes[randrange(len(sorted_genes))]
            gene2 = sorted_genes[randrange(len(sorted_genes))]
            (c1, c2) = crossover(gene1, gene2)
            best_genes.append(c1)
            best_genes.append(c2)
    # contengency
    else:
        for i in range(NUM_ORGANISMS):
            best_genes.append(genome.generate())

        # Small chance for a mutation
    for gene in best_genes:
        if random() < MUTATION_CHANCE:
            gene = genome.mutate(gene)

    # last param is best gene, used for brain visulization
    return (best_genes, total_survivors, sorted_genes[0])


def survivor_condition(position):
    (pt1, pt2) = bounds.get_bounds()
    return position.x >= pt1.x and position.x <= pt2.x and position.y <= pt2.y and position.y >= pt1.y


# ITS A GLOBAL var i know but we want performance
position_grid = np.zeros((Y_SIZE, X_SIZE), dtype=np.short)


def step(brains, positions):
    position_grid.fill(0)
    # Populate the cells with the current positions, for collisions
    for p in positions:
        position_grid[p.y][p.x] = Cell.ORG.value

    for i, ((brain, gene), pos) in enumerate(zip(brains, positions)):
        actions = neural_network.think(brain, pos)
        for action in actions:
            p = action_funcs[action](pos)
            # Verify the cell is not occupied, and then work
            if position_grid[p.y][p.x] != Cell.ORG.value:
                position_grid[p.y][p.x] = Cell.ORG.value
                positions[i] = p
