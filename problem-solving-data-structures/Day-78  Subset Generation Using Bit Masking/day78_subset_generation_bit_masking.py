# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Subset Generation Using Bit Masking
# Day         : 78
# Description : Generate all subsets using binary masks.
# ==========================================================

arr = [1, 2, 3]

n = len(arr)

print("All Subsets:\n")

for mask in range(1 << n):

    subset = []

    for i in range(n):

        if mask & (1 << i):

            subset.append(arr[i])

    print(subset)