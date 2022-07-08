from matplotlib import pyplot as plt


def show_gen_survivors(gen_num, survivor_list):
    ax1 = plt.subplot(5, 5, 2)
    plt.figure(figsize=(8, 6))
    plt.fill_between(gen_num, survivor_list, alpha=0.5)
    plt.plot(gen_num, survivor_list)
    plt.title = "Survivors vs Generation"
    plt.xlabel = "Generation Num"
    plt.ylabel = "Number of Survivors"
    plt.savefig('survivors_graph.png')
