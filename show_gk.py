# Example using Python and NetworkX (Conceptual)
import matplotlib.pyplot as plt
import networkx as nx
import os
import matplotlib
from math import gcd

# Assume you have functions to get primes and element orders from your group software


def save_info(name, primes, edges):
    with open("saved_info.py", "a") as file:
        file.write(f"graphs['{name}'] = ({primes}, {edges})\n")


def draw_graph(name, primes, orders):
    GK_graph = nx.Graph()
    for prime in primes:
        GK_graph.add_node(prime, value=f"\'prime\'")

    edges = set()
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            p, q = primes[i], primes[j]
            if (p * q) in orders:
                GK_graph.add_edge(p, q)
                edges.add((p, q))

    save_info(name.split("/")[-1], primes, edges)
    plt.figure(figsize=(8, 6))
    pos = nx.circular_layout(GK_graph)
    nx.draw(GK_graph, pos, node_size=3200, edgecolors='black', linewidths=3, node_color='white', width=3)
    nx.draw_networkx_labels(GK_graph, pos, font_color='black', font_size=24, )

    plt.savefig(name + ".png")


# draw_graph("graphs/Aut(M22)", [2, 3, 5, 7, 11], [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14])
# draw_graph("Aut(J3)", [2, 3, 5, 17, 19], [1, 2, 3, 4, 5, 6, 34, 8, 9, 10, 12, 15, 17, 18, 19, 24])
# draw_graph("Aut(HS)", [2, 3, 5, 7, 11], [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 20, 30])

# draw_graph("Aut(ON)", [2, 3, 5, 7, 11, 19, 31], [6, 15, 10, 14, 22, 38])
# draw_graph("Fi24'", [2, 3, 5, 7, 11, 13, 17, 23, 29], [6, 10, 14, 22, 26, 15, 21, 33, 39, 35])
# draw_graph("Aut(Fi24')", [2, 3, 5, 7, 11, 13, 17, 23, 29], [6, 10, 14, 22, 26, 34, 46, 15, 21, 33, 39, 35])

# draw_graph("cands/ON/U3(31)", [2, 3, 5, 7, 19, 31], [])
