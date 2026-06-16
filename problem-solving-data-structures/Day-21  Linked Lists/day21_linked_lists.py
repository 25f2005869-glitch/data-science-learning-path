# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Linked Lists
# Day         : 21
# Description : Creating and traversing a singly linked list.
# ==========================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking nodes
node1.next = node2
node2.next = node3

# Head node
head = node1

# Traversal
current = head

print("Linked List:")

while current is not None:

    print(current.data, end=" -> ")

    current = current.next

print("NULL")