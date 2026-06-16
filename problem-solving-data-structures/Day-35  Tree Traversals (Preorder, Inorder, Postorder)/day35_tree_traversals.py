# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Tree Traversals
# Day         : 35
# Description : Preorder, Inorder and Postorder Traversals
#               of a Binary Tree.
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

    if node:

        print(node.data, end=" ")

        preorder(node.left)

        preorder(node.right)


# Inorder Traversal
def inorder(node):

    if node:

        inorder(node.left)

        print(node.data, end=" ")

        inorder(node.right)


# Postorder Traversal
def postorder(node):

    if node:

        postorder(node.left)

        postorder(node.right)

        print(node.data, end=" ")


print("Preorder Traversal:")
preorder(root)

print("\n")

print("Inorder Traversal:")
inorder(root)

print("\n")

print("Postorder Traversal:")
postorder(root)