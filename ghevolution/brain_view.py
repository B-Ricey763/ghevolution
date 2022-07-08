import matplotlib.pyplot as plt
import networkx as nx
import actions
import senses

options = {
    'node_color': 'yellow',
    'node_size': 300,
    'width': 3,
    'arrows': True,
    'with_labels': True,
}


def draw_brain(brain):
    g = nx.DiGraph()
    for to_id, inputs in brain.items():
        for from_id, weight in inputs:
            g.add_edge(senses.display_names[senses.Senses(from_id)], actions.display_names[actions.Actions(
                to_id)], weight=weight)

    plt.subplot(121)
    nx.draw_planar(g, **options)
    plt.savefig('brain_graph.png')
