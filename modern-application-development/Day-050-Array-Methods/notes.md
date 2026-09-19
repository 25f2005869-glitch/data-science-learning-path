# 📦 Day 050 — Array Methods — Detailed Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 050  
**Topic:** Array Methods

---

# 1. What Are Array Methods?

Array methods are built-in JavaScript functions that help us work with arrays.

They can be used to:

- Add elements
- Remove elements
- Search elements
- Transform elements
- Filter elements
- Calculate values
- Check conditions
- Sort data

Example:

    const numbers = [1, 2, 3];

    numbers.push(4);

---

# 2. Callback Function

Many modern array methods accept a function as an argument.

This function is called a callback function.

Example:

    numbers.forEach(function(number) {
        console.log(number);
    });

The callback is executed for each element.

Arrow functions are commonly used:

    numbers.forEach(number => {
        console.log(number);
    });

---

# 3. forEach()

`forEach()` executes a function once for each array element.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    subjects.forEach(subject => {
        console.log(subject);
    });

Output:

    DBMS
    PDSA
    MLF

`forEach()` is useful when we want to perform an action for every element.

---

# 4. forEach() Parameters

The callback can receive:

- Current element
- Index
- Complete array

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    subjects.forEach((subject, index) => {
        console.log(index, subject);
    });

Output:

    0 DBMS
    1 PDSA
    2 MLF

---

# 5. map()

`map()` creates a new array by transforming every element.

Example:

    const numbers = [1, 2, 3, 4];

    const squares = numbers.map(number => number * number);

Result:

    [1, 4, 9, 16]

Important:

`map()` returns a new array.

---

# 6. map() vs forEach()

| `map()` | `forEach()` |
|---|---|
| Returns a new array | Does not return a transformed array |
| Used for transformation | Used for performing an action |
| Usually stores returned values | Return value is generally ignored |

Example:

    const doubled = numbers.map(number => number * 2);

---

# 7. filter()

`filter()` creates a new array containing elements that satisfy a condition.

Example:

    const marks = [35, 45, 60, 30, 80];

    const passingMarks = marks.filter(mark => mark >= 40);

Result:

    [45, 60, 80]

The callback must produce a truthy or falsy result.

---

# 8. filter() with Objects

Example:

    const students = [
        { name: "Asha", marks: 85 },
        { name: "Riya", marks: 35 },
        { name: "Neha", marks: 75 }
    ];

    const passed = students.filter(student => student.marks >= 40);

The result contains only passing students.

---

# 9. find()

`find()` returns the first element that satisfies a condition.

Example:

    const numbers = [10, 20, 30, 40];

    const result = numbers.find(number => number > 25);

Result:

    30

If no element satisfies the condition:

    undefined

---

# 10. findIndex()

`findIndex()` returns the index of the first matching element.

Example:

    const numbers = [10, 20, 30, 40];

    const index = numbers.findIndex(number => number > 25);

Result:

    2

If no element matches:

    -1

---

# 11. find() vs findIndex()

| Method | Returns |
|---|---|
| `find()` | Matching element |
| `findIndex()` | Index of matching element |

---

# 12. some()

`some()` checks whether at least one element satisfies a condition.

Example:

    const marks = [30, 45, 60];

    const hasHighMark = marks.some(mark => mark >= 50);

Result:

    true

Only one matching element is enough.

---

# 13. every()

`every()` checks whether all elements satisfy a condition.

Example:

    const marks = [50, 60, 70];

    const allPassed = marks.every(mark => mark >= 40);

Result:

    true

If even one element fails the condition, it returns `false`.

---

# 14. some() vs every()

| `some()` | `every()` |
|---|---|
| At least one must satisfy condition | Every element must satisfy condition |
| Stops when a match is found | Stops when a failure is found |

---

# 15. reduce()

`reduce()` processes all array elements and produces a single final value.

Example:

    const numbers = [10, 20, 30];

    const total = numbers.reduce(
        (sum, number) => sum + number,
        0
    );

Result:

    60

Here:

- `sum` → accumulator
- `number` → current element
- `0` → initial value

---

# 16. Understanding reduce()

For:

    [10, 20, 30]

with initial value `0`:

First:

    0 + 10 = 10

Second:

    10 + 20 = 30

Third:

    30 + 30 = 60

Final result:

    60

---

# 17. reduce() for Product

Example:

    const numbers = [2, 3, 4];

    const product = numbers.reduce(
        (result, number) => result * number,
        1
    );

Result:

    24

---

# 18. reduce() for Objects

`reduce()` can also create an object.

Example:

    const numbers = [1, 2, 3];

    const result = numbers.reduce((obj, number) => {
        obj[number] = number * 2;
        return obj;
    }, {});

