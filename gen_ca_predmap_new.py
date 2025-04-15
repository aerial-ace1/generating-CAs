import networkx as nx
from gen_ca_graph_helpers import init_graph, gen_transitions
from gen_ca_helper import to_bin


def first_pos(arr):
    if arr[0] == 3:
        return 3

    elif arr[0] == 12:
        return 12

    elif arr[0] == 6:
        if arr[1] == 51:
            return 9
        elif arr[1] == 204:
            return 6
        elif arr[1] == 15:
            return 5
        elif arr[1] == 240:
            return 10

    elif arr[0] == 9:
        if arr[1] == 51:
            return 6
        elif arr[1] == 204:
            return 9
        elif arr[1] == 15:
            return 5
        elif arr[1] == 240:
            return 10

    elif arr[0] == 5:
        if arr[1] == 60:
            return 9
        elif arr[1] == 195:
            return 6
        elif arr[1] == 15:
            return 5
        elif arr[1] == 240:
            return 10

    elif arr[0] == 10:
        if arr[1] == 60:
            return 6
        elif arr[1] == 195:
            return 9
        elif arr[1] == 15:
            return 5
        elif arr[1] == 240:
            return 10


def second_pos(arr, pred):
    first, second, third = arr[0], arr[1], arr[2]

    if second in (17, 51, 68, 204):
        pred[0] = second

    elif second == 85:
        pred[0] = {15: 85, 60: 153, 195: 102, 240: 170}.get(third, -1)
        pred.append(15)

    elif second == 102:
        pred.append(None)
        mapping = {51: (153, 51), 204: (102, 204), 15: (85, 195), 240: (170, 60)}
        pred[0], pred[1] = mapping.get(third, (-1, -1))

    elif second == 153:
        pred.append(None)
        mapping = {51: (102, 51), 204: (153, 204), 15: (85, 60), 240: (170, 195)}
        pred[0], pred[1] = mapping.get(third, (-1, -1))

    elif second == 170:
        pred[0] = {15: 85, 60: 102, 195: 153, 240: 170}.get(third, -1)
        pred.append(240)

    elif second == 15:
        pred[0] = {10: 240, 5: 15, 6: 195, 9: 60}.get(first, -1)

    elif second in (99, 54, 57, 147):
        pred.append(None)
        map_3 = {
            99: {51: (57, 51), 204: (54, 204)},
            54: {51: (147, 51), 204: (99, 204)},
            57: {51: (99, 51), 204: (147, 204)},
            147: {51: (54, 51), 204: (57, 204)},
        }
        map_12 = {
            99: {51: (147, 51), 204: (99, 204)},
            54: {51: (57, 51), 204: (54, 204)},
            57: {51: (54, 51), 204: (57, 204)},
            147: {51: (99, 51), 204: (147, 204)},
        }
        if first == 3:
            pred[0], pred[1] = map_3[second].get(third, (-1, -1))
        elif first == 12:
            pred[0], pred[1] = map_12[second].get(third, (-1, -1))

    elif second in (60, 195):
        pred[0] = {
            3: 195 if second == 60 else 60,
            12: 60 if second == 60 else 195,
            5: 15,
            10: 240,
        }.get(first, -1)

    elif second in (150, 156, 198, 201, 105, 108):
        pred.append(None)
        mapping = {
            150: {
                3: {51: (150, 51), 204: (105, 204)},
                12: {51: (105, 51), 204: (150, 204)},
            },
            156: {
                3: {51: (198, 51), 204: (201, 204)},
                12: {51: (108, 51), 204: (156, 204)},
            },
            198: {
                3: {51: (156, 51), 204: (108, 204)},
                12: {51: (201, 51), 204: (198, 204)},
            },
            201: {
                3: {51: (108, 51), 204: (156, 204)},
                12: {51: (198, 51), 204: (201, 204)},
            },
            105: {
                3: {51: (105, 51), 204: (150, 204)},
                12: {51: (150, 51), 204: (105, 204)},
            },
            108: {
                3: {51: (201, 51), 204: (198, 204)},
                12: {51: (156, 51), 204: (108, 204)},
            },
        }
        pred[0], pred[1] = mapping[second][first].get(third, (-1, -1))

    elif second == 240:
        pred[0] = {5: 15, 10: 240, 6: 60, 9: 195}.get(first, -1)

    return pred


