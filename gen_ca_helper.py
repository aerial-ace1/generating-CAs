"""
Script to store helper functions for Gen CA Scripts
"""


def to_bin(number):
    """
    Converts a number to its 8 digit binary
    """
    return format(number, "08b")


def get_3_neighbourhood(number, position):
    """
    Extracts 3 neighbourhood at a given position from the binary
    representation of a number
    """
    binary_repr = to_bin(number)
    if position == 0:
        return "0" + binary_repr[0:2]
    if position == 7:
        return binary_repr[6:] + "0"
    return binary_repr[position - 1: position + 2]


