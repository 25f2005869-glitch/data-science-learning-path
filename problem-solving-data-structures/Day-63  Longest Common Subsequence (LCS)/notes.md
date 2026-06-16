# Day 63 – Longest Common Subsequence (LCS)

## Objective

The goal of this session is to understand the Longest Common Subsequence (LCS) problem and solve it using Dynamic Programming.

---

## What is a Subsequence?

A subsequence is a sequence obtained by deleting zero or more characters without changing the order of the remaining characters.

Example:

String:

ABCDEF

Possible Subsequences:

ABC

ACE

ADF

ABF

ADEF

---

## What is Longest Common Subsequence?

The Longest Common Subsequence (LCS) is the longest sequence that appears in both strings while maintaining order.

Example:

String 1:

ABCDE

String 2:

ACE

Common Subsequences:

A

AC

ACE

Longest Common Subsequence:

ACE

Length:

3

---

## Example

String 1:

ABCDGH

String 2:

AEDFHR

Common Subsequences:

ADH

AH

AD

Longest Common Subsequence:

ADH

Length:

3

---

## Key Observation

Compare characters one by one.

If characters match:

Include the character in LCS.

If characters do not match:

Try both possibilities and take the better result.

---

## Recurrence Relation

If characters match:

LCS(i,j)

=

1 + LCS(i−1,j−1)

---

If characters do not match:

LCS(i,j)

=

max(

LCS(i−1,j),

LCS(i,j−1)

)

---

## Dynamic Programming Table

String 1:

ABCDGH

String 2:

AEDFHR

Final DP Value:

3

This represents the length of the Longest Common Subsequence.

---

## Algorithm

1. Create DP table.
2. Compare characters.
3. If match:
   Add 1 to diagonal value.
4. Otherwise:
   Take maximum of top and left cell.
5. Final cell contains LCS length.

---

## Applications

### DNA Sequence Analysis

Compare genetic sequences.

### Spell Checkers

Find similar words.

### Version Control Systems

Compare file changes.

### Text Comparison

Document similarity detection.

---

## Time Complexity

O(m × n)

Where:

m = Length of First String

n = Length of Second String

---

## Space Complexity

O(m × n)

---

## Key Concepts Learned

- Subsequence
- Longest Common Subsequence
- Dynamic Programming
- Recurrence Relation
- DP Table

---

## Summary

The Longest Common Subsequence problem finds the longest sequence that appears in two strings while preserving character order. It is one of the most important Dynamic Programming problems and forms the basis for many string algorithms.