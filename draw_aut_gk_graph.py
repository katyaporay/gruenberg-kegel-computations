# Example using Python and NetworkX (Conceptual)
import matplotlib.pyplot as plt
import networkx as nx
import os
from show_gk import draw_graph
import matplotlib
from math import gcd
from build_and_draw import build_and_draw

# Assume you have functions to get primes and element orders from your group software

# group_name = "Fi24"
# file_name = "test/Aut(" + group_name + ")"
# group_creation = f"L := SimpleGroup(\\\"{group_name}\\\");\nG := AutomorphismGroup(L);"
# build_and_draw(group_name, file_name, group_creation)

group_name = "ON"
file_name = "test/" + group_name
group_creation = f"G := SimpleGroup(\\\"{group_name}\\\");"
build_and_draw(group_name, file_name, group_creation)

# for group_name in ["L2(11)", "M11", "M12", "U5(2)", "M22", "A11", "McL", "HS", "A12", "U6(2)"]:
#     file_name = "cands/M22/" + group_name
#     group_creation = f"G := SimpleGroup(\\\"{group_name}\\\");"
#     build_and_draw(group_name, file_name, group_creation)

# for group_name in ["L2(19)", "J3"]:
#     file_name = "cands/J3/" + group_name
#     group_creation = f"G := SimpleGroup(\\\"{group_name}\\\");"
#     build_and_draw(group_name, file_name, group_creation)

# for group_name in ["L2(11)", "M11", "M12", "U5(2)", "M22", "A11", "McL", "HS", "A12", "U6(2)"]:
#     file_name = "cands/HS/" + group_name
#     group_creation = f"G := SimpleGroup(\\\"{group_name}\\\");"
#     build_and_draw(group_name, file_name, group_creation)

# for group_name in ["Sz(8)", "L2(64)", "U4(5)", "L3(9)", "S6(3)", "O7(3)", "G2(4)", "S4(8)", "O8+(3)", "L5(3)",
#                    "A13", "A14", "A15", "L6(3)", "Suz", "A16", "Fi22"]:
#     file_name = "cands/Suz/" + group_name
#     group_creation = f"G := SimpleGroup(\\\"{group_name}\\\");"
#     build_and_draw(group_name, file_name, group_creation)

# for group_name in ["U3(31)"]:
#     file_name = "cands/ON/" + group_name
#     group_creation = f"G := SimpleGroup(\\\"{group_name}\\\");"
#     build_and_draw(group_name, file_name, group_creation)

# for group_name in ["L2(29)", "L2(17^2)", "S4(17)", "Ru", "U4(17)"]:
#     file_name = "cands/Fi24'/" + group_name
#     group_creation = f"G := SimpleGroup(\\\"{group_name}\\\");"
#     build_and_draw(group_name, file_name, group_creation)