from draw.create_graph import get_primes
from draw.saved_info import check_edge, clear_name

edges_by_chi = dict()


with open('fixedpoint_main.txt', 'r') as file:
    next(file)  # skip first line
    for line in file:
        group, chi_id, p1, p2, cls, sz = line.split(" ")
        group = clear_name(group)
        chi_id = int(chi_id)
        p1 = int(p1)
        p2 = int(p2)
        sz = int(sz)
        if group != "Fi23" or p1 != 2:
            continue
        if p2 == -1:  # It is the first time when (chi_id) is presented
            edges_by_chi[chi_id] = edges_by_chi.get(chi_id, set())
        else:
            edges_by_chi[chi_id].add((p1, p2))

edges_presented_always = True
check_edges = [(2, 17), (2, 23)]
for chi, edges in edges_by_chi.items():
    # Is it true that every character add an extra edge?
    edges = set(edges)
    edges_presented = True
    for edge in check_edges:
        if edge not in edges:
            edges_presented = False
    if not edges_presented:
        edges_presented_always = False

if edges_presented_always:
    print(f"edges {check_edges} are always presented")
else:
    print(f"Something went wrong with edges {check_edges}")
