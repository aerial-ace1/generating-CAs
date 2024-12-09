"""
Script to Generate a CA of Neighbourhood 3
"""

import random
from gen_ca_rules import first_rule_table, last_rule_table, transition_rules

# print(first_rule_table, last_rule_table, transition_rules)


def get_3_neighbourhood(number, position):
    """
    Extracts 3 neighbourhood at a given position from the binary
    representation of a number
    """
    binary_repr = format(number, "08b")
    if position == 0:
        return "0" + binary_repr[0:2]
    if position == 7:
        return binary_repr[6:] + "0"
    return binary_repr[position - 1: position + 2]


def gen_ca(number, ca_class, steps):
    """
    Generates the next step of the CA using transition rules
    """
    print("\t".join(list(format(number, "08b"))), end="\t")
    print("\t\t", number)
    for i in range(8):
        print(get_3_neighbourhood(number, i), end="\t")
    print()

    if steps > 1:
        next_class = random.choice(list(transition_rules[ca_class].keys()))
        next_number = random.choice(
            list(transition_rules[ca_class][next_class])
        )
        gen_ca(next_number, next_class, steps - 1)
    else:
        next_class = random.choice(list(last_rule_table.keys()))
        next_number = random.choice(list(last_rule_table[next_class]))
        print("\t".join(list(format(next_number, "08b"))), end="\t")
        print("\t\t", next_number)


if __name__ == "__main__":
    init_class = random.choice(list(first_rule_table.keys()))
    init_number = random.choice(list(first_rule_table[init_class]))
    gen_ca(init_number, init_class, random.randint(3, 5))
