# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Longest Increasing Subsequence (LIS)
# Day         : 64
# Description : Finding LIS length using Dynamic
#               Programming.
# ==========================================================

arr = [10, 22, 9, 33, 21, 50, 41, 60]

n = len(arr)

dp = [1] * n

for i in range(1, n):

    for j in range(i):

        if arr[j] < arr[i]:

            dp[i] = max(

                dp[i],

                dp[j] + 1

            )

print("Length of LIS:")

print(max(dp))