Result:

    {
        1: 2,
        2: 4,
        3: 6
    }

---

# 19. sort()

`sort()` sorts array elements.

For strings:

    const subjects = ["MLF", "DBMS", "PDSA"];

    subjects.sort();

The array is sorted alphabetically.

---

# 20. Numerical Sorting

By default, `sort()` converts elements to strings.

Therefore, for numbers, use a comparison function.

Ascending:

    const numbers = [10, 5, 30, 2];

    numbers.sort((a, b) => a - b);

Result:

    [2, 5, 10, 30]

Descending:

    numbers.sort((a, b) => b - a);

Result:

    [30, 10, 5, 2]

---

# 21. reverse()

`reverse()` reverses the order of array elements.

Example:

    const numbers = [1, 2, 3, 4];

    numbers.reverse();

Result:

    [4, 3, 2, 1]

`reverse()` modifies the original array.

---

# 22. includes()

`includes()` checks whether a value exists.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    subjects.includes("PDSA");

Result:

    true

---

# 23. indexOf()

`indexOf()` returns the index of the first matching value.

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    subjects.indexOf("MLF");

Result:

    2

If the value is not found:

    -1

---

# 24. Mutating Array Methods

Some methods modify the original array.

Examples:

    push()
    pop()
    shift()
    unshift()
    splice()
    sort()
    reverse()

These are called mutating methods.

---

# 25. Non-Mutating Methods

Some methods create or return results without changing the original array.

Examples:

    map()
    filter()
    find()
    findIndex()
    some()
    every()
    includes()
    indexOf()
    slice()

This distinction is important when writing predictable code.

---

# 26. Method Chaining

Multiple array methods can be combined.

Example:

    const numbers = [1, 2, 3, 4, 5, 6];

    const result = numbers
        .filter(number => number % 2 === 0)
        .map(number => number * 2);

Result:

    [4, 8, 12]

Execution:

1. `filter()` selects even numbers.
2. `map()` doubles them.

---

# 27. Array Methods with Objects

Example:

    const students = [
        { name: "Asha", marks: 85 },
        { name: "Riya", marks: 72 },
        { name: "Neha", marks: 92 }
    ];

Find the student with marks above 80:

    const result = students.find(student => student.marks > 80);

Filter students:

    const highScorers = students.filter(
        student => student.marks >= 80
    );

Extract names:

    const names = students.map(student => student.name);

---

# 28. Calculating Average with reduce()

Example:

    const marks = [80, 90, 70, 85];

    const total = marks.reduce(
        (sum, mark) => sum + mark,
        0
    );

    const average = total / marks.length;

This combines `reduce()` with `length`.

---

# 29. Practical Student Example

Given:

    const marks = [85, 90, 38, 72, 95];

Passing marks:

    const passed = marks.filter(mark => mark >= 40);

Highest mark:

    const highest = marks.reduce(
        (max, mark) => mark > max ? mark : max,
        marks[0]
    );

Check whether every student passed:

    const allPassed = marks.every(mark => mark >= 40);

---

# 30. Common Mistakes

### Mistake 1: Forgetting that map() returns a new array

    numbers.map(number => number * 2);

The result should be stored if you need it later.

### Mistake 2: Using sort() directly for numbers

Incorrect:

    [10, 2, 30].sort();

Use:

    [10, 2, 30].sort((a, b) => a - b);

### Mistake 3: Confusing find() and filter()

`find()` returns one matching element.

`filter()` returns an array containing all matching elements.

### Mistake 4: Forgetting reduce() initial value

Using an explicit initial value often makes the logic clearer and safer.

---

# 31. Important Comparison

| Method | Main Purpose | Result |
|---|---|---|
| `forEach()` | Perform action | `undefined` |
| `map()` | Transform | New array |
| `filter()` | Select | New array |
| `find()` | Find first match | Element / `undefined` |
| `findIndex()` | Find first matching index | Number / `-1` |
| `some()` | Check any | Boolean |
| `every()` | Check all | Boolean |
| `reduce()` | Combine values | Single value |
| `sort()` | Sort | Sorted array |
| `reverse()` | Reverse | Reversed array |

---

# 32. Best Practices

- Use `map()` when transforming every element.
- Use `filter()` when selecting elements.
- Use `find()` when only the first match is needed.
- Use `some()` for "at least one" conditions.
- Use `every()` for "all" conditions.
- Use `reduce()` for totals and aggregation.
- Always use a comparison function for numerical `sort()`.
- Remember which methods mutate the original array.
- Keep callbacks short and readable.
- Use method chaining when it improves readability.