"""
Script to store helper functions for Gen CA Scripts
"""


def to_bin(number, bits=8):
    """
    Converts a number to its 8 digit binary
    """
    return format(number, f"0{bits}b")


def get_3_neighbourhood(number, position, bits=8):
    """
    Extracts 3 neighbourhood at a given position from the binary
    representation of a number
    """
    binary_repr = to_bin(number, bits)
    if position == 0:
        return "0" + binary_repr[0:2]
    if position == bits - 1:
        offset = bits - 2
        return binary_repr[offset:] + "0"
    l_offset = position - 1
    r_offset = position + 2
    return binary_repr[l_offset:r_offset]


def get_4_neighbourhood(number, position, offset=0, bits=4):
    """
    Extracts 4 neighbourhood at a given position from the binary
    representation of a number
    """
    binary_repr = to_bin(number, bits)
    return (
        "0" * (bits - 1 - position - offset)
        + binary_repr[: position + 2 + offset]
        + "0" * (position - bits + 1 + offset)
    )[-4:]


def transition_table(ca_vals):
    """
    Generate transition table
    """
    print("Present State \t111\t110\t101\t100\t011\t010\t001\t000\tRule")
    for index, element in enumerate(ca_vals):
        formatted_bin_element = "\t".join(list(to_bin(int(element))))
        print(f"({index+1})Next state\t", formatted_bin_element, "\t", element)
