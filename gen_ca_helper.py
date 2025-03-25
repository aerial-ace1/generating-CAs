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
    binary_repr = "0" * (bits - 1) + binary_repr + "0" * (bits - 1)
    return binary_repr[position + offset :][:bits]


def transition_table(ca_vals):
    """
    Generate transition table
    """
    print("Present State \t111\t110\t101\t100\t011\t010\t001\t000\tRule")
    for index, element in enumerate(ca_vals):
        f_bin_element = "\t".join(list(to_bin(int(element))))
        print(f"({index+1})Next state\t", f_bin_element, "\t", element)


def rev_transition_table(ca_vals, offset_list, find_num=True):
    """
    Generate transition table
    """
    logs = []
    ca = []
    logs.append(
        "Present State \t1111\t1110\t1101\t1100\t1011\t1010\t1001\t1000"
        "\t0111\t0110\t0101\t0100\t0011\t0010\t0001\t0000\tRule\tOffset"
    )
    for index, element in enumerate(ca_vals):
        f_bin_element = "\t".join(element)
        if find_num:
            f_num_element = int("".join(element), 2)
        else:
            bin_join = "".join(element)
            f_num_element = int(bin_join.replace("2", "0"), 2)
        ca.append(f_num_element)
        line = f"({index+1})Next state\t{f_bin_element}\t{f_num_element}\t{offset_list[index]}"
        logs.append(line)
    return logs, ca


def rev_transition_table_3(ca_vals, find_num=True):
    """
    Generate transition table
    """
    logs = []
    ca = []
    logs.append("Present State \t111\t110\t101\t100\t011\t010\t001\t000\tRule")
    for index, element in enumerate(ca_vals):
        f_bin_element = "\t".join(element)
        if find_num:
            f_num_element = int("".join(element), 2)
        else:
            bin_join = "".join(element)
            f_num_element = int(bin_join.replace("2", "0"), 2)
        ca.append(f_num_element)
        line = f"({index+1})Next state\t{f_bin_element}\t{f_num_element}"
        logs.append(line)
    return logs, ca


def custom_checker_4(ca_vals, offset, iter_pos):
    """
    Dont Care Checker for 4n
    """
    custom_bitset = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    ]
    scbs = custom_bitset[offset + iter_pos]
    for val, bit in zip(ca_vals, scbs):
        if bit == 0:
            if val not in ["0", "1"]:
                return False
        else:
            if val != "2":
                return False
    return True


def custom_checker_3(ca_vals, iter_pos):
    """
    Dont Care Checker for 3n
    """
    custom_bitset = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0],
    ]
    if iter_pos == 0:
        pick = 0
    elif iter_pos == 3:
        pick = 2
    else:
        pick = 1

    scbs = custom_bitset[pick]
    for val, bit in zip(ca_vals, scbs):
        if bit == 0:
            if val not in ["0", "1"]:
                return False
        else:
            if val != "2":
                return False
    return True
