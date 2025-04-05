"""
Helper functions to generate the reverse transition diagram for Gen CA
"""

from gen_ca_helper import (
    get_3_neighbourhood,
    get_4_neighbourhood,
    rev_transition_table,
    rev_transition_table_3,
    custom_checker_4,
    custom_checker_3,
)


def nhood_4_symmetric(ca, rev_edges, ca_len, find_num=True):
    """
    Function to generate symmetric neighbourhood in 4
    """
    logs = []
    new_ca_vals_bin = []
    new_ca = []
    solved = False
    conflict = False
    offset_list = [0] * ca_len
    logs.append(f"CA: {ca}")
    for offset in range(4):
        offset_list = [offset] * ca_len
        logs.append(f"Offset : {offset}")
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
                    logs.append(
                        f"Conflict: Position: {pos}: "
                        f"{parent}:{child}: "
                        f": Existing: {new_ca_vals_bin[pos][-nhood_value - 1]}"
                    )
                    break
                logs.append(f"Updated: Position: {pos}: " f"{parent}:{child}")
                new_ca_vals_bin[pos][-nhood_value - 1] = child[pos]
            if conflict:
                break
        for check in range(4):
            if not custom_checker_4(new_ca_vals_bin[check], offset, check):
                logs.append(f"Unfilled for {check} with offset {offset}")
                continue
        if not conflict:
            solved = True

    if solved or (not find_num):
        result, new_ca = rev_transition_table(new_ca_vals_bin, offset_list, find_num)
        result = [f"CA: {ca} : 4"] + result
        write_lines_to_file(result, "result.txt")
    write_lines_to_file(logs, "logs.txt")
    return solved, new_ca


def nhood_4_asymmetric(ca, rev_edges, find_num=True):
    """
    Function to generate asymmetric neighbourhood in 4
    """
    logs = []
    new_ca = []
    new_ca_vals_bin = []
    offset_list = []
    solved = False
    conflict = False
    logs.append(f"CA: {ca}")
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
                    logs.append(
                        f"Conflict: Position: {iter_pos}: Offset: {offset}: "
                        f"{parent}:{child}: "
                        f": Existing: {new_ca_vals_bin_row[-nhood_value - 1]}"
                    )
                    break
                logs.append(f"Updated: Position: {iter_pos}: " f"{parent}:{child}")
                new_ca_vals_bin_row[-nhood_value - 1] = child[iter_pos]
            if not custom_checker_4(new_ca_vals_bin_row, offset, iter_pos):
                logs.append(f"Unfilled for {iter_pos} with offset {offset}")
            elif not conflict:
                new_ca_vals_bin.append(new_ca_vals_bin_row)
                logs.append(f"Solved for {iter_pos} with offset {offset}")
                offset_list.append(offset)
                solved = True
                break
        if not solved:
            logs.append("No valid rule set!")
            logs.append(f"Unsolved for {iter_pos}")
            break

    if solved or (not find_num):
        result, new_ca = rev_transition_table(new_ca_vals_bin, offset_list, find_num)
        result = [f"CA: {ca} : 4a"] + result
        write_lines_to_file(result, "result.txt")
    write_lines_to_file(logs, "logs.txt")
    return solved, new_ca


def nhood_3_symmetric(ca, rev_edges, ca_len, find_num=True):
    """
    Function to generate symmetric neighbourhood in 4
    """
    logs = []
    new_ca = []
    new_ca_vals_bin = []
    solved = False
    conflict = False
    logs.append(f"CA: {ca}")
    conflict = False
    new_ca_vals_bin = [["2"] * (2**(ca_len-1)) for _ in range(ca_len)]
    for parent, child in rev_edges:
        for pos in range(ca_len):
            nhood = get_3_neighbourhood(int(parent, 2), pos, 4)
            nhood_value = int(nhood, 2)
            if new_ca_vals_bin[pos][-nhood_value - 1] not in [
                child[pos],
                "2",
            ]:
                conflict = True
                logs.append(
                    f"Conflict: Position: {pos}: "
                    f"{parent}:{child}: "
                    f": Existing: {new_ca_vals_bin[pos][-nhood_value - 1]}"
                )
                break
            logs.append(f"Updated: Position: {pos}: " f"{parent}:{child}")
            new_ca_vals_bin[pos][-nhood_value - 1] = child[pos]
        if conflict:
            break
    for check in range(4):
        if not custom_checker_3(new_ca_vals_bin[check], check):
            logs.append(f"Unfilled for {check}")
            conflict = True
            break
    if not conflict:
        solved = True

    if solved or (not find_num):
        result, new_ca = rev_transition_table_3(new_ca_vals_bin, False)
        result = [f"CA: {ca} : 3"] + result
        write_lines_to_file(result, "result.txt")
    write_lines_to_file(logs, "logs.txt")
    return solved, new_ca


def write_lines_to_file(lines, filename):
    """Write lines to file"""
    with open(filename, "a", encoding="utf-8") as file:
        file.writelines(f"{line}\n" for line in lines)
