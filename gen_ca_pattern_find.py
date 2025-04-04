import networkx as nx

from gen_ca_graph_helpers import gen_transitions, init_graph
from gen_ca_helper import to_bin


def find_pattern():
    """
    Func to find pattern
    """
    filename = "file.txt"
    overall_list = {}
    ca_dict = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            # ca = line.strip()[1:-1].split(",")
            # ca = [int(x) for x in ca]
            ca = line.strip().split(":")[1].strip()[1:-1].split(",")
            ca = [int(x.replace("'", "")) for x in ca]
            iso_ca = line.strip().split(":")[4].strip()[1:-1].split(",")
            iso_ca = [int(x.replace("'", "")) for x in iso_ca]

            ca_vals = ca
            ca_len = len(ca_vals)
            ca_vals_bin = [to_bin(int(val)) for val in ca_vals]
            states = 2**ca_len
            vertices, edges, graph_dict = init_graph(states)
            gen_transitions(states, ca_len, graph_dict, ca_vals_bin)
            edges = [(value["bin"], value["next"]) for _, value in graph_dict.items()]
            g = nx.DiGraph()
            g.add_nodes_from(vertices)
            g.add_edges_from(edges)
            cycle_list = []
            for cycle in nx.simple_cycles(g):
                cycle_list.append(len(cycle))
            cycle_list.sort()
            # if len(cycle_list) == 14:
            #     print(f"{ca} : {iso_ca}")
            if len(cycle_list) in overall_list.keys():
                if str(cycle_list) in overall_list[len(cycle_list)]:
                    overall_list[len(cycle_list)][str(cycle_list)] += 1
                    ca_dict[len(cycle_list)][str(cycle_list)].append((ca, iso_ca))
                else:
                    overall_list[len(cycle_list)][str(cycle_list)] = 1
                    ca_dict[len(cycle_list)][str(cycle_list)] = [(ca, iso_ca)]
            else:
                overall_list[len(cycle_list)] = {str(cycle_list): 1}
                ca_dict[len(cycle_list)] = {str(cycle_list): [(ca, iso_ca)]}
    print(overall_list)
    print(ca_dict[16])


if __name__ == "__main__":
    find_pattern()
