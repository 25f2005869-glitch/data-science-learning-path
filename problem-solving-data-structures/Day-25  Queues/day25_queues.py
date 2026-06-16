# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Queues
# Day         : 25
# Description : Basic queue operations using deque.
# ==========================================================

from collections import deque

queue = deque()

# Enqueue Operation
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue After Enqueue:", list(queue))

# Front Element
print("Front Element:", queue[0])

# Rear Element
print("Rear Element:", queue[-1])

# Dequeue Operation
removed = queue.popleft()

print("Removed Element:", removed)

print("Queue After Dequeue:", list(queue))

# Is Empty Check
if len(queue) == 0:

    print("Queue is Empty")

else:

    print("Queue is Not Empty")