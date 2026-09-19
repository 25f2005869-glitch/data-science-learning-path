# 🔧 Day 046 — Functions — Detailed Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 046  
**Topic:** Functions

---

# 1. What Is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code repeatedly, we can put it inside a function and call the function whenever required.

Example:

    function greet() {
        console.log("Hello!");
    }

Calling the function:

    greet();

Output:

    Hello!

---

# 2. Why Are Functions Important?

Functions help us:

- Reuse code
- Reduce repetition
- Organize programs
- Make code easier to understand
- Make debugging easier
- Divide large problems into smaller tasks

---

# 3. Function Declaration

A function can be declared using the `function` keyword.

Syntax:

    function functionName() {
        // statements
    }

Example:

    function greet() {
        console.log("Welcome to JavaScript!");
    }

The function does not execute merely because it is declared.

---

# 4. Function Call

A function is executed by calling it.

Example:

    function greet() {
        console.log("Hello Saloni!");
    }

    greet();

The statement:

    greet();

is the function call.

---

# 5. Parameters

Parameters are variables written inside the function definition.

Example:

    function greet(name) {
        console.log("Hello " + name);
    }

Here:

    name

is a parameter.

---

# 6. Arguments

Arguments are the actual values passed to a function when it is called.

Example:

    function greet(name) {
        console.log("Hello " + name);
    }

    greet("Saloni");

Here:

    "Saloni"

is an argument.

### Parameter vs Argument

| Term | Meaning |
|---|---|
| Parameter | Variable in function definition |
| Argument | Actual value passed during function call |

---

# 7. Multiple Parameters

A function can accept multiple parameters.

Example:

    function add(a, b) {
        console.log(a + b);
    }

    add(10, 20);

Output:

    30

Here `a` and `b` are parameters.

`10` and `20` are arguments.

---

# 8. return Statement

The `return` statement sends a value back from a function.

Example:

    function add(a, b) {
        return a + b;
    }

    const result = add(10, 20);

    console.log(result);

Output:

    30

The returned value can be stored in a variable.

---

# 9. return Stops Function Execution

When JavaScript reaches `return`, the function immediately finishes.

Example:

    function test() {
        return "Done";

        console.log("This will not execute");
    }

The statement after `return` is unreachable.

---

# 10. Function Without return

A function does not always need to return a value.

Example:

    function showMessage() {
        console.log("Learning JavaScript");
    }

    showMessage();

This function performs an action but does not explicitly return a value.

---

# 11. Function with return vs console.log

`console.log()` displays a value.

`return` sends a value back to the place where the function was called.

Example:

    function add(a, b) {
        return a + b;
    }

    const result = add(5, 10);

    console.log(result);

Returning values makes functions more reusable.

---

# 12. Default Parameters

A parameter can have a default value.

Example:

    function greet(name = "Student") {
        console.log("Hello " + name);
    }

    greet();

Output:

    Hello Student

If an argument is provided, it replaces the default value.

    greet("Saloni");

Output:

    Hello Saloni

---

# 13. Function Expression

A function can be stored in a variable.

Example:

    const add = function(a, b) {
        return a + b;
    };

    console.log(add(5, 3));

This is called a function expression.

---

# 14. Arrow Functions

Arrow functions provide a shorter syntax for functions.

Example:

    const add = (a, b) => {
        return a + b;
    };

Short form:

    const add = (a, b) => a + b;

Arrow functions are widely used in modern JavaScript.

---

# 15. Arrow Function with One Parameter

Parentheses can usually be omitted for one parameter.

Example:

    const square = number => number * number;

Calling:

    console.log(square(5));

Output:

    25

Using parentheses is also valid:

    const square = (number) => number * number;

---

# 16. Function Scope

Variables declared inside a function are generally local to that function.

Example:

    function test() {
        let message = "Hello";
        console.log(message);
    }

    test();

The variable `message` cannot normally be accessed outside the function.

---

# 17. Global Variables

A variable declared outside a function can be accessible inside the function.

Example:

    const programme = "IIT Madras BS Degree";

    function showProgramme() {
        console.log(programme);
    }

    showProgramme();

However, unnecessary global variables should be avoided.

---

# 18. Functions with Conditions

Functions can contain conditional statements.

Example:

    function checkResult(marks) {
        if (marks >= 40) {
            return "Pass";
        } else {
            return "Fail";
        }
    }

    console.log(checkResult(75));

Output:

    Pass

---

# 19. Functions with Loops

Functions can also contain loops.

Example:

    function printNumbers(limit) {
        for (let i = 1; i <= limit; i++) {
            console.log(i);
        }
    }

    printNumbers(5);

This combines functions and loops.

---

# 20. Reusable Calculation Function

Example:

    function calculateAverage(a, b, c) {
        return (a + b + c) / 3;
    }

    const average = calculateAverage(80, 90, 70);

    console.log(average);

The same function can be reused with different values.

---

# 21. Function Calling Another Function

One function can call another function.

Example:

    function add(a, b) {
        return a + b;
    }

    function showResult() {
        const result = add(10, 20);
        console.log(result);
    }

    showResult();

This allows programs to be divided into smaller reusable functions.

---

# 22. Function Naming

Use meaningful names.

Good examples:

    calculateTotal()
    calculateAverage()
    checkResult()
    displayStudent()
    validateForm()

Avoid unclear names such as:

    x()
    abc()
    test123()

unless the purpose is obvious from context.

---

# 23. Common Mistakes

### Mistake 1: Forgetting to call the function

Declaration:

    function greet() {
        console.log("Hello");
    }

The function needs to be called:

    greet();

### Mistake 2: Forgetting return

Incorrect:

    function add(a, b) {
        a + b;
    }

Correct:

    function add(a, b) {
        return a + b;
    }

### Mistake 3: Calling with wrong arguments

Always check what values the function expects.

### Mistake 4: Making functions too large

A function should ideally perform one clear responsibility.

---

# 24. Function Declaration vs Function Expression

### Function Declaration

    function add(a, b) {
        return a + b;
    }

### Function Expression

    const add = function(a, b) {
        return a + b;
    };

Both can perform the same task but have different syntax and behavior around hoisting.

---

# 25. Arrow Function

Normal function:

    function square(x) {
        return x * x;
    }

Arrow function:

    const square = x => x * x;

Arrow functions are concise and especially common in modern JavaScript.

---

# 26. Function Execution Flow

For:

    function add(a, b) {
        return a + b;
    }

    const result = add(10, 20);

The basic flow is:

1. Function is defined.
2. Function is called.
3. Arguments are passed.
4. Parameters receive the values.
5. Function body executes.
6. `return` sends the result back.
7. Result is stored in `result`.

---

# 27. Important Concepts

- Function = reusable block of code.
- Declaration defines a function.
- Call executes a function.
- Parameter = variable in definition.
- Argument = value passed during call.
- `return` sends a value back.
- Function expressions store functions in variables.
- Arrow functions provide concise syntax.
- Functions can contain conditions and loops.
- Local variables belong to their function scope.
- Good functions should have clear responsibilities.

---

# 28. Best Practices

- Give functions meaningful names.
- Keep functions focused on one task.
- Avoid unnecessary global variables.
- Use parameters instead of hard-coded values.
- Return values when the result needs to be reused.
- Keep functions readable and reasonably small.
- Use `const` for function expressions when the variable is not reassigned.
- Choose normal or arrow functions based on the required behavior and context.