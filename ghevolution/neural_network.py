from ctypes.wintypes import SIZE
from turtle import pos
import genome
import enum
from settings import *
from math import tanh

sensory_evaluations = {
    # Percent distance from right wall
    0: (lambda pos: pos.x / X_SIZE),
}


def move_left(pos):
    pos.x -= 1


def move_right(pos):
    pos.x += 1


actions = {
    0: move_left,
    1: move_right,
}


def generate(genes):
    brain = {}
    for (_, from_id, _, to_id, raw_weight) in genome.decode(genes):
        weight = raw_weight / WEIGHT_DIV
        # Lazy initialization of dict keys to keep graph small
        # We make our keys the action neurons to be easier
        if from_id not in brain:
            brain[to_id] = [(from_id, weight)]
        else:
            brain[to_id].append((from_id, weight))
    return brain

# when we think, we want to evaluate the relevant stimuli
# using our sensory neurons, which produce a float multiplied by
# the weight
# Input neurons produce value from 0.0 to 1.0 * weight
# action neurons take all inputs and sum and tanh (similar to curved clamp)
# So for an overarching structure, you can start at action neurons
# and recursively calculate the input neurons, memoizing already sensed values


def think(brain, pos):
    actions = []
    for action, sensory in brain.items():
        inputVal = tanh(sum(map(
            # Please refactor this sometime
            lambda id_weight: sensory_evaluations[id_weight[0]](
                pos) * id_weight[1],
            sensory)))
        if abs(inputVal) > 0.5:
            actions.append(action)
    return actions


def act(action_ids, pos):
    # We pass the state in to mutate
    # it would be better to make it immutable,
    # but that has performance and write implementations
    # the only benefit is using lambdas, which i can't do with mutation
    for id in action_ids:
        actions[id](pos)
