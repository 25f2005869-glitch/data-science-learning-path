📘 Day 54 – Huffman Coding
notes.md
Day 54 – Huffman Coding
Objective

The goal of this session is to understand Huffman Coding and how Greedy Algorithms are used in data compression.

What is Huffman Coding?

Huffman Coding is a lossless data compression algorithm.

It assigns:

Short Codes

to frequently occurring characters and

Long Codes

to less frequent characters.

This reduces the total storage required.

Why Huffman Coding?

Normal Encoding:

A = 8 bits
B = 8 bits
C = 8 bits

Every character uses the same number of bits.

Huffman Encoding:

Frequent Characters → Fewer Bits

Rare Characters → More Bits

Result:

Smaller File Size
Example

Character Frequencies:

Character	Frequency
A	5
B	9
C	12
D	13
E	16
F	45
Greedy Strategy

Always combine:

Two Lowest Frequency Nodes

This is the greedy choice.

Step 1

Combine:

A(5) + B(9)

New Node:

14
Step 2

Combine:

C(12) + D(13)

New Node:

25
Step 3

Combine:

14 + E(16)

New Node:

30
Continue Until One Node Remains

Final Huffman Tree:

                100
              /     \
            F(45)    55
                    /   \
                  25     30
                 / \    /  \
               C  D   14   E
                     / \
                    A   B
Assign Binary Codes

Rule:

Left Edge  = 0

Right Edge = 1

Generated Codes:

Character	Code
F	0
C	100
D	101
A	1100
B	1101
E	111
Prefix Property

No code is the prefix of another code.

Example:

0
100
101
1100

All codes are unique.

Why Greedy Works?

At every step:

Choose Smallest Frequencies

This minimizes total encoding cost.

Huffman Algorithm
Create a node for each character.
Insert nodes into a Min Heap.
Remove two minimum nodes.
Combine them.
Insert combined node back.
Repeat until one node remains.
Applications
ZIP Files
PNG Images
JPEG Compression
MP3 Compression
Data Transmission
File Archiving
Time Complexity

Using Min Heap:

O(n log n)

Where:

n = Number of Characters
Space Complexity
O(n)
Key Concepts Learned
Huffman Coding
Data Compression
Min Heap
Prefix Code
Greedy Algorithm
Huffman Tree
Summary

Huffman Coding is a Greedy Algorithm that builds an optimal prefix code by repeatedly combining the two least frequent characters. It is one of the most important algorithms in data compression.