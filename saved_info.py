graphs = dict()
graphs['Aut(M22)'] = ([2, 3, 5, 7, 11], {(2, 3), (2, 5), (2, 7)})
graphs['M22'] = ([2, 3, 5, 7, 11], {(2, 3)})
graphs['J3'] = ([2, 3, 5, 17, 19], {(2, 3), (2, 5), (3, 5)})
graphs['Aut(J3)'] = ([2, 3, 5, 17, 19], {(2, 3), (2, 5), (2, 17), (3, 5)})
graphs['Fi24'] = ([2, 3, 5, 7, 11, 13, 17, 23, 29], {(2, 3), (2, 5), (2, 7), (2, 11), (2, 13), (3, 5), (3, 7), (3, 11), (3, 13), (5, 7)})
graphs['Aut(Fi24)'] = ([2, 3, 5, 7, 11, 13, 17, 23, 29], {(2, 3), (2, 5), (2, 7), (2, 11), (2, 13), (2, 17), (2, 23), (3, 5), (3, 7), (3, 11), (3, 13), (5, 7)})
graphs['ON'] = ([2, 3, 5, 7, 11, 19, 31], {(2, 3), (2, 5), (2, 7), (3, 5)})
graphs['Aut(ON)'] = ([2, 3, 5, 7, 11, 19, 31], {(2, 3), (2, 5), (2, 7), (2, 11), (2, 19), (3, 5)})


def clear_name(name):
    name = name.replace("'", "")
    if name.endswith(".2"):
        name = "Aut(" + name[:-2] + ")"
    assert name in graphs
    return name


def check_edge(name: str, edge):
    name = clear_name(name)
    a = edge[0]
    b = edge[1]
    edges = graphs[name][1]
    return (a, b) in edges or (b, a) in edges


def get_all_edges(name: str):
    name = clear_name(name)
    return graphs[name][1]
