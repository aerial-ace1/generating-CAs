"""
Script to generate the reverse transition diagram for Gen CA
"""

import sys
from gen_ca_graph_helpers import init_graph, display_graph, gen_transitions
from gen_ca_helper import to_bin, transition_table, get_4_neighbourhood


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
    solved = False
    conflict = False
    for offset in range(4):
        print("Offset : ", offset)
        if solved:
            break
        conflict = False
        new_ca_vals_bin = [["2"] * 16 for _ in range(ca_len)]
        for parent, child in rev_edges:
            for pos in range(ca_len):
                nhood = get_4_neighbourhood(int(parent, 2), pos, offset)
                nhood_value = int(nhood, 2)
                if new_ca_vals_bin[pos][-nhood_value - 1] not in [
                    child[pos],
                    "2",
                ]:
                    conflict = True
                    print(
                        f"Conflict: Position: {pos}: "
                        f"{parent}:{child}: "
                        f": Existing: {new_ca_vals_bin[pos][-nhood_value - 1]}"
                    )
                    break
                print(f"Updated: Position: {pos}: " f"{parent}:{child}")
                new_ca_vals_bin[pos][-nhood_value - 1] = child[pos]
            if conflict:
                break
        if not conflict:
            solved = True

    print(new_ca_vals_bin)


if __name__ == "__main__":
    transition_diagram()

