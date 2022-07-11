from matplotlib import pyplot as plt


def show_gen_survivors(gen_num, survivor_list):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.fill_between(gen_num, survivor_list, alpha=0.5)
    ax.plot(gen_num, survivor_list)
    ax.set_ylabel("Surviving Organisms")
    ax.set_xlabel("Generation")
    plt.savefig('survivors_graph.png')
