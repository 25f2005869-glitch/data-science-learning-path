# 📝 Day 044 — Conditional Statements Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 044  
**Topic:** Conditional Statements

---

# 1. What is a Conditional Statement?

A conditional statement allows JavaScript to execute different code depending on whether a condition is true or false.

Basic idea:

    If condition is true
        → do something

    Otherwise
        → do something else

Example:

    if (age >= 18) {
        console.log("Adult");
    }

---

# 2. Why Do We Need Conditions?

Programs often need to make decisions.

Examples:

- Check whether a student passed.
- Check whether a user is logged in.
- Check whether a number is positive.
- Check whether a person is eligible.
- Select a menu option.
- Validate input.

---

# 3. The `if` Statement

The `if` statement executes a block when its condition is truthy.

Syntax:

    if (condition) {
        // code
    }

Example:

    let age = 20;

    if (age >= 18) {
        console.log("Adult");
    }

---

# 4. How `if` Works

Suppose:

    let age = 20;

    if (age >= 18) {
        console.log("Adult");
    }

JavaScript checks:

    age >= 18

The result is:

    true

Therefore, the code inside the `if` block executes.

---

# 5. `if...else`

`if...else` provides two possible paths.

Syntax:

    if (condition) {
        // true block
    } else {
        // false block
    }

Example:

    let age = 16;

    if (age >= 18) {
        console.log("Adult");
    } else {
        console.log("Minor");
    }

---

# 6. `else if`

`else if` is used when there are multiple conditions.

Syntax:

    if (condition1) {
        // block 1
    } else if (condition2) {
        // block 2
    } else {
        // default block
    }

Example:

    let marks = 75;

    if (marks >= 90) {
        console.log("A");
    } else if (marks >= 75) {
        console.log("B");
    } else if (marks >= 50) {
        console.log("C");
    } else {
        console.log("Fail");
    }

JavaScript checks the conditions from top to bottom.

Once a matching condition is found, its block executes and the remaining `else if` blocks are skipped.

---

# 7. Order of Conditions

Condition order matters.

Example:

    let marks = 95;

    if (marks >= 40) {
        console.log("Pass");
    } else if (marks >= 90) {
        console.log("Excellent");
    }

The first condition is already true, so `"Pass"` is printed.

Better:

    if (marks >= 90) {
        console.log("Excellent");
    } else if (marks >= 40) {
        console.log("Pass");
    }

More specific conditions should generally come before broader conditions.

---

# 8. Nested `if`

An `if` statement can exist inside another `if`.

Example:

    if (age >= 18) {

        if (hasID) {
            console.log("Entry allowed");
        }

    }

Nested conditions are useful when one decision depends on another.

Avoid excessive nesting because it can make code difficult to read.

---

# 9. Multiple Conditions

Logical operators can combine conditions.

Example:

    if (age >= 18 && hasID) {
        console.log("Entry allowed");
    }

Both conditions must be truthy.

---

# 10. Logical AND

The `&&` operator means AND.

Example:

    if (age >= 18 && hasID) {
        console.log("Allowed");
    }

Both conditions must be true.

---

# 11. Logical OR

The `||` operator means OR.

Example:

    if (isStudent || isTeacher) {
        console.log("Education access available");
    }

At least one condition must be truthy.

---

# 12. Logical NOT

The `!` operator reverses a Boolean value.

Example:

    let isLoggedIn = false;

    if (!isLoggedIn) {
        console.log("Please log in");
    }

---

# 13. Comparison Operators in Conditions

Conditions commonly use comparison operators.

Examples:

    >
    <
    >=
    <=
    ===
    !==

Example:

    if (score >= 40) {
        console.log("Pass");
    }

---

# 14. Prefer Strict Equality

Use:

    ===

instead of:

    ==

when you want value and type to match.

Example:

    if (age === 18) {
        console.log("Exactly 18");
    }

Strict inequality:

    !==

---

# 15. Truthy Values

JavaScript can use values in Boolean contexts.

Most values are truthy.

Examples:

    true
    "hello"
    100
    []
    {}

An `if` condition can therefore use a value directly.

Example:

    let name = "Saloni";

    if (name) {
        console.log("Name exists");
    }

---

# 16. Falsy Values

Common falsy values are:

    false
    0
    -0
    0n
    ""
    null
    undefined
    NaN

Example:

    let name = "";

    if (name) {
        console.log("Name exists");
    } else {
        console.log("Name is empty");
    }

---

# 17. `switch`

`switch` is useful when one expression needs to be compared against multiple possible values.

Syntax:

    switch (expression) {
        case value1:
            // code
            break;

        case value2:
            // code
            break;

        default:
            // code
    }

---

# 18. `case`

Each `case` represents a possible matching value.

Example:

    let day = 2;

    switch (day) {
        case 1:
            console.log("Monday");
            break;

        case 2:
            console.log("Tuesday");
            break;
    }

---

# 19. `break`

`break` stops execution of the current `switch`.

Example:

    switch (choice) {
        case 1:
            console.log("Option 1");
            break;

        case 2:
            console.log("Option 2");
            break;
    }

Without `break`, execution can continue into later cases. This is called fall-through.

---

# 20. `default`

`default` runs when no case matches.

Example:

    let day = 8;

    switch (day) {
        case 1:
            console.log("Monday");
            break;

        case 2:
            console.log("Tuesday");
            break;

        default:
            console.log("Invalid day");
    }

