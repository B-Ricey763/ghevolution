from collections import namedtuple
from turtle import position
import brain_view
from functools import reduce
from enum import Enum
from math import floor
from random import random, randrange
import neural_network
import genome
from dataclasses import dataclass
from settings import *
import settings
import world_view
from actions import action_funcs
import numpy as np


class Cell(Enum):
    ORG = 1


def crossover(gene1, gene2):
    crossover_pt = randrange(TOTAL_BYTES * 2)
    new1 = gene1[:crossover_pt] + gene2[crossover_pt:]
    new2 = gene2[:crossover_pt] + gene1[crossover_pt:]
    return (new1, new2)


def start_generation(genes, gen_num):

    # Remove duplicate genes
    # brains = [(neural_network.generate(g), floor(NUM_ORGANISMS * n / num_s), g)
    #           for g, n in genes.items()]
    # # positions = np.zeros((Y_SIZE, X_SIZE), dtype=np.short)
    # positions = []
    # for i in range(NUM_ORGANISMS):
    #     # Randomize position for each organism at start
    #     # positions[randrange(Y_SIZE)][randrange(X_SIZE)] = Cell.ORG.value
    #     positions.append(Point(randrange(X_SIZE), randrange(Y_SIZE)))
    brains = [(neural_network.generate(gene), gene) for gene in genes]
    positions = [Point(randrange(X_SIZE), randrange(Y_SIZE))
                 for _ in range(NUM_ORGANISMS)]

    is_displaying = False
    if SHOULD_DISPLAY and (gen_num <= 5 or gen_num % (NUM_GENERATIONS // 2) == 0 or gen_num >= NUM_GENERATIONS - 3):
        is_displaying = True
        screen = world_view.init_display()

    if NUM_GENERATIONS // 2 == gen_num:
        settings.TOP_BOUND = 20

    for i in range(STEPS_PER_GEN):
        # we are currying the step function to send more info
        step(brains, positions)
        if is_displaying:
            world_view.update_display(screen, brains, positions, gen_num)

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
    total_survivors = 0
    for (_brain, gene), pos in zip(brains, positions):
        if survivor_condition(pos):
            # the ones that surive, their genes are added
            if gene not in surviving_genes:
                surviving_genes[gene] = 0
            surviving_genes[gene] += 1
            total_survivors += 1

    sorted_genes = sorted(
        surviving_genes, key=surviving_genes.get, reverse=True)
    best_genes = []
    # for i, gene in enumerate(sorted_genes):
    #     if i % 2 == 1 and len(best_genes) < NUM_ORGANISMS:
    #         (new1, new2) = crossover(sorted_genes[i - 1], gene)
    #         best_genes.append(new1)
    #         best_genes.append(new2)

    # # the above for loop is not guaranteed to fill everything for the next
    # # generation so we just reuse the best genes from the last
    # i = 0
    # while len(best_genes) < NUM_ORGANISMS and i < len(sorted_genes):
    #     best_genes.append(sorted_genes[i])
    #     i += 1

    # # If we still need more we just fill it randomly
    # while len(best_genes) < NUM_ORGANISMS:
    #     best_genes.append(genome.generate())
    while len(best_genes) < NUM_ORGANISMS:
        gene1 = sorted_genes[randrange(len(sorted_genes))]
        gene2 = sorted_genes[randrange(len(sorted_genes))]
        (c1, c2) = crossover(gene1, gene2)
        best_genes.append(c1)
        best_genes.append(c2)

    for gene in best_genes:
        if random() < MUTATION_CHANCE:
            gene = genome.mutate(gene)

    # last param is best gene
    return (best_genes, total_survivors, sorted_genes[0])


# UNUSED
def fitness_score(position):
    return position.x


def survivor_condition(position):
    return position.x < LEFT_BOUND and position.y < settings.TOP_BOUND


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
