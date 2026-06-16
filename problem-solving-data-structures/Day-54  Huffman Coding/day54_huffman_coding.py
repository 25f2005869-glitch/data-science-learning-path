# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Huffman Coding
# Day         : 54
# Description : Building a Huffman Tree using Min Heap.
# ==========================================================

import heapq

frequencies = [

    ("A", 5),
    ("B", 9),
    ("C", 12),
    ("D", 13),
    ("E", 16),
    ("F", 45)

]

heap = []

for char, freq in frequencies:

    heapq.heappush(heap, (freq, char))

while len(heap) > 1:

    left = heapq.heappop(heap)

    right = heapq.heappop(heap)

    merged_freq = left[0] + right[0]

    merged_node = (

        merged_freq,

        left[1] + right[1]

    )

    heapq.heappush(heap, merged_node)

print("Root Node:")

print(heap[0])