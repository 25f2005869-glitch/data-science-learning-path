# 🧵 Day 047 — Strings and Template Literals — Detailed Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 047  
**Topic:** Strings and Template Literals

---

# 1. What Is a String?

A string is a sequence of characters used to represent text.

Examples:

    "Hello"
    'JavaScript'
    `IIT Madras`

Strings can contain:

- Letters
- Numbers
- Spaces
- Symbols
- Special characters

Example:

    const name = "Saloni";

---

# 2. Creating Strings

JavaScript provides three common ways to create strings.

### Double Quotes

    const name = "Saloni";

### Single Quotes

    const name = 'Saloni';

### Backticks

    const name = `Saloni`;

Backticks are especially useful for template literals.

---

# 3. String Indexing

Each character in a string has an index.

Indexes start from `0`.

Example:

    const word = "Hello";

Indexes:

    H → 0
    e → 1
    l → 2
    l → 3
    o → 4

Access a character:

    console.log(word[0]);

Output:

    H

---

# 4. String length

The `length` property returns the number of characters.

Example:

    const word = "Hello";

    console.log(word.length);

Output:

    5

Spaces are also counted.

Example:

    const text = "Hello World";

    console.log(text.length);

---

# 5. Last Character

The last character can be accessed using:

    string[string.length - 1]

Example:

    const word = "JavaScript";

    console.log(word[word.length - 1]);

Output:

    t

---

# 6. Strings Are Immutable

Strings cannot be directly changed character by character.

Example:

    let word = "Hello";

This does not change the original string:

    word[0] = "Y";

Instead, create a new string:

    word = "Y" + word.slice(1);

---

# 7. String Concatenation

Concatenation means joining strings together.

Using `+`:

    const firstName = "Saloni";
    const lastName = "Tiwari";

    const fullName = firstName + " " + lastName;

    console.log(fullName);

Output:

    Saloni Tiwari

---

# 8. Escape Characters

Escape characters allow special characters to be included in strings.

### New line

    \n

### Tab

    \t

### Single quote

    \'

### Double quote

    \"

### Backslash

    \\

Example:

    const message = "Hello\nJavaScript";

---

# 9. toUpperCase()

Converts a string to uppercase.

Example:

    const name = "saloni";

    console.log(name.toUpperCase());

Output:

    SALONI

The original string is not changed.

---

# 10. toLowerCase()

Converts a string to lowercase.

Example:

    const name = "SALONI";

    console.log(name.toLowerCase());

Output:

    saloni

---

# 11. trim()

Removes whitespace from the beginning and end of a string.

Example:

    const name = "   Saloni   ";

    console.log(name.trim());

Output:

    Saloni

`trim()` does not remove spaces between words.

---

# 12. includes()

Checks whether a string contains specific text.

Example:

    const course = "Modern Application Development";

    console.log(course.includes("Application"));

Output:

    true

It returns either `true` or `false`.

---

# 13. startsWith()

Checks whether a string starts with specific text.

Example:

    const text = "JavaScript";

    console.log(text.startsWith("Java"));

Output:

    true

---

# 14. endsWith()

Checks whether a string ends with specific text.

Example:

    const file = "index.html";

    console.log(file.endsWith(".html"));

Output:

    true

---

# 15. indexOf()

Returns the index of the first occurrence of specified text.

Example:

    const text = "JavaScript";

    console.log(text.indexOf("Script"));

The result is the starting index of `"Script"`.

If the text is not found, `indexOf()` returns `-1`.

---

# 16. slice()

`slice()` extracts part of a string.

Syntax:

    string.slice(start, end)

Example:

    const text = "JavaScript";

    console.log(text.slice(0, 4));

Output:

    Java

The ending index is not included.

---

# 17. Negative Index with slice()

`slice()` can use negative indexes.

Example:

    const text = "JavaScript";

    console.log(text.slice(-6));

This extracts characters from the end.

---

# 18. substring()

`substring()` extracts characters between two indexes.

Example:

    const text = "JavaScript";

    console.log(text.substring(0, 4));

Output:

    Java

Unlike `slice()`, `substring()` treats negative values differently.

