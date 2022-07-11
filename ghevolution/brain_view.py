import matplotlib.pyplot as plt
import networkx as nx
import actions
import senses
import neural_network

options = {
    'node_size': 750,
    'width': 3,
    'arrows': True,
    'with_labels': True,
}


def draw_brain(gene):
    brain = neural_network.generate(gene)
    g = nx.DiGraph()
    for to_id, inputs in brain.items():
        for from_id, weight in inputs:
            g.add_edge(senses.display_names[senses.Senses(from_id)], actions.display_names[actions.Actions(
                to_id)], weight=weight)
    colors = []
    for node in g:
        if node in senses.display_names.values():
            colors.append('yellow')
        else:
            colors.append('red')
    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw_planar(g, node_color=colors, ax=ax, label="hello", **options)
    plt.savefig('brain_graph.png')
