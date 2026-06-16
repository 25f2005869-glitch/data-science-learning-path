# ==========================================================
# Author      : Saloni Tiwari
# Topic       : BST Insertion Operation
# Day         : 33
# Description : Inserting nodes into a Binary Search Tree.
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

values = [50, 30, 70, 20, 40, 60]

for value in values:

    root = insert(root, value)

# Insert New Node
root = insert(root, 80)

print("Inorder Traversal:")

inorder(root)