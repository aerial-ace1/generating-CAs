import re
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.outputs = {}  # Dictionary to store corresponding outputs at each level

class RuleTrie:
    def __init__(self):
        self.tries = {}  # Dictionary of Tries { "w": TrieNode(), "w2": TrieNode(), ... }

    def insert(self, root_rule, rule_sequence, output_rule):
        """Insert (w, x, y, z) → (a, b, c, d) into the trie with 4 levels."""
        if root_rule not in self.tries:
            self.tries[root_rule] = TrieNode()  # Create a new Trie if missing

        node = self.tries[root_rule]  # Get the trie for this root_rule
        for level, (rule, output) in enumerate(zip(rule_sequence, output_rule)):
            if rule not in node.children:
                node.children[rule] = TrieNode()
            node = node.children[rule]
            node.outputs[level + 1] = output  # Store corresponding output at the correct level

    def display_trie(self, root_rule, node=None, depth=0):
        """Recursively print the trie structure with levels in a readable format."""
        if node is None:
            node = self.tries.get(root_rule, None)
            if node is None:
                print(f"No trie found for root {root_rule}\n")
                return

        for key, child in node.children.items():
            indent = "    " * depth
            output_str = ", ".join(f"Level {lvl}: {out}" for lvl, out in child.outputs.items())
            print(f"{indent}└── Node({key}) -> [ {output_str} ]")
            self.display_trie(root_rule, child, depth + 1)

    def display_all_tries(self):
        """Display tries for all unique root nodes."""
        for root in sorted(self.tries.keys()):
            print(f"\nTrie for Root Node {root}:\n" + "=" * 30)
            self.display_trie(root)

# Function to clean and parse the rules correctly
def clean_rule(rule):
    return re.sub(r"[^\d]", "", rule)  # Remove non-numeric characters

# Read the relations.txt file
file_path = "file.txt"  # Update this path if needed
with open(file_path, "r", encoding="utf-8") as file:
    file_contents = file.readlines()

# Initialize Trie
rule_trie = RuleTrie()

# Parse the file and insert rules into the trie
for line in file_contents:
    parts = line.strip().split(" : ")
    if len(parts) != 3:
        continue  # Skip malformed lines

    # Extract and clean rules
    input_part = parts[0].replace("CA: ", "").strip("[]").split(",")
    output_part = parts[2].replace("Isomorphic CA: ", "").strip("[]").split(",")

    # Clean each value by removing extra quotes and spaces
    input_rules = tuple(map(clean_rule, input_part))
    output_rules = tuple(map(clean_rule, output_part))

    # Insert into Trie (fixing root node as first element)
    root_rule, sequence = input_rules[0], input_rules
    rule_trie.insert(root_rule, sequence, output_rules)

rule_trie.display_all_tries()
