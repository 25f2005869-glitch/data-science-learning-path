# Day 70 – Trie Data Structure

## Objective

The goal of this session is to understand the Trie Data Structure and how it is used for efficient string storage and searching.

---

## What is a Trie?

A Trie is a tree-based data structure used to store and search strings efficiently.

Trie is also known as:

Prefix Tree

because it stores words based on common prefixes.

---

## Why Use a Trie?

Suppose we store:

CAT

CAR

CAN

All three words start with:

CA

Instead of storing the prefix repeatedly, Trie stores it only once.

This saves space and enables fast searching.

---

## Example

Words:

CAT

CAR

CAN

Trie Structure:

        Root
          |
          C
          |
          A
       /  |  \
      T   R   N

---

## Key Property

Each node represents:

One Character

A path from root to a node represents:

A Prefix

---

## Word Search

To search:

CAR

Traverse:

Root

↓

C

↓

A

↓

R

If path exists and word is marked:

Word Found

---

## Prefix Search

Suppose prefix:

CA

Exists in Trie:

CAT

CAR

CAN

All matching words can be found quickly.

---

## Trie Node

Each node stores:

- Character Links
- End Of Word Marker

Example:

Node:

A

Children:

T

R

N

---

## Operations

### Insert

Add a word character by character.

Example:

Insert:

CAT

Create:

C

↓

A

↓

T

Mark T as end of word.

---

### Search

Traverse characters one by one.

If path exists and last node is marked:

Word Found

---

### Starts With

Check whether a prefix exists.

Example:

CA

Exists

Result:

True

---

## Algorithm

### Insert

1. Start from root.
2. Process characters.
3. Create missing nodes.
4. Mark last node.

---

### Search

1. Start from root.
2. Traverse characters.
3. If path breaks:
   Return False.
4. Check end marker.

---

## Applications

### Autocomplete

Google Search Suggestions

---

### Spell Checker

Word Validation

---

### Dictionary Applications

Fast Word Lookup

---

### Search Engines

Prefix Matching

---

### Contact Lists

Name Search

---

## Time Complexity

Let:

L = Length of Word

Insert:

O(L)

Search:

O(L)

Prefix Search:

O(L)

---

## Space Complexity

O(N × L)

Where:

N = Number of Words

L = Average Length

---

## Trie vs Hash Table

| Feature | Trie | Hash Table |
|----------|----------|----------|
| Prefix Search | Yes | No |
| Search | O(L) | O(L) |
| Autocomplete | Excellent | Difficult |
| Memory Usage | Higher | Lower |

---

## Key Concepts Learned

- Trie
- Prefix Tree
- String Searching
- Prefix Matching
- Autocomplete

---

## Summary

A Trie is a tree-based data structure designed for efficient storage and retrieval of strings. It is especially useful for prefix searches, autocomplete systems, and dictionary-based applications.