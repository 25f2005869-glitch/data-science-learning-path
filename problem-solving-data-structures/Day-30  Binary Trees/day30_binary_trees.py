# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Binary Trees
# Day         : 30
# Description : Creating a binary tree and performing
#               preorder traversal.
# ==========================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
root = Node("A")

root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")

root.right.left = Node("F")
root.right.right = Node("G")


# Preorder Traversal
def preorder(node):

    if node is not None:

        print(node.data, end=" ")

        preorder(node.left)

        preorder(node.right)


print("Preorder Traversal:")

preorder(root)