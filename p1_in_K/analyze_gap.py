from draw.create_graph import get_primes
from draw.saved_info import check_edge, clear_name

edges_by_group_and_chi = dict()  # by (group, p1, chi_id) - list of possibly extra edges
chi_by_group_and_p1 = dict()  # by (group, p1) - list of ids of characters
extra_groups = ["Fi23"]  # list of extra groups for Fi24'

with open('fixedpoint_main.txt', 'r') as file:
    next(file)  # skip first line
    for line in file:
        group, chi_id, p1, p2, cls, sz = line.split(" ")
        group = clear_name(group)  # M22.2 -> Aut(M22)
        chi_id = int(chi_id)
        p1 = int(p1)
        p2 = int(p2)
        sz = int(sz)
        primes = get_primes(sz)
        if group not in extra_groups and p1 == primes[-1]:  # Ignore the biggest prime of G which is not in p_1(G)
            continue
        if p2 == -1:  # It is the first time when (p1, chi_id) is presented
            edges_by_group_and_chi[(group, p1, chi_id)] = edges_by_group_and_chi.get((group, p1, chi_id), set())

            # add to chi to chi_by_group_and_p1
            chi_by_group_and_p1[(group, p1)] = chi_by_group_and_p1.get((group, p1), set())
            chi_by_group_and_p1[(group, p1)].add(chi_id)
        else:
            edges_by_group_and_chi[(group, p1, chi_id)].add((p1, p2))

output = open("res.txt", 'w')
for group_and_p1, chi_list in chi_by_group_and_p1.items():
    group = group_and_p1[0]
    p1 = group_and_p1[1]
    # We need to aut group which we are checking now (Fi23 -> Fi24')
    if group in extra_groups:
        aut_group = "Aut(Fi24')"
    elif group.startswith("Aut"):
        aut_group = group
    else:
        aut_group = "Aut(" + group + ")"
    # Is it true that every character add an extra edge?
    all_extra_edge = True
    for chi in chi_list:
        p1p2 = sorted(edges_by_group_and_chi[(group, p1, chi)])
        extra_edge = False
        # Check that there is no extra edges
        for edge in p1p2:
            if not check_edge(aut_group, edge) and not extra_edge:
                # This edges is extra
                extra_edge = True
        if not extra_edge:
            all_extra_edge = False
    if all_extra_edge and group != aut_group:
        output.write(f"{p1} not in π(K) for {aut_group}\n")
    elif not all_extra_edge and group == aut_group:
        output.write(f"{p1} can be in π(K) for {aut_group}\n")
