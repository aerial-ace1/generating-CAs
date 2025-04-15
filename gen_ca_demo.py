import random
import sys
from gen_ca_graph_helpers import gen_transitions, init_graph
from gen_ca_helper import to_bin
from gen_ca_predmap_new import gen_cycle_list, predmap_core
from gen_ca_rev_helper import nhood_3_symmetric
from gen_ca_rules_new import first_rule_table, last_rule_table, transition_rules

CA_LEN = 10


def gen_random_ca(steps, number=None, ca_class=None):
    """
    Function to Generate Random CA of given Length
    """
    if steps == CA_LEN:
        init_class = random.choice(list(first_rule_table.keys()))
        init_number = random.choice(list(first_rule_table[init_class]))
        return gen_random_ca(CA_LEN - 1, init_number, init_class)
    elif steps > 1:
        next_class = random.choice(list(transition_rules[ca_class].keys()))
        next_number = random.choice(list(transition_rules[ca_class][next_class]))
        return [number] + gen_random_ca(
            steps - 1,
            next_number,
            next_class,
        )

    next_class = random.choice(list(last_rule_table.keys()))
    next_number = random.choice(list(last_rule_table[next_class]))
    return [number, next_number]


def check_iso(ca_vals):
    """
    Function to Check if CA has Isomorphic form
    """
    ca_len = len(ca_vals)
    ca_vals_bin = [to_bin(int(val), 2 ** (ca_len - 1)) for val in ca_vals]
    states = 2**ca_len
    _, rev_edges, graph_dict = init_graph(states, ca_len)
    gen_transitions(states, ca_len, graph_dict, ca_vals_bin)
    rev_edges = [(v["next"], v["bin"]) for _, v in graph_dict.items()]

    truth, _ = nhood_3_symmetric(ca_vals, rev_edges, ca_len, False)
    return truth


if __name__ == "__main__":

    find_iso = False
    ca = None
    iso_ca = None
    while not find_iso:
        random_ca = gen_random_ca(CA_LEN)
        ca = random_ca
        try:
            iso_ca = predmap_core(ca)
        except KeyError:
            find_iso = False
            print(f"{random_ca} - {find_iso}")
            continue

        if "--check-iso-bin" in sys.argv:
            find_iso = check_iso(random_ca)
        else:
            find_iso = -1 not in iso_ca and None not in iso_ca
        print(f"{random_ca} - {find_iso}")

    print(f"\n{ca} - {iso_ca}\n")

    if "--check-cycles" in sys.argv:
        ca_cycle_list = gen_cycle_list(ca)
        iso_cycle_list = gen_cycle_list(iso_ca)
        if "--show-cycles" in sys.argv:
            print(f"CA Cycles - {ca_cycle_list}")
            print(f"Iso CA Cycles - {iso_cycle_list}")
        print(f"{ca_cycle_list == iso_cycle_list}")
