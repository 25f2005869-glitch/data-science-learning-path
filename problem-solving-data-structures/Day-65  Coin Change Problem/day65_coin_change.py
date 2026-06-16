# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Coin Change Problem
# Day         : 65
# Description : Minimum coins required using
#               Dynamic Programming.
# ==========================================================

coins = [1, 2, 5]

amount = 11

dp = [float("inf")] * (amount + 1)

dp[0] = 0

for value in range(1, amount + 1):

    for coin in coins:

        if coin <= value:

            dp[value] = min(

                dp[value],

                dp[value - coin] + 1

            )

print("Minimum Coins Required:")

print(dp[amount])