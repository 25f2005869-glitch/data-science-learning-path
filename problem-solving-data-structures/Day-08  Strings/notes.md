# Day 08 – Strings

## Objective

The goal of this session is to understand how text data is stored and manipulated using strings in Python.

---

## What is a String?

A string is a sequence of characters enclosed in quotes.

Examples:

```python id="s801"
name = "Saloni"
city = 'Prayagraj'
```

---

## Accessing Characters

Strings use indexing.

```python id="s802"
text = "Python"

print(text[0])
print(text[1])
```

Output:

```text id="s803"
P
y
```

---

## Length of a String

The `len()` function returns the number of characters.

```python id="s804"
text = "Python"

print(len(text))
```

Output:

```text id="s805"
6
```

---

## String Concatenation

Joining two strings using `+`.

```python id="s806"
first = "Hello"
second = "World"

print(first + " " + second)
```

Output:

```text id="s807"
Hello World
```

---

## String Repetition

```python id="s808"
print("Hi " * 3)
```

Output:

```text id="s809"
Hi Hi Hi
```

---

## Common String Methods

### Uppercase

```python id="s810"
text.upper()
```

### Lowercase

```python id="s811"
text.lower()
```

### Replace

```python id="s812"
text.replace("Python", "PDSA")
```

---

## Traversing a String

```python id="s813"
text = "Python"

for ch in text:
    print(ch)
```

---

## Key Concepts Learned

* String
* Indexing
* len()
* Concatenation
* String Methods
* String Traversal

---

## Summary

Strings are used to store and manipulate textual data. They are one of the most frequently used data types in programming.
