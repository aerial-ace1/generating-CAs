"""
Script to generate the reverse transition diagram for Gen CA
"""

import sys
from gen_ca_graph_helpers import init_graph, display_graph, gen_transitions
from gen_ca_helper import (
    to_bin,
    transition_table,
    get_4_neighbourhood,
    rev_transition_table,
)


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

    new_ca_vals_bin = []
    offset_list = []
    solved = False
    conflict = False
    for iter_pos in range(4):
        for offset in range(4):
            conflict = False
            new_ca_vals_bin_row = ["2"] * 16
            for parent, child in rev_edges:
                nhood = get_4_neighbourhood(int(parent, 2), iter_pos, offset)
                nhood_value = int(nhood, 2)
                if new_ca_vals_bin_row[-nhood_value - 1] not in [
                    child[iter_pos],
                    "2",
                ]:
                    conflict = True
                    print(
                        f"Conflict: Position: {iter_pos}: Offset: {offset}: "
                        f"{parent}:{child}: "
                        f": Existing: {new_ca_vals_bin_row[-nhood_value - 1]}"
                    )
                    break
                # print(f"Updated: Position: {iter_pos}: " f"{parent}:{child}")
                new_ca_vals_bin_row[-nhood_value - 1] = child[iter_pos]
            if not conflict:
                new_ca_vals_bin.append(new_ca_vals_bin_row)
                print(f"Solved for {iter_pos} with offset {offset}")
                offset_list.append(offset)
                solved = True
                break
        if not solved:
            print("No valid rule set!")
            print(f"Unsolved for {iter_pos} with offset {offset}")
            break

    rev_transition_table(new_ca_vals_bin, offset_list)


if __name__ == "__main__":
    transition_diagram()
