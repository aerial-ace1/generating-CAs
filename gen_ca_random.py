"""
Script to Generate a Random CA of Neighbourhood 3
"""

import random
from gen_ca_helper import get_3_neighbourhood
from gen_ca_rules import first_rule_table, last_rule_table, transition_rules


def gen_ca_random(number, ca_class, steps):
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
        gen_ca_random(next_number, next_class, steps - 1)
    else:
        next_class = random.choice(list(last_rule_table.keys()))
        next_number = random.choice(list(last_rule_table[next_class]))
        print("\t".join(list(format(next_number, "08b"))), end="\t")
        print("\t\t", next_number)


if __name__ == "__main__":
    init_class = random.choice(list(first_rule_table.keys()))
    init_number = random.choice(list(first_rule_table[init_class]))
    gen_ca_random(init_number, init_class, random.randint(3, 5))
