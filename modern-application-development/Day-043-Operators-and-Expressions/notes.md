# 📝 Day 043 — Operators and Expressions Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 043  
**Topic:** Operators and Expressions

---

# 1. What is an Operator?

An operator is a symbol or keyword that performs an operation on one or more values.

Example:

    10 + 20

Here:

- `10` → operand
- `+` → operator
- `20` → operand

Result:

    30

---

# 2. What is an Operand?

An operand is a value on which an operator works.

Example:

    10 + 20

There are two operands:

    10
    20

The operator is:

    +

---

# 3. What is an Expression?

An expression is a piece of JavaScript code that produces a value.

Examples:

    10 + 20

    50 * 2

    age >= 18

    "Hello " + name

Expressions can be used inside statements.

Example:

    console.log(10 + 20);

---

# 4. Arithmetic Operators

Arithmetic operators are used for mathematical calculations.

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Remainder |
| `**` | Exponentiation |

Examples:

    10 + 5
    10 - 5
    10 * 5
    10 / 5
    10 % 3
    2 ** 3

---

# 5. Addition

The `+` operator performs addition when used with numbers.

Example:

    let total = 10 + 20;

Result:

    30

---

# 6. Subtraction

The `-` operator subtracts one number from another.

Example:

    let result = 50 - 20;

Result:

    30

---

# 7. Multiplication

The `*` operator performs multiplication.

Example:

    let total = 10 * 5;

Result:

    50

---

# 8. Division

The `/` operator performs division.

Example:

    let result = 20 / 5;

Result:

    4

JavaScript numbers use floating-point arithmetic, so division can produce decimal values.

Example:

    5 / 2

Result:

    2.5

---

# 9. Remainder Operator

The `%` operator returns the remainder after division.

Example:

    10 % 3

Result:

    1

Another example:

    20 % 5

Result:

    0

The remainder operator is useful for checking divisibility and even/odd values.

---

# 10. Exponentiation

The `**` operator raises a number to a power.

Example:

    2 ** 3

Result:

    8

Because:

    2 × 2 × 2 = 8

---

# 11. Assignment Operator

The basic assignment operator is:

    =

Example:

    let score = 90;

The value `90` is assigned to `score`.

Assignment is not the same as equality comparison.

---

# 12. Compound Assignment Operators

Compound assignment operators combine an operation with assignment.

Examples:

    +=
    -=
    *=
    /=
    %=
    **=

Example:

    let score = 100;

    score += 10;

Now:

    score = 110

---

# 13. Addition Assignment

Example:

    let x = 10;

    x += 5;

Equivalent to:

    x = x + 5;

---

# 14. Subtraction Assignment

Example:

    let x = 10;

    x -= 3;

Equivalent to:

    x = x - 3;

Result:

    7

---

# 15. Multiplication Assignment

Example:

    let x = 10;

    x *= 2;

Equivalent to:

    x = x * 2;

Result:

    20

---

# 16. Division Assignment

Example:

    let x = 20;

    x /= 4;

Equivalent to:

    x = x / 4;

Result:

    5

---

# 17. Comparison Operators

Comparison operators compare values and produce a Boolean result.

Important operators:

    >
    <
    >=
    <=
    ==
    ===
    !=
    !==

Examples:

    10 > 5
    10 < 5
    10 >= 10

The result is:

    true

or:

    false

---

# 18. Greater Than

    10 > 5

Result:

    true

---

# 19. Less Than

    10 < 5

Result:

    false

---

# 20. Greater Than or Equal To

    10 >= 10

Result:

    true

---

# 21. Less Than or Equal To

    10 <= 10

Result:

    true

---

# 22. Equality: `==`

The loose equality operator compares values after allowing type coercion.

Example:

    5 == "5"

Result:

    true

This happens because JavaScript converts values during the comparison.

---

# 23. Strict Equality: `===`

The strict equality operator compares both value and type.

Example:

    5 === "5"

Result:

    false

Because:

    5 → number
    "5" → string

In modern JavaScript, prefer `===` in most situations.

---

# 24. Loose Inequality: `!=`

The `!=` operator checks whether values are not equal after type coercion.

Example:

    5 != "6"

Result:

    true

---

# 25. Strict Inequality: `!==`

The `!==` operator checks whether value or type is different.

Example:

    5 !== "5"

Result:

    true

Because the types are different.

---

# 26. Logical Operators

Logical operators work with Boolean conditions.

Main operators:

    &&
    ||
    !

---

# 27. Logical AND `&&`

AND returns true when both conditions are true.

Example:

    age >= 18 && hasID === true

Both conditions must be true.

Truth table:

| A | B | A && B |
|---|---|---|
| true | true | true |
| true | false | false |
| false | true | false |
| false | false | false |

---

# 28. Logical OR `||`

OR returns true when at least one condition is true.

Example:

    isStudent || isTeacher

