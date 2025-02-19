"""
Script to generate the reverse transition diagram for Gen CA
"""

import sys
from gen_ca_graph_helpers import init_graph, display_graph, gen_transitions
from gen_ca_helper import to_bin, transition_table
from gen_ca_rev_helper import nhood_4_asymmetric


def transition_diagram():
    """
    Parse and generate transition diagram
    """
    ca_vals = sys.argv[1:]
    ca_len = len(ca_vals)
    ca_vals_bin = [to_bin(int(val)) for val in ca_vals]
    states = 2**ca_len

    transition_table(ca_vals)
    vertices, rev_edges, graph_dict = init_graph(states)
    gen_transitions(states, ca_len, graph_dict, ca_vals_bin)
    rev_edges = [(v["next"], v["bin"]) for _, v in graph_dict.items()]
    display_graph(vertices, rev_edges)

    nhood_4_asymmetric(ca_vals, rev_edges)


if __name__ == "__main__":
    transition_diagram()