def predict_isomorphic_rule(arr, i):
    prev_rule = arr[i - 1]
    curr_rule = arr[i]
    next_rule = arr[i + 1]

    pred1 = [
        -1,
        -1,
    ]  # first -> current rule mapping, second -> neighbor rule mapping if needed

    if curr_rule in (17, 51, 68, 204):
        pred1[0] = curr_rule
        return [pred1[0]]

    elif curr_rule == 85:
        pred1[0] = {
            5: 85,
            15: 85,
            20: 153,
            60: 153,
            65: 102,
            80: 170,
            195: 102,
            240: 170,
        }.get(next_rule, -1)

    elif curr_rule == 102:
        mapping = {
            5: 85,
            15: 85,
            17: 153,
            51: 153,
            68: 102,
            80: 170,
            204: 102,
            240: 170,
        }
        pred1[0] = mapping.get(next_rule, -1)

    elif curr_rule == 153:
        mapping = {
            5: 85,
            15: 85,
            17: 102,
            51: 102,
            68: 153,
            80: 170,
            204: 153,
            240: 170,
        }
        pred1[0] = mapping.get(next_rule, -1)

    elif curr_rule == 170:
        pred1[0] = {
            5: 85,
            15: 85,
            20: 102,
            60: 102,
            65: 153,
            80: 170,
            195: 153,
            240: 170,
        }.get(next_rule, -1)

    elif curr_rule in (99, 54, 57, 147):
        map_51 = {
            99: {17: 57, 51: 57, 68: 54, 204: 54},
            54: {17: 147, 51: 147, 68: 99, 204: 99},
            57: {17: 99, 51: 99, 68: 147, 204: 147},
            147: {17: 54, 51: 54, 68: 57, 204: 57},
        }
        map_204 = {
            99: {17: 147, 51: 147, 68: 99, 204: 99},
            54: {17: 57, 51: 57, 68: 54, 204: 54},
            57: {17: 54, 51: 54, 68: 57, 204: 57},
            147: {17: 99, 51: 99, 68: 147, 204: 147},
        }
        if prev_rule == 51:
            pred1[0] = map_51[curr_rule].get(next_rule, -1)
        elif prev_rule == 204:
            pred1[0] = map_204[curr_rule].get(next_rule, -1)

    elif curr_rule in (60, 195):
        pred1[0] = {
            51: 195 if curr_rule == 60 else 60,
            204: 60 if curr_rule == 60 else 195,
            170: 240,
            85: 15,
        }.get(prev_rule, -1)

    elif curr_rule in (150, 156, 198, 201, 105, 108):
        mapping = {
            150: {
                51: {17: 150, 68: 105, 51: 150, 204: 105},
                204: {17: 105, 51: 105, 204: 150, 68: 150},
            },
            156: {
                51: {17: 198, 51: 198, 204: 201, 68: 201},
                204: {17: 108, 51: 108, 204: 156, 68: 156},
            },
            198: {
                51: {17: 156, 51: 156, 204: 108, 68: 108},
                204: {17: 201, 51: 201, 204: 198, 68: 198},
            },
            201: {
                51: {17: 108, 51: 108, 204: 156, 68: 156},
                204: {17: 198, 51: 198, 204: 201, 68: 201},
            },
            105: {
                51: {17: 105, 68: 150, 51: 105, 204: 150},
                204: {17: 150, 51: 150, 204: 105, 68: 105},
            },
            108: {
                51: {17: 201, 51: 201, 204: 198, 68: 198},
                204: {17: 156, 51: 156, 204: 108, 68: 108},
            },
        }
        pred1[0] = mapping[curr_rule][prev_rule].get(next_rule, -1)

    elif curr_rule == 240:
        pred1[0] = {85: 15, 170: 240, 102: 60, 153: 195, 60: 60, 195: 195}.get(
            prev_rule, -1
        )
    elif curr_rule == 15:
        pred1[0] = {85: 15, 170: 240, 102: 195, 153: 60}.get(prev_rule, -1)

    pred1.pop()
    return pred1


def last_pos(arr, n):
    if arr[n - 1] in [17, 68]:
        return arr[n - 1]

    elif arr[n - 2] == 51 and arr[n - 1] in [20, 65]:
        if arr[n - 1] == 20:
            return 65
        else:
            return 20

    elif arr[n - 2] == 204 and arr[n - 1] in [20, 65]:
        return arr[n - 1]

    elif arr[n - 2] == 85:
        return 5

    elif arr[n - 2] == 170:
        return 80

    elif arr[n - 2] == 102 and arr[n - 1] == 5:
        return 65

    elif arr[n - 2] == 153 and arr[n - 1] == 5:
        return 20

    elif arr[n - 2] == 102 and arr[n - 1] == 80:
        return 20

    elif arr[n - 2] == 153 and arr[n - 1] == 80:
        return 65


def gen_cycle_list(ca_vals):
    ca_len = len(ca_vals)
    ca_vals_bin = [to_bin(int(val), 2 ** (ca_len - 1)) for val in ca_vals]
    states = 2**ca_len
    vertices, rev_edges, graph_dict = init_graph(states, ca_len)
    gen_transitions(states, ca_len, graph_dict, ca_vals_bin)
    rev_edges = [(v["next"], v["bin"]) for _, v in graph_dict.items()]
    g = nx.DiGraph()
    g.add_nodes_from(vertices)
    g.add_edges_from(rev_edges)

    cycle_list = []
    for cycle in nx.simple_cycles(g):
        cycle_list.append(len(cycle))
    cycle_list.sort()
    return cycle_list


def predmap_core(ca):
    pred = [None]
    n = len(ca)
    pred = second_pos(ca, pred)
    i = len(pred) + 1
    while i < len(ca) - 1:
        initn = len(pred)
        pred.extend(predict_isomorphic_rule(ca, i))
        finaln = len(pred)
        i += finaln - initn

    if pred[len(pred) - 1] == -1:
        while pred[len(pred) - 1] == -1:
            pred.pop()
        pred.append(last_pos(ca, n))
    elif len(pred) == len(ca) - 1:
        pred.pop()
        pred.append(last_pos(ca, n))
    else:
        pred.append(last_pos(ca, n))
    new_pred = [first_pos(ca)] + pred
    return new_pred


if __name__ == "__main__":

    # filename = "runinng7.txt"
    filename = "temp.txt"
    # filename = "obs_new/4/output.txt"
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            count += 1
            print("\r", str(count), end="")
            ca = line.strip().split(":")[1].strip()[1:-1].split(",")
            ca = [int(x.replace("'", "")) for x in ca]
            n = len(ca)

            new_pred = predmap_core(ca)

            if len(ca) != len(new_pred):
                with open(f"{n}len_predmap_false", "a", encoding="utf-8") as file1:
                    file1.write(f"{ca} - {new_pred}\n")
            else:
                c1 = gen_cycle_list(ca)
                c2 = gen_cycle_list(new_pred)

                with open(f"{n}len_predmap_new", "a", encoding="utf-8") as file2:
                    file2.write(f"{ca} - {new_pred}\t{c1==c2} - {c1} - {c2}\n")
    print("\n")
