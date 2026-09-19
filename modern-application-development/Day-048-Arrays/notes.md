# 📦 Day 048 — Arrays — Detailed Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 048  
**Topic:** Arrays

---

# 1. What Is an Array?

An array is a data structure used to store multiple values in a single variable.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

Instead of creating three separate variables, we can store all subjects in one array.

---

# 2. Why Use Arrays?

Arrays are useful when we have a collection of related values.

Examples:

- Student marks
- Course names
- Product prices
- Names of students
- List of cities
- Project names

Example:

    const marks = [85, 90, 78, 92];

---

# 3. Creating an Array

The most common syntax is:

    const fruits = ["Apple", "Banana", "Mango"];

An array can contain numbers:

    const numbers = [10, 20, 30, 40];

It can also contain different JavaScript values:

    const data = ["Saloni", 17, true];

For beginner code, it is usually clearer to keep related data of the same kind together.

---

# 4. Array Index

Array indexes start from `0`.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

Indexes:

    DBMS → 0
    PDSA → 1
    MLF  → 2

Access an element:

    console.log(subjects[0]);

Output:

    DBMS

---

# 5. Accessing Array Elements

Example:

    const marks = [80, 90, 75];

    console.log(marks[0]);
    console.log(marks[1]);
    console.log(marks[2]);

Output:

    80
    90
    75

---

# 6. Last Element

The last element can be accessed using:

    array[array.length - 1]

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    console.log(subjects[subjects.length - 1]);

Output:

    MLF

---

# 7. Array length

The `length` property returns the number of elements.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    console.log(subjects.length);

Output:

    3

Remember:

- `length` = number of elements
- Last index = `length - 1`

---

# 8. Updating an Array Element

Array elements can be changed using their index.

Example:

    const marks = [80, 90, 75];

    marks[1] = 95;

Now:

    [80, 95, 75]

The second element was changed.

---

# 9. push()

`push()` adds one or more elements to the end of an array.

Example:

    const subjects = ["DBMS", "PDSA"];

    subjects.push("MLF");

Now:

    ["DBMS", "PDSA", "MLF"]

`push()` returns the new array length.

---

# 10. pop()

`pop()` removes the last element.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    subjects.pop();

Now:

    ["DBMS", "PDSA"]

`pop()` returns the removed element.

---

# 11. unshift()

`unshift()` adds elements to the beginning of an array.

Example:

    const subjects = ["PDSA", "MLF"];

    subjects.unshift("DBMS");

Now:

    ["DBMS", "PDSA", "MLF"]

---

# 12. shift()

`shift()` removes the first element.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    subjects.shift();

Now:

    ["PDSA", "MLF"]

---

# 13. push vs unshift

| Method | Action |
|---|---|
| `push()` | Add at end |
| `unshift()` | Add at beginning |

---

# 14. pop vs shift

| Method | Action |
|---|---|
| `pop()` | Remove from end |
| `shift()` | Remove from beginning |

---

# 15. Iterating Through an Array

A `for` loop can be used to visit every element.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    for (let i = 0; i < subjects.length; i++) {
        console.log(subjects[i]);
    }

Output:

    DBMS
    PDSA
    MLF

---

# 16. Array with Functions

Arrays can be passed to functions.

Example:

    function calculateTotal(numbers) {
        let total = 0;

        for (let i = 0; i < numbers.length; i++) {
            total += numbers[i];
        }

        return total;
    }

    const marks = [80, 90, 75];

    console.log(calculateTotal(marks));

Output:

    245

---

# 17. includes()

`includes()` checks whether an array contains a specific value.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    console.log(subjects.includes("PDSA"));

Output:

    true

If the value does not exist:

    subjects.includes("MAD1");

Result:

    false

---

# 18. indexOf()

`indexOf()` returns the index of the first matching element.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    console.log(subjects.indexOf("PDSA"));

Output:

    1

If the value is not found:

    -1

---

# 19. join()

`join()` combines array elements into a string.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    console.log(subjects.join(", "));

Output:

    DBMS, PDSA, MLF

---

# 20. slice()

`slice()` creates a new array containing a selected portion.

Syntax:

    array.slice(start, end)

