# ==========================================================
# Author      : Saloni Tiwari
# Topic       : BST Search Operation
# Day         : 32
# Description : Searching an element in a Binary Search Tree.
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


def search(root, key):

    if root is None:

        return False

    if root.data == key:

        return True

    if key < root.data:

        return search(root.left, key)

    return search(root.right, key)


# Create BST
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:

    root = insert(root, value)

# Search Element
target = int(input("Enter element to search: "))

if search(root, target):

    print("Element Found")

else:

    print("Element Not Found")