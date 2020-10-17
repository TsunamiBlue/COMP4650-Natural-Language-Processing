import json


class TreeNode:
    """
    Class for representing parse trees. Contains some useful utilities for printing and reading/writing to string.
    """
    def from_list(lst):
        root = TreeNode(lst[0])
        root.children = [TreeNode.from_list(ls) for ls in lst[1:]]
        return root

    def from_string(string):
        return TreeNode.from_list(json.loads(string))

    def __init__(self, val):
        self.val = val
        self.children = []

    def to_list(self):
        return [self.val] + [c.to_list() for c in self.children]

    def to_string(self):
        return json.dumps(self.to_list())

    def display(self):
        string = self.val + '\n'
        stack = self.children
        done = False
        while not done:
            done = True
            new_stack = []
            for c in stack:
                string += c.val + '\t'
                if len(c.children) == 0:
                    new_stack.append(TreeNode('\t'))
                else:
                    done = False
                    new_stack.extend(c.children)
            string += '\n'
            stack = new_stack
        return string


with open('train_x.txt', 'r') as f:
    x = [l.split() for l in f.readlines()]
    # Each element of x is a list of words (a sentence).

with open('train_y.txt', 'r') as f:
    y = [TreeNode.from_string(l) for l in f.readlines()]
    # Each element of y is a TreeNode object representing the syntax of the corresponding element of x


# TODO estimate the PCFG that generated (x, y) and print to output. Your output should be a list of rules along with
# their corresponding probabilities (e.g. [(A -> B, 0.9), (A -> C, 0.1), ...]
