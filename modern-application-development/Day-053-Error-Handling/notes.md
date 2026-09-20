# 📝 Day 053 — Error Handling — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 053  
**Topic:** Error Handling

---

# 1. What is an Error?

An error is a problem that occurs while writing or executing a program.

Errors can prevent JavaScript from producing the expected result.

Example:

    console.log(name);

If `name` has not been declared, JavaScript produces a `ReferenceError`.

---

# 2. Why Error Handling is Important

Error handling helps us:

- Detect problems
- Prevent application crashes
- Display useful messages
- Recover from expected failures
- Debug programs
- Improve user experience

---

# 3. Types of Programming Errors

Three common categories are:

1. Syntax Errors
2. Runtime Errors
3. Logical Errors

---

# 4. Syntax Error

A syntax error occurs when JavaScript code does not follow valid language syntax.

Example:

    if (true {
        console.log("Hello");
    }

The JavaScript engine cannot correctly parse this code.

Syntax errors usually need to be fixed before the program can execute normally.

---

# 5. Runtime Error

A runtime error occurs while the program is executing.

Example:

    const student = null;

    console.log(student.name);

Trying to access `name` from `null` causes a `TypeError`.

Runtime errors can often be handled using `try...catch`.

---

# 6. Logical Error

A logical error occurs when the program runs but produces an incorrect result.

Example:

    const marks = 80;
    const total = 100;

    const percentage = marks / total;

If the intention was to calculate percentage, the correct formula should multiply by 100.

Logical errors generally do not automatically throw JavaScript exceptions.

---

# 7. try...catch

`try...catch` allows a program to handle certain runtime errors.

Basic structure:

    try {
        // Code that may produce an error
    } catch (error) {
        // Handle the error
    }

---

# 8. Example of try...catch

    try {
        console.log(studentName);
    } catch (error) {
        console.log("An error occurred.");
    }

If `studentName` is not defined, the error is caught instead of stopping the rest of the surrounding script.

---

# 9. The catch Parameter

The `catch` block can receive an error object.

Example:

    try {
        console.log(unknownVariable);
    } catch (error) {
        console.log(error);
    }

The error object contains information about the problem.

---

# 10. error.name

The `name` property identifies the type of error.

Example:

    try {
        console.log(unknownVariable);
    } catch (error) {
        console.log(error.name);
    }

Possible result:

    ReferenceError

---

# 11. error.message

The `message` property describes the error.

Example:

    try {
        console.log(unknownVariable);
    } catch (error) {
        console.log(error.message);
    }

The exact message can vary between JavaScript environments.

---

# 12. error.stack

The `stack` property can provide information about where the error occurred.

Example:

    try {
        throw new Error("Something went wrong");
    } catch (error) {
        console.log(error.stack);
    }

The exact stack format depends on the browser or JavaScript runtime.

---

# 13. finally

The `finally` block runs after the `try` and `catch` process finishes.

Basic structure:

    try {
        // Attempt operation
    } catch (error) {
        // Handle error
    } finally {
        // Cleanup
    }

---

# 14. Example of finally

    try {
        console.log("Trying...");
    } catch (error) {
        console.log("Error handled");
    } finally {
        console.log("This always runs");
    }

`finally` is useful for cleanup operations.

---

# 15. Why Use finally?

Typical uses include:

- Closing resources
- Resetting application state
- Hiding loading indicators
- Cleaning temporary data
- Releasing resources

---

# 16. throw

The `throw` statement allows us to create our own exceptions.

Example:

    throw new Error("Invalid score");

This immediately transfers control to an appropriate `catch` block when one exists.

---

# 17. throw with try...catch

Example:

    try {
        throw new Error("Invalid marks");
    } catch (error) {
        console.log(error.message);
    }

Output:

    Invalid marks

---

# 18. Creating an Error Object

The standard `Error` constructor can create an error.

Example:

    const error = new Error("Something went wrong");

    console.log(error.message);

---

# 19. Custom Validation Error

We can validate input and throw an error when it is invalid.

Example:

    function checkMarks(marks) {
        if (marks < 0 || marks > 100) {
            throw new Error("Marks must be between 0 and 100");
        }

        return "Valid marks";
    }

---

# 20. Common Error Types

JavaScript provides several built-in error types.

Common examples:

- `Error`
- `SyntaxError`
- `ReferenceError`
- `TypeError`
- `RangeError`
- `URIError`
- `EvalError`

Some errors are much more commonly encountered in everyday development than others.

---

# 21. ReferenceError

A `ReferenceError` occurs when JavaScript cannot find a referenced variable or binding.

Example:

    console.log(studentName);

If `studentName` has not been declared, a `ReferenceError` occurs.

---

# 22. TypeError

A `TypeError` occurs when an operation is performed on a value of an inappropriate type.

Example:

    const student = null;

    console.log(student.name);

Accessing a property on `null` causes a `TypeError`.

Another example:

    const number = 10;

    number.toUpperCase();

A number does not provide the expected string method.

---

# 23. RangeError

A `RangeError` occurs when a value is outside an allowed range.

Example:

    const numbers = new Array(-1);

This produces a `RangeError`.

---

# 24. SyntaxError

A `SyntaxError` indicates invalid JavaScript syntax.

Example:

    JSON.parse("{name:");

The string is not valid JSON, so parsing throws a `SyntaxError`.

---

# 25. URIError

A `URIError` can occur when URI-related functions receive invalid input.

Example:

    decodeURIComponent("%");

This can produce a `URIError`.

---

# 26. Error Hierarchy

Many built-in JavaScript errors inherit from `Error`.

Conceptually:

    Error
    ├── SyntaxError
    ├── ReferenceError
    ├── TypeError
    ├── RangeError
    └── URIError

---

# 27. Multiple catch Behaviors

JavaScript uses one `catch` block for a given `try` statement.

We can inspect `error.name` to handle different error types.

Example:

    try {
        JSON.parse("invalid");
    } catch (error) {
        if (error.name === "SyntaxError") {
            console.log("Invalid JSON");
        }
    }

---

# 28. Catch Without Binding

Modern JavaScript allows the catch parameter to be omitted when the error object is not needed.

Example:

    try {
        JSON.parse("invalid");
    } catch {
        console.log("Invalid data");
    }

---

# 29. Nested try...catch

A `try...catch` can exist inside another `try` block.

Example:

    try {
        try {
            throw new Error("Inner error");
        } catch (error) {
            console.log("Inner error handled");
        }
    } catch (error) {
        console.log("Outer error handled");
    }

---

# 30. Error Propagation

If an error is not handled by the current `try...catch`, it can propagate to an outer caller.

Example:

    function test() {
        throw new Error("Problem");
    }

    try {
        test();
    } catch (error) {
        console.log(error.message);
    }

The error thrown inside `test()` is handled by the surrounding `catch`.

---

# 31. Return in finally

A `finally` block runs even when control leaves the `try` or `catch`.

However, using `return` inside `finally` is usually discouraged because it can override earlier return values or even suppress an exception.

Prefer using `finally` for cleanup rather than returning values.

---

# 32. Error Handling with Functions

Example:

    function calculatePercentage(marks, total) {
        if (total <= 0) {
            throw new Error("Total must be greater than zero");
        }

        return (marks / total) * 100;
    }

    try {
        console.log(calculatePercentage(90, 100));
    } catch (error) {
        console.log(error.message);
    }

---

# 33. Error Handling with JSON

JSON parsing is a common situation where runtime errors can occur.

Example:

    try {
        const data = JSON.parse('{"name":"Saloni"}');
        console.log(data.name);
    } catch (error) {
        console.log("Invalid JSON");
    }

---

# 34. Defensive Programming

Defensive programming means writing code that anticipates possible invalid inputs or unexpected situations.

Examples:

- Validate user input
- Check required values
- Handle missing data
- Validate ranges
- Use `try...catch` where exceptions are expected
- Provide useful error messages

---

# 35. Do Not Hide Errors

Avoid catching errors and doing nothing.

Poor approach:

    try {
        riskyOperation();
    } catch {
    }

This makes debugging difficult.

Better:

    try {
        riskyOperation();
    } catch (error) {
        console.error("Operation failed:", error.message);
    }

---

# 36. console.error()

`console.error()` is useful for displaying errors in the browser console.

Example:

    console.error("Something went wrong");

It is generally preferable to `console.log()` when reporting an actual error.

---

# 37. User-Friendly Error Messages

Technical errors should not always be shown directly to users.

Instead of exposing internal details:

    Database connection failed at internal server...

A user-facing application might display:

    "We could not load your data. Please try again."

Developers can log technical details separately.

---

# 38. Best Practices

- Use `try...catch` for operations that may reasonably throw.
- Validate input before processing it.
- Throw meaningful `Error` objects.
- Use specific error types when appropriate.
- Use `finally` for cleanup.
- Do not silently ignore errors.
- Use `console.error()` for debugging errors.
- Keep error messages clear.
- Do not expose sensitive implementation details to users.
- Do not use exceptions for normal program flow.
- Fix the underlying problem instead of only hiding the error.

---

# 39. Key Difference

Remember:

    Syntax Error
        ↓
    Invalid JavaScript syntax

    Runtime Error
        ↓
    Problem while executing

    Logical Error
        ↓
    Program runs but result is wrong

    try...catch
        ↓
    Handle certain runtime exceptions

    throw
        ↓
    Create/raise an exception

    finally
        ↓
    Cleanup code that runs afterward