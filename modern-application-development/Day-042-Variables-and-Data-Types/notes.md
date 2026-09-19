# 📝 Day 042 — Variables and Data Types Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 042  
**Topic:** Variables and Data Types

---

# 1. What is a Variable?

A variable is a named reference used to store or hold a value.

Example:

    let studentName = "Saloni";

Here:

- `let` → keyword
- `studentName` → variable name
- `"Saloni"` → value
- `=` → assignment operator

A variable allows us to reuse data in our program.

Example:

    let marks = 95;

    console.log(marks);

---

# 2. Why Do We Need Variables?

Variables help us:

- Store information
- Reuse values
- Modify data
- Perform calculations
- Write dynamic programs
- Make code easier to understand

Example:

    let price = 500;
    let quantity = 2;

    let total = price * quantity;

---

# 3. Variable Declaration

Declaration means creating a variable.

Example:

    let name;

The variable exists but no value has been explicitly assigned to it.

Its value is:

    undefined

---

# 4. Initialization

Initialization means assigning an initial value to a variable.

Example:

    let name = "Saloni";

The variable is declared and initialized in the same statement.

---

# 5. Assignment

Assignment means giving or changing a value.

Example:

    let score = 80;

    score = 95;

The second statement changes the value of `score`.

---

# 6. `let`

`let` is used to declare variables whose values may change.

Example:

    let score = 80;

    score = 90;

This is valid.

`let` is block-scoped.

Example:

    {
        let message = "Hello";
    }

The variable `message` is available only inside that block.

---

# 7. `const`

`const` is used when a variable binding should not be reassigned.

Example:

    const pi = 3.14159;

The following is not allowed:

    pi = 4;

A `const` variable must be initialized when declared.

This is invalid:

    const name;

---

# 8. `var`

`var` is the older way of declaring variables.

Example:

    var name = "Saloni";

Modern JavaScript generally prefers:

    let
    const

instead of `var`.

One important difference is that `var` is function-scoped rather than block-scoped.

---

# 9. `let` vs `const` vs `var`

| Keyword | Reassignment | Scope | Modern Recommendation |
|---|---|---|---|
| `let` | Allowed | Block | Use when value changes |
| `const` | Not allowed | Block | Prefer by default |
| `var` | Allowed | Function | Usually avoid in modern code |

A useful rule:

    Use const by default.
    Use let when reassignment is required.
    Avoid var in modern JavaScript unless you specifically need its behavior.

---

# 10. Variable Naming Rules

JavaScript identifiers can contain:

- Letters
- Digits
- `_`
- `$`

Rules:

- Cannot start with a digit.
- Cannot contain spaces.
- Cannot use reserved keywords.
- JavaScript is case-sensitive.

Valid examples:

    studentName
    totalMarks
    _count
    $price
    score2

Invalid examples:

    2score
    student name
    let

---

# 11. Naming Conventions

JavaScript commonly uses camelCase.

Example:

    firstName
    totalMarks
    studentAge
    calculateTotal

Meaningful names are better than unclear names.

Prefer:

    let totalMarks = 450;

instead of:

    let x = 450;

---

# 12. What is a Data Type?

A data type describes the kind of value stored or represented by JavaScript.

Examples:

    "Saloni" → String
    100 → Number
    true → Boolean

JavaScript has primitive and non-primitive/reference values.

---

# 13. Primitive Data Types

The main primitive types are:

1. String
2. Number
3. BigInt
4. Boolean
5. Undefined
6. Null
7. Symbol

Objects are non-primitive/reference values.

---

# 14. String

A string represents text.

Examples:

    let name = "Saloni";

    let course = 'JavaScript';

Strings can use:

- Double quotes
- Single quotes
- Backticks

Example:

    let message = `Hello`;

---

# 15. Number

JavaScript uses the `number` type for both integers and floating-point numbers.

Examples:

    let age = 17;
    let price = 99.99;
    let temperature = -5;

JavaScript does not have separate `int` and `float` primitive types.

---

# 16. Special Number Values

JavaScript numbers can also represent special values.

Examples:

    Infinity
    -Infinity
    NaN

`NaN` means "Not a Number".

Example:

    console.log("hello" * 5);

This produces `NaN`.

---

# 17. Boolean

Boolean values represent logical states.

There are only two Boolean values:

    true
    false

Example:

    let isStudent = true;

    let isLoggedIn = false;

---

# 18. Undefined

`undefined` usually means that a value has not been assigned.

Example:

    let result;

    console.log(result);

Output:

    undefined

---

# 19. Null

`null` represents an intentional absence of a value.

Example:

    let selectedUser = null;

This means there is currently no selected user.

Important distinction:

    undefined → value is not assigned
    null → absence of value is intentional

---

# 20. BigInt

`BigInt` is used for integers larger than the safe integer range of the regular `Number` type.