---

# 21. `switch` Uses Strict Matching

`switch` case matching uses strict comparison semantics.

Example:

    let value = 5;

    switch (value) {
        case "5":
            console.log("String");
            break;

        case 5:
            console.log("Number");
            break;
    }

The output is:

    Number

---

# 22. Multiple Cases

Multiple cases can share the same code.

Example:

    switch (day) {
        case "Saturday":
        case "Sunday":
            console.log("Weekend");
            break;

        default:
            console.log("Weekday");
    }

---

# 23. `if...else` vs `switch`

Use `if...else` when conditions involve ranges or complex logic.

Example:

    if (marks >= 90) {
        ...
    } else if (marks >= 75) {
        ...
    }

Use `switch` when checking one value against several known alternatives.

Example:

    switch (role) {
        case "student":
            ...
            break;

        case "teacher":
            ...
            break;
    }

---

# 24. Ternary Operator

The ternary operator is useful for simple two-way decisions.

Syntax:

    condition ? valueIfTrue : valueIfFalse

Example:

    let result =
        marks >= 40 ? "Pass" : "Fail";

For complex logic, use `if...else`.

---

# 25. Conditional Assignment

A condition can determine which value is assigned.

Example:

    const status =
        age >= 18 ? "Adult" : "Minor";

The variable receives one of the two values.

---

# 26. Conditions with Strings

Conditions can compare strings.

Example:

    const role = "student";

    if (role === "student") {
        console.log("Student account");
    }

Use strict equality for predictable comparisons.

---

# 27. Conditions with Numbers

Example:

    const marks = 82;

    if (marks >= 40) {
        console.log("Pass");
    }

---

# 28. Conditions with Boolean Values

Example:

    const isLoggedIn = true;

    if (isLoggedIn) {
        console.log("Welcome");
    }

There is usually no need to write:

    if (isLoggedIn === true)

The simpler form is normally preferred.

---

# 29. Guard Conditions

A condition can stop an operation when a requirement is not met.

Example:

    if (!username) {
        console.log("Username is required");
    }

This style is useful for validation and early exits.

---

# 30. Combining Conditions

Example:

    const age = 20;
    const isStudent = true;

    if (age >= 18 && isStudent) {
        console.log("Eligible student");
    }

Multiple logical operators can be combined, but overly complex conditions should be simplified when possible.

---

# 31. Operator Precedence in Conditions

Parentheses make complex conditions easier to understand.

Example:

    if ((age >= 18 && hasID) || isAdmin) {
        console.log("Access allowed");
    }

The parentheses make the intended grouping clear.

---

# 32. Common Mistake: Assignment Instead of Comparison

Incorrect:

    if (age = 18) {
        ...
    }

This assigns a value instead of performing the intended equality check.

Use:

    if (age === 18) {
        ...
    }

---

# 33. Common Mistake: Incorrect Range Syntax

Do not write:

    if (40 <= marks <= 100)

This does not work as mathematical chained comparison.

Use:

    if (marks >= 40 && marks <= 100)

---

# 34. Common Mistake: Missing Braces

Although JavaScript allows some single-statement forms without braces, braces improve readability.

Prefer:

    if (age >= 18) {
        console.log("Adult");
    }

---

# 35. Common Mistake: Too Many Nested Conditions

Deep nesting can make logic difficult to understand.

Instead of:

    if (...) {
        if (...) {
            if (...) {
                ...
            }
        }
    }

consider combining conditions or restructuring the logic.

---

# 36. Common Mistake: Forgetting `break`

Incorrect:

    switch (choice) {
        case 1:
            console.log("One");

        case 2:
            console.log("Two");
    }

If `choice` is `1`, both cases can execute because there is no `break`.

---

# 37. Decision-Making Flow

A typical conditional flow:

    Start
      ↓
    Check condition
      ↓
    Is it true?
      ↓
    Yes ──→ Execute block
      │
      No
      ↓
    Check next condition
      ↓
    Else block

---

# 38. Student Result Example

Example:

    const marks = 78;

    if (marks >= 90) {
        console.log("Grade A");
    } else if (marks >= 75) {
        console.log("Grade B");
    } else if (marks >= 50) {
        console.log("Grade C");
    } else if (marks >= 40) {
        console.log("Grade D");
    } else {
        console.log("Fail");
    }

---

# 39. Eligibility Example

Example:

    const age = 20;
    const hasID = true;

    if (age >= 18 && hasID) {
        console.log("Eligible");
    } else {
        console.log("Not eligible");
    }

---

# 40. Best Practices

- Use meaningful conditions.
- Prefer `===` and `!==`.
- Use braces for readability.
- Put specific conditions before broad conditions.
- Use `switch` for discrete known values.
- Use `if...else` for ranges and complex conditions.
- Avoid unnecessary nesting.
- Use parentheses when logic is complex.
- Keep conditions easy to read.

---

# 📌 Day 044 Summary

Today I learned:

- Conditional statements
- `if`
- `if...else`
- `else if`
- Nested `if`
- Comparison operators in conditions
- Logical operators in conditions
- Truthy values
- Falsy values
- `switch`
- `case`
- `break`
- `default`
- Strict matching in `switch`
- Ternary operator
- Decision-making patterns
- Common conditional mistakes
- Conditional best practices

Next, I will learn loops in JavaScript.