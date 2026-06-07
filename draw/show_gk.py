import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(name, primes, edges):
    """Creates image of graph with vertices {primes} and edges {edges} in file with path {name}.png"""
    gk_graph = nx.Graph()
    for prime in primes:
        # Add vertex {prime} to graph
        gk_graph.add_node(prime, value=f"\'prime\'")

    for (p, q) in edges:
        # Add edge (p, q) to graph
        gk_graph.add_edge(p, q)

    plt.figure(figsize=(8, 6))
    pos = nx.circular_layout(gk_graph)  # The vertices are arranged in a circle
    nx.draw(gk_graph, pos, node_size=3200, edgecolors='black', linewidths=3, node_color='white', width=3)  # Draw
    nx.draw_networkx_labels(gk_graph, pos, font_color='black', font_size=24, )  # Add numbers of primes to vertices

    plt.margins(0.1)  # Add margins
    plt.savefig(name + ".png")  # Save image
    plt.close()
