from random import random
import genome
from actions import Actions
from senses import Senses, sense_funcs
from settings import *
from math import tanh
from settings import *


def generate(genes, dontMutate=False):
    # There is a small chance the genes will mutate
    if random() < MUTATION_CHANCE and not dontMutate:
        genes = genome.mutate(genes)

    brain = dict()
    for (from_num, to_num, raw_weight) in genome.decode(genes):
        weight = raw_weight / WEIGHT_DIV
        # last couple indicies reserved for the inner neurons
        # this way we can simplify genes
        # find good way to do this
        from_id = from_num % len(Senses)
        to_id = to_num % len(Actions)
        # Lazy initialization of dict keys to keep graph small
        if to_id not in brain:
            brain[to_id] = set()
        brain[to_id].add((from_id, weight))
    return brain

# when we think, we want to evaluate the relevant stimuli
# using our sensory neurons, which produce a float multiplied by
# the weight
# Input neurons produce value from 0.0 to 1.0 * weight
# action neurons take all inputs and sum and tanh (similar to curved clamp)
# So for an overarching structure, you can start at action neurons
# and recursively calculate the input neurons, memoizing already sensed values


def think(brain, pos):
    def get_input(id_n_weight):
        (id, weight) = id_n_weight
        return sense_funcs[Senses(id)](pos) * weight

    actions = []
    for action_index, input in brain.items():
        inputVal = tanh(sum(map(get_input, input)))
        # it has to be positive, and then it has a chance of happening
        if inputVal >= 0 and inputVal >= random():
            # take raw index and put in enum
            actions.append(Actions(action_index))
    return actions
