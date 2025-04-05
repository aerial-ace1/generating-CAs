"""
Script to generate the transition diagram for Gen CA
"""

import sys
from gen_ca_graph_helpers import init_graph, display_graph, gen_transitions
from gen_ca_helper import to_bin, transition_table


def transition_diagram():
    """
    Parse and generate transition diagram
    """
    ca_vals = sys.argv[1:]
    ca_len = len(ca_vals)
    ca_vals_bin = [to_bin(int(val), 2**(ca_len-1)) for val in ca_vals]
    transition_table(ca_vals)
    states = 2**ca_len
    vertices, edges, graph_dict = init_graph(states, ca_len)
    gen_transitions(states, ca_len, graph_dict, ca_vals_bin)
    edges = [(value["bin"], value["next"]) for _, value in graph_dict.items()]
    display_graph(vertices, edges)


if __name__ == "__main__":
    transition_diagram()
