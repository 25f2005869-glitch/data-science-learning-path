# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Depth First Search (DFS)
# Day         : 37
# Description : DFS Traversal using Recursion.
# ==========================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


# Create Tree
root = Node("A")

root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")

root.right.left = Node("F")
root.right.right = Node("G")


def dfs(node):

    if node is None:

        return

    print(node.data, end=" ")

    dfs(node.left)

    dfs(node.right)


print("DFS Traversal:")

dfs(root)