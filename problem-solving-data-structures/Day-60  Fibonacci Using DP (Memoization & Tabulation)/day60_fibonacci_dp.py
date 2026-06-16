# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Fibonacci Using DP
# Day         : 60
# Description : Fibonacci using Memoization and
#               Tabulation techniques.
# ==========================================================

# -------------------------
# Memoization (Top-Down)
# -------------------------

memo = {}


def fibonacci_memo(n):

    if n <= 1:

        return n

    if n not in memo:

        memo[n] = (

            fibonacci_memo(n - 1)

            + fibonacci_memo(n - 2)

        )

    return memo[n]


# -------------------------
# Tabulation (Bottom-Up)
# -------------------------

def fibonacci_tab(n):

    if n <= 1:

        return n

    dp = [0] * (n + 1)

    dp[0] = 0

    dp[1] = 1

    for i in range(2, n + 1):

        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = 10

print("Memoization Result:")

print(fibonacci_memo(n))

print("\nTabulation Result:")

print(fibonacci_tab(n))