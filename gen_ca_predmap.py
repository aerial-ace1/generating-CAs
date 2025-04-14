import networkx as nx
from gen_ca_graph_helpers import init_graph, gen_transitions
from gen_ca_helper import to_bin

pred = [-1, -1, -1, -1]

def first_pos(arr):
    if arr[0] == 3:
        pred[3] = 3

    elif arr[0] == 12:
        pred[3] = 12

    elif arr[0] == 6:
        if arr[1] == 51:
            pred[3] = 9
        elif arr[1] == 204:
            pred[3] = 6
        elif arr[1] == 15:
            pred[3] = 5
        elif arr[1] == 240:
            pred[3] = 10

    elif arr[0] == 9:
        if arr[1] == 51:
            pred[3] = 6
        elif arr[1] == 204:
            pred[3] = 9
        elif arr[1] == 15:
            pred[3] = 5
        elif arr[1] == 240:
            pred[3] = 10

    elif arr[0] == 5:
        if arr[1] == 60:
            pred[3] = 9
        elif arr[1] == 195:
            pred[3] = 6
        elif arr[1] == 15:
            pred[3] = 5
        elif arr[1] == 240:
            pred[3] = 10

    elif arr[0] == 10:
        if arr[1] == 60:
            pred[3] = 6
        elif arr[1] == 195:
            pred[3] = 9
        elif arr[1] == 15:
            pred[3] = 5
        elif arr[1] == 240:
            pred[3] = 10

def second_pos(arr):
    first, second, third = arr[0], arr[1], arr[2]

    if second in (17, 51, 68, 204):
        pred[0] = second

    elif second == 85:
        pred[1] = 15
        pred[0] = {15: 85, 60: 153, 195: 102, 240: 170}.get(third, -1)

    elif second == 102:
        mapping = {51: (153, 51), 204: (102, 204), 15: (85, 195), 240: (170, 60)}
        pred[0], pred[1] = mapping.get(third, (-1, -1))

    elif second == 153:
        mapping = {51: (102, 51), 204: (153, 204), 15: (85, 60), 240: (170, 195)}
        pred[0], pred[1] = mapping.get(third, (-1, -1))

    elif second == 170:
        pred[1] = 240
        pred[0] = {15: 85, 60: 102, 195: 153, 240: 170}.get(third, -1)

    elif second == 15:
        pred[0] = {10: 240, 5: 15, 6: 195, 9: 60}.get(first, -1)

    elif second in (99, 54, 57, 147):
        map_3 = {
            99: {51: (57, 51), 204: (54, 204)},
            54: {51: (147, 51), 204: (99, 204)},
            57: {51: (99, 51), 204: (147, 204)},
            147: {51: (54, 51), 204: (57, 204)}
        }
        map_12 = {
            99: {51: (147, 51), 204: (99, 204)},
            54: {51: (57, 51), 204: (54, 204)},
            57: {51: (54, 51), 204: (57, 204)},
            147: {51: (99, 51), 204: (147, 204)}
        }
        if first == 3:
            pred[0], pred[1] = map_3[second].get(third, (-1, -1))
        elif first == 12:
            pred[0], pred[1] = map_12[second].get(third, (-1, -1))

    elif second in (60, 195):
        pred[0] = {3: 195 if second == 60 else 60, 12: 60 if second == 60 else 195, 5: 15, 10: 240}.get(first, -1)

    elif second in (150, 156, 198, 201, 105, 108):
        mapping = {
            150: {3: {51: (150, 51), 204: (105, 204)}, 12: {51: (105, 51), 204: (150, 204)}},
            156: {3: {51: (198, 51), 204: (201, 204)}, 12: {51: (108, 51), 204: (156, 204)}},
            198: {3: {51: (156, 51), 204: (108, 204)}, 12: {51: (201, 51), 204: (198, 204)}},
            201: {3: {51: (108, 51), 204: (156, 204)}, 12: {51: (198, 51), 204: (201, 204)}},
            105: {3: {51: (105, 51), 204: (150, 204)}, 12: {51: (150, 51), 204: (105, 204)}},
            108: {3: {51: (201, 51), 204: (198, 204)}, 12: {51: (156, 51), 204: (108, 204)}}
        }
        pred[0], pred[1] = mapping[second][first].get(third, (-1, -1))

    elif second == 240:
        pred[0] = {5: 15, 10: 240, 6: 60, 9: 195}.get(first, -1)

