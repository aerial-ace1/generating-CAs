"""
Script to Generate a All CA of Neighbourhood 3
"""

import copy
from gen_ca_helper import to_bin
from gen_ca_rules import first_rule_table, last_rule_table, transition_rules


STEP = 2  # Arbitrary Number of Steps
list_of_ca = []


def gen_ca(num_list, ca_class, steps):
    """
    Generates the next step of the CA using transition rules
    """
    if steps > 1:
        for next_class, next_num_list in transition_rules[ca_class].items():
            for next_num in next_num_list:
                new_number_list = copy.deepcopy(num_list)
                new_number_list.append(next_num)
                gen_ca(new_number_list, next_class, steps - 1)
    else:
        for last_num in last_rule_table[ca_class]:
            last_number_list = copy.deepcopy(num_list)
            last_number_list.append(last_num)
            list_of_ca.append(last_number_list)


if __name__ == "__main__":
    for first_rule_ca_class, first_rule_ca_rules in first_rule_table.items():
        for rule in first_rule_ca_rules:
            gen_ca([rule], first_rule_ca_class, STEP)

    with open(f"all_steps/{STEP}", "w", encoding="utf-8") as file:
        for line in list_of_ca:
            file.write(f"{line}\n")
    with open(f"all_steps/{STEP}_bin", "w", encoding="utf-8") as file:
        for line in list_of_ca:
            file.write(",".join(to_bin(element) for element in line) + "\n")