Truth table:

| A | B | A \|\| B |
|---|---|---|
| true | true | true |
| true | false | true |
| false | true | true |
| false | false | false |

---

# 29. Logical NOT `!`

NOT reverses a Boolean value.

Example:

    !true

Result:

    false

And:

    !false

Result:

    true

---

# 30. Increment Operator

The `++` operator increases a value by one.

Example:

    let count = 5;

    count++;

Result:

    6

Equivalent to:

    count = count + 1;

---

# 31. Decrement Operator

The `--` operator decreases a value by one.

Example:

    let count = 5;

    count--;

Result:

    4

Equivalent to:

    count = count - 1;

---

# 32. Prefix and Postfix

Increment and decrement can be used before or after a variable.

### Prefix

    ++x

The value is incremented before it is used in the expression.

### Postfix

    x++

The current value is used first, then incremented.

Example:

    let x = 5;
    let y = ++x;

Now:

    x = 6
    y = 6

Postfix example:

    let x = 5;
    let y = x++;

Now:

    x = 6
    y = 5

---

# 33. String Concatenation

The `+` operator can combine strings.

Example:

    let firstName = "Saloni";
    let message = "Hello " + firstName;

Result:

    Hello Saloni

---

# 34. Template Literals

Template literals use backticks.

Example:

    const name = "Saloni";
    const age = 17;

    const message = `My name is ${name} and I am ${age} years old.`;

Template literals are often easier to read than repeated string concatenation.

---

# 35. Unary Operators

A unary operator works with one operand.

Examples include:

    typeof value
    !value
    -value
    +value

Example:

    -10

The unary minus changes the sign.

---

# 36. `typeof` Operator

`typeof` returns a string describing the type of a value.

Examples:

    typeof 10

Result:

    "number"

    typeof "Hello"

Result:

    "string"

---

# 37. Ternary Operator

The conditional or ternary operator is a compact way to choose between two expressions.

Syntax:

    condition ? valueIfTrue : valueIfFalse

Example:

    let age = 20;

    let status = age >= 18 ? "Adult" : "Minor";

Result:

    Adult

The ternary operator is useful for simple conditions.

Complex logic should usually use `if...else`.

---

# 38. Operator Precedence

When multiple operators appear in one expression, JavaScript follows precedence rules.

Example:

    10 + 5 * 2

Multiplication is performed first.

Result:

    20

Not:

    30

---

# 39. Parentheses

Parentheses can be used to make the intended order explicit.

Example:

    (10 + 5) * 2

Result:

    30

Compare:

    10 + 5 * 2

Result:

    20

Use parentheses when they improve clarity.

---

# 40. Common Precedence Idea

A simplified order is:

    Parentheses
       ↓
    Exponentiation
       ↓
    Multiplication / Division / Remainder
       ↓
    Addition / Subtraction
       ↓
    Comparisons
       ↓
    Logical AND
       ↓
    Logical OR
       ↓
    Conditional
       ↓
    Assignment

This is a simplified learning model. JavaScript has more detailed precedence rules.

---

# 41. Short-Circuit Evaluation

Logical operators can stop evaluating as soon as the final result is known.

For AND:

    false && anything

The second operand may not need to be evaluated.

For OR:

    true || anything

The second operand may not need to be evaluated.

This behavior is called short-circuit evaluation.

---

# 42. Truthy and Falsy Basics

JavaScript converts values to Boolean in Boolean contexts.

Common falsy values include:

    false
    0
    -0
    0n
    ""
    null
    undefined
    NaN

Most other values are truthy.

This concept becomes important when using logical operators and conditions.

---

# 43. Common Mistakes

### Mistake 1

Using `=` instead of comparison:

    if (age = 18)

Assignment and comparison are different operations.

### Mistake 2

Using `==` when strict comparison is preferred:

    5 == "5"

Prefer:

    5 === "5"

### Mistake 3

Forgetting operator precedence.

### Mistake 4

Confusing `%` with percentage.

In JavaScript `%` is the remainder operator.

### Mistake 5

Confusing `++x` and `x++`.

---

# 44. Best Practices

- Prefer `===` and `!==` for comparisons.
- Use parentheses when expressions become difficult to read.
- Use meaningful variable names.
- Avoid unnecessarily complex expressions.
- Understand operator precedence.
- Use template literals for readable string interpolation.
- Use ternary expressions only for simple conditions.
- Keep calculations readable.

---

# 📌 Day 043 Summary

Today I learned:

- Operators
- Operands
- Expressions
- Arithmetic operators
- Assignment operators
- Compound assignment
- Comparison operators
- Loose equality
- Strict equality
- Logical operators
- Increment
- Decrement
- Prefix and postfix
- String concatenation
- Template literals
- Unary operators
- Ternary operator
- Operator precedence
- Short-circuit evaluation
- Truthy and falsy basics

Next, I will learn conditional statements.