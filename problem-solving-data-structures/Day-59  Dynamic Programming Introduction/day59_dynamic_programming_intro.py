
# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Dynamic Programming Introduction
# Day         : 59
# Description : Fibonacci using Dynamic Programming
#               (Tabulation Method).
# ==========================================================

def fibonacci(n):

    if n <= 1:

        return n

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):

        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = 10

print("Fibonacci Number:")

print(fibonacci(n))