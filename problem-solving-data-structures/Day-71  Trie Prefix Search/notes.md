# Day 71 – Trie Prefix Search

## Objective

The goal of this session is to understand how Tries can be used for efficient prefix searching and autocomplete functionality.

---

## What is Prefix Search?

Prefix Search means finding words that start with a given sequence of characters.

Example:

Words:

APPLE

APPLICATION

APPLY

APE

BALL

Prefix:

APP

Matching Words:

APPLE

APPLICATION

APPLY

---

## Why Prefix Search?

Suppose a user types:

APP

Search engines immediately suggest:

APPLE

APPLICATION

APPLY

This feature is powered by Trie-based prefix searching.

---

## How Trie Helps?

Words:

APPLE

APPLICATION

APPLY

APE

Trie Structure:

            Root
              |
              A
              |
              P
            /   \
           E     P
                / \
               L   L
               |   |
               E   Y
               |
               I
               |
               C
               |
               A
               |
               T
               |
               I
               |
               O
               |
               N

---

## Key Idea

First:

Find the node representing the prefix.

Then:

Traverse all child nodes.

Every complete word found is a matching result.

---

## Example

Stored Words:

APPLE

APPLICATION

APPLY

APE

BALL

---

Prefix:

APP

Traversal:

Root

↓

A

↓

P

↓

P

Prefix Found

---

Continue Searching:

APPLE

APPLICATION

APPLY

---

Result

APPLE

APPLICATION

APPLY

---

## Prefix Search Algorithm

### Step 1

Find Prefix Node

Traverse characters one by one.

If path does not exist:

No Match

---

### Step 2

Collect Words

Perform DFS from prefix node.

Every end-of-word node represents a valid word.

---

## Applications

### Search Engines

Search Suggestions

---

### Mobile Keyboards

Word Prediction

---

### Dictionary Systems

Prefix Lookup

---

### Contact Search

Name Suggestions

---

### Code Editors

Auto Completion

---

## Time Complexity

Let:

P = Prefix Length

N = Matching Characters

Finding Prefix:

O(P)

Collecting Results:

O(N)

---

Overall:

O(P + N)

---

## Space Complexity

O(N)

for storing Trie nodes.

---

## Advantages

- Fast Prefix Search
- Efficient Autocomplete
- Scalable for Large Dictionaries
- Faster than Linear Search

---

## Key Concepts Learned

- Trie
- Prefix Search
- DFS Traversal
- Autocomplete
- String Searching

---

## Summary

Trie Prefix Search efficiently finds all words that begin with a given prefix. This technique is widely used in search engines, mobile keyboards, IDEs, and dictionary applications.