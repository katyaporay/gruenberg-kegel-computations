from show_gk import draw_graph
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


def build_and_draw(group_name, file_name, group_creation):
    command = f"(echo \"{group_creation}\" && cat print_group_orders.sh) | gap -q > output.txt"
    print(command)
    os.system(command)
    output_lines = open("output.txt").readlines()
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

    print(primes)
    print(group_order)
    print(orders)
    print()
    print(f"draw_graph(\"{file_name}\", {primes}, {orders})")

    draw_graph(file_name, primes, orders)