Example:

    let largeNumber = 123456789012345678901234567890n;

The `n` at the end creates a BigInt literal.

BigInt should not be mixed directly with ordinary Number values in arithmetic.

---

# 21. Symbol

A Symbol creates a unique primitive value.

Example:

    const id = Symbol("id");

Symbols are often useful when creating unique object property keys.

They are an advanced topic and will be used less frequently in basic frontend development.

---

# 22. Object

Objects store collections of related data.

Example:

    const student = {
        name: "Saloni",
        age: 17,
        course: "Data Science"
    };

Objects are non-primitive/reference values.

Arrays and functions are also objects in JavaScript's type system.

---

# 23. Array

An array stores an ordered collection of values.

Example:

    const skills = [
        "Python",
        "SQL",
        "HTML",
        "CSS"
    ];

Arrays will be studied in greater detail later.

---

# 24. Function

Functions are reusable blocks of code.

Example:

    function greet() {
        console.log("Hello");
    }

Functions are objects in JavaScript.

Functions will be studied in detail later.

---

# 25. `typeof`

The `typeof` operator can be used to determine the type of a value.

Examples:

    typeof "Hello"

    typeof 100

    typeof true

Expected results:

    "string"
    "number"
    "boolean"

---

# 26. `typeof` Examples

Example:

    console.log(typeof "Saloni");

Output:

    string

Example:

    console.log(typeof 25);

Output:

    number

Example:

    console.log(typeof true);

Output:

    boolean

---

# 27. Important `typeof` Cases

For an undeclared identifier, using `typeof` does not normally throw a ReferenceError:

    typeof unknownVariable

Result:

    "undefined"

A well-known JavaScript historical quirk is:

    typeof null

Result:

    "object"

Although `null` is a primitive value, `typeof null` returns `"object"`.

---

# 28. Dynamic Typing

JavaScript is dynamically typed.

This means a variable does not have to permanently hold values of only one type.

Example:

    let value = 100;

    value = "Hello";

    value = true;

This is allowed.

The current value determines the runtime type.

---

# 29. Static vs Dynamic Typing

### Static typing

A variable's type is generally checked and constrained more strictly by the language/type system.

### Dynamic typing

A variable can hold values of different types at different times.

JavaScript is dynamically typed.

---

# 30. Type Conversion

Type conversion means converting a value from one type to another.

Examples:

    Number("100")

    String(100)

    Boolean(1)

Example:

    let value = "100";

    let numberValue = Number(value);

---

# 31. Explicit Type Conversion

When the programmer intentionally converts a value, it is explicit conversion.

Common functions:

    Number()
    String()
    Boolean()

Example:

    Number("50")

Result:

    50

---

# 32. Type Coercion

JavaScript can sometimes automatically convert values during operations.

Example:

    "10" + 5

The result is:

    "105"

The number is converted to a string for string concatenation.

Type coercion will be studied more deeply with operators.

---

# 33. `const` with Objects

`const` prevents reassignment of the variable binding.

It does not make the entire object immutable.

Example:

    const student = {
        name: "Saloni"
    };

This is allowed:

    student.name = "Student";

But this is not:

    student = {};

The distinction between binding and object mutation is important.

---

# 34. Variable Scope

Scope determines where a variable can be accessed.

Important scopes include:

- Block scope
- Function scope
- Global scope

`let` and `const` are block-scoped.

`var` is function-scoped.

Scope will be studied in greater detail with functions.

---

# 35. Best Practices

Prefer:

    const name = "Saloni";

Use:

    let score = 90;
    score = 95;

when reassignment is necessary.

Avoid unnecessary:

    var

Use meaningful names.

Prefer:

    totalMarks

over:

    x

Keep naming consistent.

---

# 36. Common Mistakes

### Mistake 1

Trying to reassign a `const` variable:

    const age = 17;
    age = 18;

### Mistake 2

Declaring `const` without initialization:

    const name;

### Mistake 3

Using invalid identifiers:

    let 2name = "Saloni";

### Mistake 4

Confusing `null` and `undefined`.

### Mistake 5

Assuming JavaScript has separate primitive `int` and `float` types.

---

# 37. Final Mental Model

Think of a variable as a named reference to a value.

    Variable
       ↓
    Value
       ↓
    Data Type

Example:

    let age = 17;

    age
     ↓
    17
     ↓
    number

---

# 📌 Day 042 Summary

Today I learned:

- Variables
- Declaration
- Initialization
- Assignment
- `let`
- `const`
- `var`
- Naming rules
- Naming conventions
- Primitive data types
- String
- Number
- Boolean
- Undefined
- Null
- BigInt
- Symbol
- Objects
- Arrays
- Functions
- `typeof`
- Dynamic typing
- Type conversion
- Type coercion basics

Next, I will learn JavaScript operators and expressions.