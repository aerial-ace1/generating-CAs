"""
Script to store helper functions for Gen CA Graph Scripts
"""

import matplotlib.pyplot as plt
import networkx as nx
from gen_ca_helper import to_bin, get_3_neighbourhood


def init_graph(states):
    """
    Init the structures for a graph
    """
    vertices = []
    edges = []
    graph_dict = {}
    for state in range(states):
        bin_repr = to_bin(state, 4)
        graph_dict[state] = {"visited": False, "next": False, "bin": bin_repr}
        vertices.append(bin_repr)
    return vertices, edges, graph_dict


def display_graph(vertices, edges):
    """
    Generate graph for transition diagram
    """
    g = nx.DiGraph()
    g.add_nodes_from(vertices)
    g.add_edges_from(edges)
    nx.draw_kamada_kawai(g, with_labels=True, font_weight="bold")
    plt.show()


def gen_transitions(states, ca_len, graph_dict, ca_vals_bin):
    """
    Generate transition from rules
    """
    state = 0
    while state < states:
        if graph_dict[state]["visited"]:
            state += 1
        else:
            graph_dict[state]["visited"] = True
            next_state = ""
            for position in range(ca_len):
                lookup_index = int(get_3_neighbourhood(state, position, 4), 2)
                next_state += ca_vals_bin[position][-lookup_index - 1]
            graph_dict[state]["next"] = next_state
            state = int(next_state, 2)
