import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(name, primes, edges):
    gk_graph = nx.Graph()
    for prime in primes:
        gk_graph.add_node(prime, value=f"\'prime\'")

    for (p, q) in edges:
        gk_graph.add_edge(p, q)

    plt.figure(figsize=(8, 6))
    pos = nx.circular_layout(gk_graph)
    nx.draw(gk_graph, pos, node_size=3200, edgecolors='black', linewidths=3, node_color='white', width=3)
    nx.draw_networkx_labels(gk_graph, pos, font_color='black', font_size=24, )

    plt.margins(0.1)
    plt.savefig(name + ".png")
    plt.close()
