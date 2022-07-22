from matplotlib import pyplot as plt
from numpy import block


def show_gen_survivors(gen_num, survivor_list):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.fill_between(gen_num, survivor_list, alpha=0.5)
    ax.plot(gen_num, survivor_list)
    ax.set_ylabel("Surviving Organisms")
    ax.set_xlabel("Generation")
    plt.savefig('survivors_graph.png')


initialized = False
fig, ax = None, None


def init_graph():
    global fig, ax
    fig, ax = plt.subplots(figsize=(8, 6))


def dyn_graph_survivors(gen_num, survivor_list):
    ax.plot(gen_num, survivor_list)
    ax.fill_between(gen_num, survivor_list,
                    alpha=1, color='blue', edgecolor='blue')
    ax.set_ylabel("Surviving Organisms")
    ax.set_xlabel("Generation")
    fig.canvas.draw()
    fig.canvas.flush_events()


def clear_graph():
    ax.clear()
