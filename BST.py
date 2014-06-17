from Node import Node

class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, root, t_node):
        if self.root is None:
            self.root = t_node
        else:

            if root.data > t_node.data:
                if root.left is None:
                    print "insert left"
                    root.left = t_node
                else:
                    self.insert(root.left, t_node)
            else:
                if root.right is None:
                    print "insert right"
                    root.right = t_node
                else:
                    self.insert(root.right, t_node)

    def print_BST(self, t_node):
        if not t_node:
            return 
        
        print str(t_node.data) + '\n'
        self.print_BST(t_node.left)
        self.print_BST(t_node.right)

