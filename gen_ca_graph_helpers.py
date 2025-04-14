"""
Script to store helper functions for Gen CA Graph Scripts
"""

import os
import matplotlib.pyplot as plt
import networkx as nx
from gen_ca_helper import to_bin, get_3_neighbourhood


def init_graph(states, ca_len=4):
    """
    Initialize the graph structures.

    Args:
    states (int): Total number of states.

    Returns:
    tuple: vertices (list), edges (list), graph_dict (dict) for the graph.
    """
    vertices = []
    edges = []
    graph_dict = {}

    for state in range(states):
        bin_repr = to_bin(state, ca_len)
        graph_dict[state] = {"visited": False, "next": False, "bin": bin_repr}
        vertices.append(bin_repr)

    return vertices, edges, graph_dict


def display_graph(vertices, edges, filename="transition_diagram.png"):
    """
    Generate and display the transition diagram graph with
    colors for connected components.

    Args:
    vertices (list): List of vertex labels (binary strings).
    edges (list): List of edges between the vertices.
    filename (str): Name of the output image file for the graph.

    Returns:
    None
    """
    g = nx.DiGraph()
    g.add_nodes_from(vertices)
    g.add_edges_from(edges)

    plt.figure(figsize=(10, 8))
    pos = nx.circular_layout(g)
    nx.draw(
        g,
        pos,
        with_labels=True,
        font_weight="bold",
        node_size=1500,
        node_color="black",
        edge_color="black",
        font_size=10,
        font_color="white",
        connectionstyle="arc3,rad=0.33",
    )
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()

    if os.name == "posix":
        os.system(f"xdg-open {filename}")
    elif os.name == "nt":
        os.system(f"start {filename}")
    else:
        print(f"Please open the image manually: {filename}")

    print(f"Graph saved and opened: {filename}")


def gen_transitions(states, ca_len, graph_dict, ca_vals_bin):
    """
    Generate transitions based on the given cellular automaton rules.

    Args:
    states (int): Total number of states.
    ca_len (int): Length of the cellular automaton.
    graph_dict (dict): Dictionary holding the state information.
    ca_vals_bin (list): List of binary values for the cellular automaton rules.

    Returns:
    None
    """
    state = 0
    while state < states:
        graph_dict[state]["visited"] = True
        next_state = ""
        for position in range(ca_len):
            lookup_index = int(get_3_neighbourhood(state, position, ca_len), 2)
            next_state += ca_vals_bin[position][-lookup_index - 1]
        graph_dict[state]["next"] = next_state
        state += 1
