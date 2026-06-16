# Day 10 – Dictionaries

## Objective

The goal of this session is to understand how data can be stored using key-value pairs in Python dictionaries.

---

## What is a Dictionary?

A dictionary is a collection of data stored as **key-value pairs**.

Each key is unique and is used to access its corresponding value.

---

## Creating a Dictionary

Example:

```python id="d1001"
student = {
    "name": "Saloni",
    "age": 20,
    "course": "PDSA"
}
```

---

## Accessing Values

Values can be accessed using keys.

```python id="d1002"
print(student["name"])
print(student["age"])
```

Output:

```text id="d1003"
Saloni
20
```

---

## Adding a New Key-Value Pair

```python id="d1004"
student["city"] = "Prayagraj"
```

---

## Updating a Value

```python id="d1005"
student["age"] = 21
```

---

## Removing an Item

```python id="d1006"
student.pop("course")
```

---

## Dictionary Methods

### Keys

```python id="d1007"
student.keys()
```

### Values

```python id="d1008"
student.values()
```

### Items

```python id="d1009"
student.items()
```

---

## Traversing a Dictionary

```python id="d1010"
for key, value in student.items():
    print(key, value)
```

---

## Key Concepts Learned

* Dictionary
* Key-Value Pair
* Accessing Values
* Updating Values
* Adding Items
* Removing Items
* Dictionary Traversal

---

## Summary

Dictionaries store data in key-value format and provide fast access to information using keys.