For normal everyday extraction, `slice()` is often easier to reason about.

---

# 19. replace()

`replace()` replaces a matching part of a string.

Example:

    const text = "I like Python";

    const result = text.replace("Python", "JavaScript");

    console.log(result);

Output:

    I like JavaScript

---

# 20. split()

`split()` converts a string into an array.

Example:

    const subjects = "DBMS,PDSA,MLF";

    const result = subjects.split(",");

Result:

    ["DBMS", "PDSA", "MLF"]

This is useful when processing text data.

---

# 21. Template Literals

Template literals use backticks.

Example:

    const name = "Saloni";

    const message = `Hello ${name}`;

    console.log(message);

Output:

    Hello Saloni

---

# 22. String Interpolation

Putting a variable or expression inside a template literal is called interpolation.

Syntax:

    `${expression}`

Example:

    const name = "Saloni";
    const age = 17;

    const message = `My name is ${name} and I am ${age} years old.`;

---

# 23. Expressions in Template Literals

JavaScript expressions can be placed inside `${}`.

Example:

    const a = 10;
    const b = 20;

    console.log(`Total = ${a + b}`);

Output:

    Total = 30

---

# 24. Function Calls in Template Literals

A function can also be called inside `${}`.

Example:

    function square(number) {
        return number * number;
    }

    console.log(`Square = ${square(5)}`);

Output:

    Square = 25

---

# 25. Multiline Strings

Template literals can easily contain multiple lines.

Example:

    const message = `Welcome to JavaScript.
    Today we are learning strings.
    Template literals make formatting easier.`;

No `\n` is required for the line breaks.

---

# 26. Concatenation vs Template Literals

Traditional concatenation:

    const name = "Saloni";
    const course = "MAD 1";

    const message = "My name is " + name + " and I am learning " + course;

Template literal:

    const message = `My name is ${name} and I am learning ${course}`;

Template literals are generally easier to read when many variables are involved.

---

# 27. Combining Strings with Functions

Functions and strings can work together.

Example:

    function createMessage(name, course) {
        return `Hello ${name}. You are learning ${course}.`;
    }

    console.log(createMessage("Saloni", "MAD 1"));

---

# 28. Combining Strings with Loops

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    for (let i = 0; i < subjects.length; i++) {
        console.log(`Subject ${i + 1}: ${subjects[i]}`);
    }

This combines:

- Arrays
- Loops
- Strings
- Template literals

---

# 29. Common Mistakes

### Mistake 1: Forgetting backticks

Incorrect:

    const message = Hello ${name};

Correct:

    const message = `Hello ${name}`;

### Mistake 2: Using quotes instead of backticks for interpolation

This does not interpolate:

    "Hello ${name}"

The `${name}` remains plain text.

Correct:

    `Hello ${name}`

### Mistake 3: Confusing index and length

For:

    const word = "Hello";

`word.length` is `5`.

The last index is `4`.

---

# 30. Useful String Methods

| Method/Property | Purpose |
|---|---|
| `length` | Number of characters |
| `toUpperCase()` | Convert to uppercase |
| `toLowerCase()` | Convert to lowercase |
| `trim()` | Remove outer whitespace |
| `includes()` | Check for text |
| `startsWith()` | Check beginning |
| `endsWith()` | Check ending |
| `indexOf()` | Find index |
| `slice()` | Extract part |
| `substring()` | Extract part |
| `replace()` | Replace text |
| `split()` | Convert string to array |

---

# 31. Important Concepts

- Strings represent text.
- String indexes start at `0`.
- `length` gives the number of characters.
- Strings are immutable.
- `+` can concatenate strings.
- Backticks create template literals.
- `${}` performs interpolation.
- Expressions can be used inside `${}`.
- Template literals support multiline text.
- String methods create useful transformed or extracted values.

---

# 32. Best Practices

- Use meaningful string variables.
- Use template literals when combining many values.
- Use `trim()` when processing user-entered text.
- Remember that indexes start from `0`.
- Remember that `slice()` excludes the ending index.
- Do not expect string methods to modify the original string.
- Keep text formatting readable.
- Validate and clean user input before processing it.