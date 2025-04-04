"""
Script to generate the reverse transition diagram for Gen CA
"""

from gen_ca_graph_helpers import init_graph, gen_transitions
from gen_ca_helper import to_bin, transition_table
from gen_ca_rev_helper import nhood_3_symmetric, nhood_4_asymmetric, nhood_4_symmetric


def transition_diagram():
    """
    Parse and generate transition diagram
    """
    # filename = "temp.txt"
    filename = "all_steps/3"
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            ca_vals = line.strip()[1:-1].split(",")

            ca_len = len(ca_vals)
            # transition_table(ca_vals)
            ca_vals_bin = [to_bin(int(val), 2**(ca_len-1)) for val in ca_vals]
            states = 2**ca_len
            _, rev_edges, graph_dict = init_graph(states, ca_len)
            gen_transitions(states, ca_len, graph_dict, ca_vals_bin)
            rev_edges = [(v["next"], v["bin"]) for _, v in graph_dict.items()]

            solved = "000"
            result, new_ca = nhood_3_symmetric(ca_vals, rev_edges, ca_len, False)
            if result:
                solved = "100"
            else:
                result, new_ca = nhood_4_symmetric(ca_vals, rev_edges, ca_len, False)
                if result:
                    solved = "010"
                else:
                    result, new_ca = nhood_4_asymmetric(ca_vals, rev_edges, False)
                    if result:
                        solved = "001"
            with open("output.txt", "a", encoding="utf-8") as file:
                file.write(f"CA: {ca_vals} : {solved} : Isomorphic CA: {new_ca}\n")


if __name__ == "__main__":
    transition_diagram()
