from pickle import TRUE
from matplotlib import pyplot as plt
import genome
from settings import *
import neural_network
import world
import world_view
import brain_view


def show_gen_survivors(gen_num, survivor_list):
    plt.subplot(232)
    plt.plot(gen_num, survivor_list)
    plt.title = "Survivors vs Generation"
    plt.xlabel = "Generation Num"
    plt.ylabel = "Number of Survivors"
    plt.savefig('survivors_graph.png')


def show_best_brain(genes):
    best_n = 0
    best_gene = ""
    for gene, n in genes.items():
        if n > best_n:
            best_gene = gene
            best_n = n
    brain_view.draw_brain(neural_network.generate(best_gene, True))


if __name__ == "__main__":
    genes = {genome.generate(): 1 for i in range(NUM_ORGANISMS)}
    gen_num = list(range(NUM_GENERATIONS))
    num_s = NUM_ORGANISMS
    survivor_list = [0] * NUM_GENERATIONS
    for i in range(NUM_GENERATIONS):
        (genes, num_s) = world.start_generation(genes, i, num_s)
        survivor_list[i] = num_s
    show_best_brain(genes)
    show_gen_survivors(gen_num, survivor_list)
