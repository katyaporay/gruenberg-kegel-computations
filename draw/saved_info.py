# This is dict of saved graphs: name -> (vertices, edges)
graphs = dict()


def clear_name(name):
    """It standardises this name, so that, for example, M22.2 would be the same is Aut(M22)"""
    name = name.split("/")[-1]
    name = name.replace("'", "")
    if name.endswith(".2"):
        name = "Aut(" + name[:-2] + ")"
    return name


def check_edge(name: str, edge):
    """Checks is there edge if Gruenberg-Kegel graph of group {name}"""
    name = clear_name(name)
    a = edge[0]
    b = edge[1]
    edges = graphs[name][1]
    return (a, b) in edges or (b, a) in edges


def check_saved(name: str):
    """Check is Gruenberg-Kegel graph of group {name} already saved there"""
    name = clear_name(name)
    return name in graphs


def get_graph(name: str):
    """Returns saved Gruenberg-Kegel graph of group {name}"""
    name = clear_name(name)
    return graphs[name]


def get_all_edges(name: str):
    """Returns all edges of Gruenberg-Kegel graph of group {name}"""
    name = clear_name(name)
    return graphs[name][1]


# Some graphs of the first groups are written from Atlas
graphs['Aut(M22)'] = ([2, 3, 5, 7, 11], {(2, 3), (2, 5), (2, 7)})
graphs['M22'] = ([2, 3, 5, 7, 11], {(2, 3)})
graphs['J3'] = ([2, 3, 5, 17, 19], {(2, 3), (2, 5), (3, 5)})
graphs['Aut(J3)'] = ([2, 3, 5, 17, 19], {(2, 3), (2, 5), (2, 17), (3, 5)})
graphs['Fi24'] = ([2, 3, 5, 7, 11, 13, 17, 23, 29], {(2, 3), (2, 5), (2, 7), (2, 11), (2, 13), (3, 5), (3, 7), (3, 11), (3, 13), (5, 7)})
graphs['Aut(Fi24)'] = ([2, 3, 5, 7, 11, 13, 17, 23, 29], {(2, 3), (2, 5), (2, 7), (2, 11), (2, 13), (2, 17), (2, 23), (3, 5), (3, 7), (3, 11), (3, 13), (5, 7)})
graphs['ON'] = ([2, 3, 5, 7, 11, 19, 31], {(2, 3), (2, 5), (2, 7), (3, 5)})
graphs['Aut(ON)'] = ([2, 3, 5, 7, 11, 19, 31], {(2, 3), (2, 5), (2, 7), (2, 11), (2, 19), (3, 5)})
graphs['HN'] = ([2, 3, 5, 7, 11, 19], {(2, 7), (3, 7), (5, 7), (2, 3), (2, 5), (2, 11), (3, 5)})
graphs['Aut(HS)'] = ([2, 3, 5, 7, 11], {(2, 3), (2, 5), (3, 5), (2, 7)})
graphs['McL'] = ([2, 3, 5, 7, 11], {(2, 3), (2, 5), (3, 5), (2, 7)})
graphs['Suz'] = ([2, 3, 5, 7, 11, 13], {(2, 7), (3, 7), (2, 3), (2, 5), (3, 5)})
graphs['Aut(J3)'] = ([2, 3, 5, 17, 19], {(2, 3), (2, 5), (2, 17), (3, 5)})
graphs['McL'] = ([2, 3, 5, 7, 11], {(2, 3), (2, 5), (3, 5), (2, 7)})
graphs['Fi22'] = ([2, 3, 5, 7, 11, 13], {(2, 7), (3, 7), (2, 3), (2, 5), (2, 11), (3, 5)})
graphs['Aut(J2)'] = ([2, 3, 5, 7], {(2, 3), (2, 5), (3, 5), (2, 7)})
graphs['Aut(McL)'] = ([2, 3, 5, 7, 11], {(2, 7), (2, 3), (2, 5), (2, 11), (3, 5)})
graphs['Aut(HS)'] = ([2, 3, 5, 7, 11], {(2, 3), (2, 5), (3, 5), (2, 7)})
graphs['Aut(Suz)'] = ([2, 3, 5, 7, 11, 13], {(2, 7), (3, 7), (2, 3), (2, 5), (2, 11), (3, 5)})
graphs['L2(11)'] = ([2, 3, 5, 11], {(2, 3)})
graphs['M11'] = ([2, 3, 5, 11], {(2, 3)})
graphs['M12'] = ([2, 3, 5, 11], {(2, 3), (2, 5)})
graphs['U5(2)'] = ([2, 3, 5, 11], {(2, 3), (3, 5)})
graphs['A11'] = ([2, 3, 5, 7, 11], {(2, 7), (3, 7), (2, 3), (2, 5), (3, 5)})
graphs['HS'] = ([2, 3, 5, 7, 11], {(2, 3), (2, 5), (3, 5)})
graphs['A12'] = ([2, 3, 5, 7, 11], {(2, 7), (3, 7), (5, 7), (2, 3), (2, 5), (3, 5)})
graphs['U6(2)'] = ([2, 3, 5, 7, 11], {(2, 3), (2, 5), (3, 5)})
graphs['L2(19)'] = ([2, 3, 5, 19], {(2, 5)})
graphs['L2(29)'] = ([2, 3, 5, 7, 29], {(3, 5), (2, 7)})
graphs['L2(289)'] = ([2, 3, 5, 17, 29], {(2, 3), (5, 29)})
graphs['S4(17)'] = ([2, 3, 5, 17, 29], {(2, 3), (2, 17), (5, 29), (3, 17)})
graphs['Ru'] = ([2, 3, 5, 7, 13, 29], {(2, 7), (2, 13), (2, 3), (2, 5), (3, 5)})
graphs['L2(31)'] = ([2, 3, 5, 31], {(3, 5)})
graphs['L3(5)'] = ([2, 3, 5, 31], {(2, 3), (2, 5)})
graphs['L2(32)'] = ([2, 3, 11, 31], {(3, 11)})
graphs['L2(125)'] = ([2, 3, 5, 7, 31], {(2, 31), (3, 7)})
graphs['G2(5)'] = ([2, 3, 5, 7, 31], {(2, 3), (3, 7), (2, 5), (3, 5)})
graphs['L5(2)'] = ([2, 3, 5, 7, 31], {(2, 3), (3, 7), (3, 5), (2, 7)})
graphs['L6(2)'] = ([2, 3, 5, 7, 31], {(2, 7), (3, 7), (2, 3), (2, 5), (3, 5)})
