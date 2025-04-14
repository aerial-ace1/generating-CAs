"""
Rules to Generate a CA of Neighbourhood 3
"""

# Class of R(1) : Rules of R(0)
first_rule_table = {1: [3, 12], 2: [5, 10], 3: [6, 9]}

# Rule Class of R(n-1) : Rule Set of R(n-1)
last_rule_table = {
    1: [17, 20, 65, 68],
    2: [5, 20, 65, 80],
    3: [5, 17, 68, 80],
    5: [17, 68],
}

# Class of R(i) : { Class of R(i+1) : Ri}
transition_rules = {
    1: {
        1: [51, 204, 60, 195],
        2: [85, 170],
        3: [102, 105, 150, 153],
        5: [54, 57, 99, 108, 147, 156, 198, 201],
    },
    2: {
        1: [15, 60, 195, 240],
    },
    3: {
        1: [51, 204, 15, 240],
    },
    5: {
        1: [51, 204],
    },
}
