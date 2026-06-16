# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Circular Queue
# Day         : 26
# Description : Implementation of a Circular Queue using
#               a fixed-size list.
# ==========================================================

SIZE = 5

queue = [None] * SIZE

front = -1
rear = -1


def enqueue(value):

    global front, rear

    if (rear + 1) % SIZE == front:

        print("Queue Overflow")

        return

    if front == -1:

        front = 0

    rear = (rear + 1) % SIZE

    queue[rear] = value


def dequeue():

    global front, rear

    if front == -1:

        print("Queue Underflow")

        return

    removed = queue[front]

    if front == rear:

        front = rear = -1

    else:

        front = (front + 1) % SIZE

    return removed


# Enqueue Operations
enqueue(10)
enqueue(20)
enqueue(30)

print("Queue:", queue)

# Dequeue Operation
print("Removed:", dequeue())

print("Queue After Dequeue:", queue)