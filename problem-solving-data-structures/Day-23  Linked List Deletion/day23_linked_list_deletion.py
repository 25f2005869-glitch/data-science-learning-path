# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Linked List Deletion
# Day         : 23
# Description : Deleting a node from a singly linked list.
# ==========================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


# Create Linked List
head = Node(10)

second = Node(20)
third = Node(30)
fourth = Node(40)

head.next = second
second.next = third
third.next = fourth


# Delete node with value 30
current = head

while current.next is not None:

    if current.next.data == 30:

        current.next = current.next.next

        break

    current = current.next


# Display Linked List
current = head

print("Linked List After Deletion:")

while current is not None:

    print(current.data, end=" -> ")

    current = current.next

print("NULL")