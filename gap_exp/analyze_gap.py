from draw.build_and_draw import get_primes
from draw.saved_info import check_edge, clear_name

edges_by_group = dict()
extra_groups = ["Fi23"]

with open('gap_exp/fixedpoint_main.txt', 'r') as file:
    next(file)
    for line in file:
        group, chi_id, p1, p2, cls, sz = line.split(" ")
        chi_id = int(chi_id)
        p1 = int(p1)
        p2 = int(p2)
        sz = int(sz)
        primes = get_primes(sz)
        if p1 == primes[-1]:
            continue
        if p2 == -1:
            edges_by_group[(group, p1, chi_id)] = edges_by_group.get((group, p1, chi_id), set())
        else:
            edges_by_group[(group, p1, chi_id)].add((p1, p2))

for group_and_chi, p1p2 in edges_by_group.items():
    p1p2 = sorted(p1p2)
    group = group_and_chi[0]
    group = clear_name(group)
    chi = group_and_chi[1]
    if group in extra_groups:
        aut_group = "Aut(Fi24')"
    elif group.startswith("Aut"):
        simple_group = group[3:-1]
        aut_group = group
    else:
        simple_group = group
        aut_group = "Aut(" + simple_group + ")"
    ok = True
    # Check that there is no extra edges
    for edge in p1p2:
        if not check_edge(aut_group, edge) and ok:
            print("Extra edge:", *edge)
            ok = False
    print(ok, group_and_chi, p1p2)
