# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Bitmask Dynamic Programming
# Day         : 79
# Description : Counting subsets using Bitmask DP.
# ==========================================================

n = 3

dp = [0] * (1 << n)

dp[0] = 1

for mask in range(1 << n):

    for bit in range(n):

        if not (mask & (1 << bit)):

            new_mask = mask | (1 << bit)

            dp[new_mask] += dp[mask]

print("DP States:\n")

for mask in range(1 << n):

    print(

        bin(mask)[2:].zfill(n),

        "->",

        dp[mask]

    )