def third_pos(arr):
    second, third, fourth = arr[1], arr[2], arr[3]

    if third in (17, 51, 68, 204):
        pred[1] = third

    elif third == 85:
        pred[2] = 5
        pred[1] = {5: 85, 20: 153, 65: 102, 80: 170}.get(fourth, -1)

    elif third == 102:
        mapping = {5: (85, 65), 17: (153, 17), 68: (102, 68), 80: (170, 20)}
        pred[1], pred[2] = mapping.get(fourth, (-1, -1))

    elif third == 153:
        mapping = {5: (85, 20), 17: (102, 17), 68: (153, 68), 80: (170, 65)}
        pred[1], pred[2] = mapping.get(fourth, (-1, -1))

    elif third == 170:
        pred[2] = 80
        pred[1] = {5: 85, 20: 102, 65: 153, 80: 170}.get(fourth, -1)

    elif third in (99, 54, 57, 147):
        map_51 = {
            99: {17: (57, 17), 68: (54, 68)},
            54: {17: (147, 17), 68: (99, 68)},
            57: {17: (99, 17), 68: (147, 68)},
            147: {17: (54, 17), 68: (57, 68)}
        }
        map_204 = {
            99: {17: (147, 17), 68: (99, 68)},
            54: {17: (57, 17), 68: (54, 68)},
            57: {17: (54, 17), 68: (57, 68)},
            147: {17: (99, 17), 68: (147, 68)}
        }
        if second == 51:
            pred[1], pred[2] = map_51[third].get(fourth, (-1, -1))
        elif second == 204:
            pred[1], pred[2] = map_204[third].get(fourth, (-1, -1))

    elif third in (60, 195):
        pred[1] = {51: 195 if third == 60 else 60, 204: 60 if third == 60 else 195,
                   170: 240, 85: 15}.get(second, -1)

    elif third in (150, 156, 198, 201, 105, 108):
        mapping = {
            150: {51: {17: (150, 17), 68: (105, 68)}, 204: {17: (105, 17), 68: (150, 68)}},
            156: {51: {17: (198, 17), 68: (201, 68)}, 204: {17: (108, 17), 68: (156, 68)}},
            198: {51: {17: (156, 17), 68: (108, 68)}, 204: {17: (201, 17), 68: (198, 68)}},
            201: {51: {17: (108, 17), 68: (156, 68)}, 204: {17: (198, 17), 68: (201, 68)}},
            105: {51: {17: (105, 17), 68: (150, 68)}, 204: {17: (150, 17), 68: (105, 68)}},
            108: {51: {17: (201, 17), 68: (198, 68)}, 204: {17: (156, 17), 68: (108, 68)}}
        }
        pred[1], pred[2] = mapping[third][second].get(fourth, (-1, -1))

    elif third == 240:
        pred[1] = {85: 15, 170: 240, 60: 60, 195: 195}.get(second, -1)

def last_pos(arr):
    if arr[3] in [17,68]:
        pred[2]=arr[3]

    elif arr[2] == 51 and arr[3] in [20,65]:
        if arr[3]==20:
            pred[2]=65
        else:
            pred[2]=20

    elif arr[2] ==204 and arr[3] in [20,65]:
        pred[2]=arr[3]

    elif arr[2]==85:
        pred[2]=5
    
    elif arr[2]==170:
        pred[2]=80
    
    elif arr[2]==102 and arr[3]==5:
        pred[2]=65

    elif arr[2]==153 and arr[3]==5:
        pred[2]=20

    elif arr[2]==102 and arr[3]==80:
        pred[2]=20

    elif arr[2]==153 and arr[3]==80:
        pred[2]=65 
     


def gen_cycle_list(ca_vals):
    ca_len = len(ca_vals)
    ca_vals_bin = [to_bin(int(val), 2**(ca_len - 1)) for val in ca_vals]
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

filename = "file.txt"
count=0
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        count += 1
        print("\r", str(count), end="")
        pred=[-1,-1,-1,-1]
        ca = line.strip().split(":")[1].strip()[1:-1].split(",")
        ca = [int(x.replace("'", "")) for x in ca]
        first_pos(ca)
        second_pos(ca)
        third_pos(ca)
        last_pos(ca)
        iso_ca = line.strip().split(":")[4].strip()[1:-1].split(",")
        iso_ca = [int(x.replace("'", "")) for x in iso_ca]
        new_pred = [pred[3], pred[0], pred[1], pred[2]]
        c1=gen_cycle_list(ca)
        c2=gen_cycle_list(new_pred)

        with open(f"4len_predmap", "a", encoding="utf-8") as file:
            file.write(f"{ca} - {new_pred}\t{c1==c2} - {c1} - {c2}\n")
           






