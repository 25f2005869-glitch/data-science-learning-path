# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Deque (Double Ended Queue)
# Day         : 27
# Description : Basic deque operations using collections.deque
# ==========================================================

from collections import deque

dq = deque()

# Insert at Rear
dq.append(10)
dq.append(20)

# Insert at Front
dq.appendleft(5)

print("Deque:", list(dq))

# Delete from Front
front_removed = dq.popleft()

print("Removed From Front:", front_removed)

# Delete from Rear
rear_removed = dq.pop()

print("Removed From Rear:", rear_removed)

print("Final Deque:", list(dq))

# Front and Rear Elements
if dq:

    print("Front Element:", dq[0])

    print("Rear Element:", dq[-1])