# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Recursion Backtracking
# Day         : 48
# Description : Generate all permutations of a string
#               using Backtracking.
# ==========================================================

def backtrack(chars, start):

    if start == len(chars):

        print("".join(chars))

        return

    for i in range(start, len(chars)):

        chars[start], chars[i] = chars[i], chars[start]

        backtrack(chars, start + 1)

        chars[start], chars[i] = chars[i], chars[start]


text = list("ABC")

print("Permutations:\n")

backtrack(text, 0)