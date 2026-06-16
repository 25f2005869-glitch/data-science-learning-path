# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Matrix Chain Multiplication (MCM)
# Day         : 66
# Description : Minimum multiplication cost using
#               Dynamic Programming.
# ==========================================================

dimensions = [10, 30, 5, 60]

n = len(dimensions)

dp = [

    [0] * n

    for _ in range(n)

]

for length in range(2, n):

    for i in range(1, n - length + 1):

        j = i + length - 1

        dp[i][j] = float("inf")

        for k in range(i, j):

            cost = (

                dp[i][k]

                + dp[k + 1][j]

                + dimensions[i - 1]

                * dimensions[k]

                * dimensions[j]

            )

            dp[i][j] = min(

                dp[i][j],

                cost

            )

print("Minimum Multiplication Cost:")

print(dp[1][n - 1])