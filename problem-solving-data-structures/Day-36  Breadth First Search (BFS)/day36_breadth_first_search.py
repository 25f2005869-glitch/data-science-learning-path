# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Breadth First Search (BFS)
# Day         : 36
# Description : Level Order Traversal using BFS.
# ==========================================================

from collections import deque

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


def bfs(root):

    if root is None:

        return

    queue = deque([root])

    while queue:

        current = queue.popleft()

        print(current.data, end=" ")

        if current.left:

            queue.append(current.left)

        if current.right:

            queue.append(current.right)


print("BFS Traversal:")

bfs(root)