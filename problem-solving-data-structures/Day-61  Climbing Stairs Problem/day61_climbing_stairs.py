# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Climbing Stairs Problem
# Day         : 61
# Description : Number of ways to climb stairs using
#               Dynamic Programming.
# ==========================================================

def climb_stairs(n):

    if n <= 2:

        return n

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):

        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = 5

print("Number of Ways:")

print(climb_stairs(n))