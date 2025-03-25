"""
Script to Find Patterns in Neighbourhood 3 CAs
"""


def find_pattern():
    """
    Func to find pattern
    """
    ca_set_0 = {}
    ca_set_1 = {}
    ca_set_2 = {}
    ca_set_3 = {}
    filename = "file.txt"
    ca_list = set()
    iso_ca_list = set()
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            ca = line.strip().split(":")[1].strip()[1:-1].split(",")
            ca = [int(x.replace("'", "")) for x in ca]
            iso_ca = line.strip().split(":")[4].strip()[1:-1].split(",")
            iso_ca = [int(x.replace("'", "")) for x in iso_ca]

            ca_list.update(ca)
            iso_ca_list.update(iso_ca)

            # bin_iso_ca_4 = list(format(iso_ca[3], f"0{8}b"))

            # bin_iso_ca_4[0] = "0"
            # bin_iso_ca_4[2] = "0"
            # bin_iso_ca_4[2] = "0"
            # bin_iso_ca_4[6] = "0"
            # bin_iso_ca_4 = "".join(bin_iso_ca_4)

            # print(iso_ca[3])
            # print(format(iso_ca[3], f"0{8}b"))
            # print(bin_iso_ca_4)
            # print(int(bin_iso_ca_4, 2))
            # iso_ca[3] = int(bin_iso_ca_4, 2)

            partial_ca_0 = str(ca[0:2])
            if partial_ca_0 in ca_set_0.keys():
                ca_set_0[partial_ca_0].add(iso_ca[0])
            else:
                ca_set_0[partial_ca_0] = set([iso_ca[0]])

            partial_ca_1 = str(ca[0:3])
            if partial_ca_1 in ca_set_1.keys():
                ca_set_1[partial_ca_1].add(iso_ca[1])
            else:
                ca_set_1[partial_ca_1] = set([iso_ca[1]])

            partial_ca_2 = str(ca[0:4])
            if partial_ca_2 in ca_set_2.keys():
                ca_set_2[partial_ca_2].add(iso_ca[2])
            else:
                ca_set_2[partial_ca_2] = set([iso_ca[2]])

            partial_ca_3 = str(ca[0:4])
            if partial_ca_3 in ca_set_3.keys():
                ca_set_3[partial_ca_3].add(iso_ca[3])
            else:
                ca_set_3[partial_ca_3] = set([iso_ca[3]])

    def find_0():
        skips_0 = []
        for key, values in ca_set_0.items():
            if key not in skips_0:
                middle = [int(key[1:-1].split(",")[1].strip())]
                for key_1, values_1 in ca_set_0.items():
                    if (
                        key_1 != key
                        and int(key[1:-1].split(",")[0].strip())
                        == int(key_1[1:-1].split(",")[0].strip())
                        and values == values_1
                    ):
                        skips_0.append(key_1)
                        middle.append(int(key_1[1:-1].split(",")[1].strip()))
                print(key[1:-1].split(",")[0], " : ", middle, " -> ", values)

    def find_1():
        skips_1 = []
        l_tups = []
        for key, values in ca_set_1.items():
            prefix_key = (
                f'{key[1:-1].split(",")[0].strip()}'
                + f':{key[1:-1].split(",")[1].strip()}'
            )
            # print(key, " : ", values)
            if key not in skips_1:
                middle = [int(key[1:-1].split(",")[2].strip())]
                for key_1, values_1 in ca_set_1.items():
                    prefix_key_1 = (
                        f'{key_1[1:-1].split(",")[0].strip()}'
                        f':{key_1[1:-1].split(",")[1].strip()}'
                    )
                    if (
                        key_1 != key
                        and prefix_key == prefix_key_1
                        and values == values_1
                    ):
                        skips_1.append(key_1)
                        middle.append(int(key_1[1:-1].split(",")[2].strip()))
                int_pk = [int(x) for x in prefix_key.split(":")]
                # print(
                #     int_pk, " : ", middle, "->", values
                # )
                l_tups.append((int_pk, middle, values))
        print(len(l_tups))
        skips_2 = []
        iso_pr = {51: 204, 204: 51}
        count = 0
        for i, (a, b, c) in enumerate(l_tups):
            if i in skips_2:
                continue
            secs = [a[1]]
            altered_c = ""
            for j, (a1, b1, c1) in enumerate(l_tups):
                if i >= j or j in skips_2:
                    continue
                c_t = list(c)[0] in iso_pr.keys() and iso_pr[list(c)[0]] == list(c1)[0]

                if b == b1 and a[0] == a1[0] and (c == c1 or c_t):
                    if c_t:
                        secs.pop()
                        secs.append(f"{a[1]}/{a1[1]}")
                        altered_c = f"{list(c)[0]}/{list(c1)[0]}"
                    else:
                        secs.append(a1[1])
                    skips_2.append(j)
            if altered_c != "":
                print(a[0], " : ", secs, " : ", b, ": ", altered_c)
            else:
                print(a[0], " : ", secs, " : ", b, ": ", c)
            count += 1
        print(count)

    def find_2():
        skips_1 = []
        count = 0
        for key, values in ca_set_2.items():
            prefix_key = (
                f'{key[1:-1].split(",")[0].strip()}'
                + f':{key[1:-1].split(",")[1].strip()}'
                + f':{key[1:-1].split(",")[2].strip()}'
            )
            # print(key, " : ", values)
            if key not in skips_1:
                middle = [int(key[1:-1].split(",")[3].strip())]
                for key_1, values_1 in ca_set_2.items():
                    prefix_key_1 = (
                        f'{key_1[1:-1].split(",")[0].strip()}'
                        f':{key_1[1:-1].split(",")[1].strip()}'
                        f':{key_1[1:-1].split(",")[2].strip()}'
                    )
                    if (
                        key_1 != key
                        and prefix_key == prefix_key_1
                        and values == values_1
                    ):
                        skips_1.append(key_1)
                        middle.append(int(key_1[1:-1].split(",")[3].strip()))
                int_pk = [int(x) for x in prefix_key.split(":")]
                print(int_pk, " : ", middle, "->", values)
                count += 1
        print(count)

    find_0()
    # find_1()
    # find_2()
    # print(len(ca_list))
    # print(len(iso_ca_list))
    # print(ca_list - iso_ca_list)


if __name__ == "__main__":
    find_pattern()
