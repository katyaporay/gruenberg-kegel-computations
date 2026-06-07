from draw.build_and_draw import build_and_draw


cands_by_group = dict()

cands_by_group["M22"] = ["L2(11)", "M11", "M12", "U5(2)", "A11", "McL", "HS", "A12", "U6(2)"]
cands_by_group["J3"] = ["L2(19)"]
cands_by_group["Fi24'"] = ["L2(29)", "L2(289)", "S4(17)", "Ru"]  # U4(17)
cands_by_group["O'N"] = ["L2(31)", "L3(5)", "L2(32)", "L2(125)", "G2(5)", "L5(2)", "L6(2)"]  # U3(31)


def create_aut_graph(group_name):
    file_name = "graphs/Aut(" + group_name + ")"
    group_creation = f"L := SimpleGroup(\\\"{group_name}\\\");\nG := AutomorphismGroup(L);"
    build_and_draw(f"Aut({group_name})", file_name, group_creation)


def create_graph(group_name):
    file_name = "graphs/" + group_name
    group_creation = f"G := SimpleGroup(\\\"{group_name}\\\");"
    build_and_draw(group_name, file_name, group_creation)


def create_cands_graph(group_name):
    for cand_group_name in cands_by_group[group_name]:
        file_name = "cands/" + group_name + "/" + cand_group_name
        group_creation = f"G := SimpleGroup(\\\"{cand_group_name}\\\");"
        build_and_draw(cand_group_name, file_name, group_creation)


for group in cands_by_group:
    create_graph(group)
    create_aut_graph(group)
    create_cands_graph(group)
