"""
main class for testing BST

"""

from Node import Node
from BST import BST

def demo():

    
    B = Node(50)
    tree = BST()

    tree.insert(tree.root, Node(50))
    tree.insert(tree.root, Node(48))
    tree.insert(tree.root, Node(52))
    tree.print_BST(tree.root)


if __name__ == "__main__":

    demo()
