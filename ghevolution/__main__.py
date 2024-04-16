import bounds
from matplotlib import pyplot as plt
from numpy import block
import genome
from settings import *
import neural_network
import world
import world_view
import brain_view
import survivor_plot


if __name__ == "__main__":
    # survivor_plot.init_graph()
    # plt.ion()
    # plt.show(block=False)
    while True:
        genes = [genome.generate() for _ in range(NUM_ORGANISMS)]
        gen_num = list(range(NUM_GENERATIONS))
        survivor_list = list()
        for i in range(NUM_GENERATIONS):
            (genes, num_s, best_gene) = world.start_generation(genes, i)
            # survivor_plot.dyn_graph_survivors(gen_num[:i], survivor_list)
            survivor_list.append(num_s)
            # brain_view.dyn_drawn_brain(best_gene)
        bounds.cycle_bounds()
        # survivor_plot.clear_graph()

    # brain_view.draw_brain(best_gene)
    # survivor_plot.show_gen_survivors(gen_num, survivor_list)
