# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Priority Queue & Heap
# Day         : 46
# Description : Min Heap implementation using heapq.
# ==========================================================

import heapq

heap = []

# Insert Elements
heapq.heappush(heap, 20)
heapq.heappush(heap, 10)
heapq.heappush(heap, 30)
heapq.heappush(heap, 5)

print("Heap:")

print(heap)

# Peek Minimum Element
print("\nMinimum Element:")

print(heap[0])

# Remove Minimum Element
removed = heapq.heappop(heap)

print("\nRemoved Element:")

print(removed)

print("\nHeap After Removal:")

print(heap)