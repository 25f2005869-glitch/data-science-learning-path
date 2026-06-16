# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Greedy Algorithms Introduction
# Day         : 51
# Description : Coin Change using Greedy Approach.
# ==========================================================

amount = 67

coins = [10, 5, 2, 1]

result = []

for coin in coins:

    while amount >= coin:

        amount -= coin

        result.append(coin)

print("Coins Used:")

print(result)

print("\nTotal Coins:")

print(len(result))