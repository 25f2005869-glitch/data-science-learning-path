# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Linked List Insertion
# Day         : 22
# Description : Inserting nodes at the beginning and end
#               of a singly linked list.
# ==========================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


# Create initial linked list
head = Node(10)

second = Node(20)
third = Node(30)

head.next = second
second.next = third


# Insert at Beginning
new_node = Node(5)

new_node.next = head

head = new_node


# Insert at End
end_node = Node(40)

current = head

while current.next is not None:

    current = current.next

current.next = end_node


# Display Linked List
current = head

print("Linked List:")

while current is not None:

    print(current.data, end=" -> ")

    current = current.next

print("NULL")