# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Trees
# Day         : 29
# Description : Creating a simple tree structure using nodes.
# ==========================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


# Creating Nodes
root = Node("A")

root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")

root.right.left = Node("F")
root.right.right = Node("G")


print("Root Node:", root.data)

print("Left Child of Root:", root.left.data)

print("Right Child of Root:", root.right.data)