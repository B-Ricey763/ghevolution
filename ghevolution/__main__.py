from pickle import TRUE
from matplotlib import pyplot as plt
import genome
from settings import *
import neural_network
import world
import world_view
import brain_view
import survivor_plot


if __name__ == "__main__":
    genes = [genome.generate() for _ in range(NUM_ORGANISMS)]
    gen_num = list(range(NUM_GENERATIONS))
    survivor_list = [0] * NUM_GENERATIONS
    for i in range(NUM_GENERATIONS):
        (genes, num_s, best_gene) = world.start_generation(genes, i)
        survivor_list[i] = num_s
    brain_view.draw_brain(best_gene)
    survivor_plot.show_gen_survivors(gen_num, survivor_list)
