# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Binary Search Trees (BST)
# Day         : 31
# Description : Creating a BST and performing inorder
#               traversal.
# ==========================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


def insert(root, value):

    if root is None:

        return Node(value)

    if value < root.data:

        root.left = insert(root.left, value)

    else:

        root.right = insert(root.right, value)

    return root


def inorder(root):

    if root is not None:

        inorder(root.left)

        print(root.data, end=" ")

        inorder(root.right)


# Create BST
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:

    root = insert(root, value)

print("Inorder Traversal:")

inorder(root)