Example:

    const numbers = [10, 20, 30, 40, 50];

    const result = numbers.slice(1, 4);

Result:

    [20, 30, 40]

The ending index is not included.

Important:

`slice()` does not modify the original array.

---

# 21. splice()

`splice()` can add, remove, or replace elements.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    subjects.splice(1, 1);

Result:

    ["DBMS", "MLF"]

The first argument is the starting index.

The second argument is the number of elements to remove.

---

# 22. Adding with splice()

Example:

    const subjects = ["DBMS", "MLF"];

    subjects.splice(1, 0, "PDSA");

Result:

    ["DBMS", "PDSA", "MLF"]

Here:

- Start index = `1`
- Remove = `0`
- Add = `"PDSA"`

---

# 23. Replacing with splice()

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    subjects.splice(1, 1, "MAD1");

Result:

    ["DBMS", "MAD1", "MLF"]

---

# 24. slice() vs splice()

| `slice()` | `splice()` |
|---|---|
| Creates a selected portion | Adds/removes/replaces elements |
| Does not modify original array | Modifies original array |
| Useful for copying/extracting | Useful for changing array contents |

---

# 25. Nested Arrays

An array can contain other arrays.

Example:

    const matrix = [
        [1, 2],
        [3, 4]
    ];

Access an element:

    console.log(matrix[0][1]);

Output:

    2

The first index selects the inner array.

The second index selects the element inside it.

---

# 26. Array of Objects

Arrays can also contain objects.

Example:

    const students = [
        { name: "Asha", marks: 85 },
        { name: "Riya", marks: 90 }
    ];

This becomes especially useful when working with structured data.

---

# 27. Array Traversal

Traversal means visiting each element of an array.

Example:

    const numbers = [10, 20, 30];

    for (let i = 0; i < numbers.length; i++) {
        console.log(numbers[i]);
    }

Traversal is one of the most important operations when working with arrays.

---

# 28. Finding Total

Example:

    const marks = [80, 90, 70, 85];

    let total = 0;

    for (let i = 0; i < marks.length; i++) {
        total += marks[i];
    }

    console.log(total);

Output:

    325

---

# 29. Finding Maximum

Example:

    const numbers = [12, 45, 7, 89, 23];

    let maximum = numbers[0];

    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > maximum) {
            maximum = numbers[i];
        }
    }

    console.log(maximum);

Output:

    89

---

# 30. Finding Minimum

Example:

    const numbers = [12, 45, 7, 89, 23];

    let minimum = numbers[0];

    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] < minimum) {
            minimum = numbers[i];
        }
    }

    console.log(minimum);

Output:

    7

---

# 31. Arrays and const

An array declared with `const` can still have its elements changed.

Example:

    const numbers = [10, 20, 30];

    numbers.push(40);

This is valid.

But assigning a completely new array is not allowed:

    numbers = [50, 60];

The variable itself cannot be reassigned.

---

# 32. Common Mistakes

### Mistake 1: Wrong index

For:

    const numbers = [10, 20, 30];

The indexes are:

    0, 1, 2

There is no index `3`.

### Mistake 2: Using <= in traversal

Usually use:

    i < array.length

rather than:

    i <= array.length

because `array.length` is not a valid last index.

### Mistake 3: Confusing slice and splice

Remember:

- `slice()` → extracts without changing original.
- `splice()` → changes original.

---

# 33. Important Concepts

- Arrays store multiple values.
- Array indexes start at `0`.
- `length` gives the number of elements.
- Elements can be accessed and updated using indexes.
- `push()` adds at the end.
- `pop()` removes from the end.
- `unshift()` adds at the beginning.
- `shift()` removes from the beginning.
- `slice()` extracts without modifying the original.
- `splice()` modifies the array.
- `includes()` checks existence.
- `indexOf()` finds an index.
- `join()` converts array elements into a string.
- Loops can traverse arrays.

---

# 34. Best Practices

- Use meaningful array names.
- Use `const` when the array variable does not need reassignment.
- Remember that indexing starts from `0`.
- Use `array.length` for dynamic traversal.
- Avoid unnecessary modifications to arrays.
- Choose `slice()` or `splice()` according to whether mutation is required.
- Keep related data together.
- Use functions to organize repeated array operations.