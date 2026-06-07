from show_gk import draw_graph
from saved_info import *
import os


def get_primes(order):  # Returns list of prime factors of |G|
    i = 2
    cur_primes = []
    while i * i <= order:
        if order % i == 0:
            cur_primes.append(i)
            order //= i
            while order % i == 0:
                order //= i
        i += 1
    if order > 1:
        cur_primes.append(order)
    return cur_primes


def save_info(name, primes, edges):
    with open("draw/saved_info.py", "a") as file:
        file.write(f"graphs['{name}'] = ({primes}, {edges})\n")


def create_primes_and_edges(group_creation):
    command = f"(echo \"{group_creation}\" && cat draw/print_group_orders.g) | gap -q > draw/output.txt"
    print(command)
    os.system(command)
    output_lines = open("draw/output.txt").readlines()
    for i in range(len(output_lines)):
        line = output_lines[i]
        if line.startswith("Size:"):
            group_order = int(line.split()[1])
            primes = get_primes(group_order)
        elif line.startswith("Orders:"):
            orders = list(map(int, line.split()[1:]))
            j = i + 1
            while j < len(output_lines) and len(output_lines[j]) > 0:
                orders += list(map(int, output_lines[j].split()))
                j += 1
            orders = list(set(orders))
    edges = set()
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            p, q = primes[i], primes[j]
            if (p * q) in orders:
                edges.add((p, q))
    return primes, edges


def get_primes_and_edges(group_name, group_creation):
    if check_saved(group_name):
        return get_graph(group_name)
    graph = create_primes_and_edges(group_creation)
    save_info(group_name, graph[0], graph[1])
    return graph


def build_and_draw(group_name, file_name, group_creation):
    primes, edges = get_primes_and_edges(group_name, group_creation)
    draw_graph(file_name, primes, edges)
