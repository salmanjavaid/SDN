"""
Binary Search Tree class to be used in Data Center architecture
Right now basic skeleton. It uses Node class from Node.py

"""


from Node import Node

class BST:
    # constructor for BST
    def __init__(self, root=None):
        self.root = root

    # insert for BST
    # The initial arguments are the root of tree, and node to be added
    def insert(self, root, t_node):
        if self.root is None:
            self.root = t_node
        else:
            if root.data > t_node.data:
                if root.left is None:
                    root.left = t_node
                else:
                    self.insert(root.left, t_node)
            else:
                if root.right is None:
                    root.right = t_node
                else:
                    self.insert(root.right, t_node)

    # print the BST
    def print_BST(self, t_node):
        if not t_node:
            return 
        print str(t_node.data) + '\n'
        self.print_BST(t_node.left)
        self.print_BST(t_node.right)

