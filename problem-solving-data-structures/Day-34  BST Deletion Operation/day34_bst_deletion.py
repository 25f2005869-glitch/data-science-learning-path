# ==========================================================
# Author      : Saloni Tiwari
# Topic       : BST Deletion Operation
# Day         : 34
# Description : Deleting a node from a Binary Search Tree.
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


def find_min(node):

    while node.left:

        node = node.left

    return node


def delete(root, key):

    if root is None:

        return root

    if key < root.data:

        root.left = delete(root.left, key)

    elif key > root.data:

        root.right = delete(root.right, key)

    else:

        # Case 1 & 2
        if root.left is None:

            return root.right

        elif root.right is None:

            return root.left

        # Case 3
        successor = find_min(root.right)

        root.data = successor.data

        root.right = delete(root.right, successor.data)

    return root


def inorder(root):

    if root:

        inorder(root.left)

        print(root.data, end=" ")

        inorder(root.right)


# Create BST
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:

    root = insert(root, value)

print("Before Deletion:")

inorder(root)

# Delete Node
root = delete(root, 70)

print("\nAfter Deletion:")

inorder(root)