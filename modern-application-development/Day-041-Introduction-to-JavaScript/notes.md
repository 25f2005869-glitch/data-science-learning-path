# 📝 Day 041 — Introduction to JavaScript Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 041  
**Topic:** Introduction to JavaScript

---

# 1. What is JavaScript?

JavaScript is a high-level programming language mainly used to add behavior and interactivity to web pages.

HTML provides structure.

CSS provides presentation.

JavaScript provides behavior.

A simple mental model:

    HTML
      ↓
    Structure

    CSS
      ↓
    Appearance

    JavaScript
      ↓
    Behavior

Example:

A button can be created with HTML.

CSS can make the button look attractive.

JavaScript can make something happen when the button is clicked.

---

# 2. Why Do We Need JavaScript?

HTML and CSS alone can create static interfaces, but JavaScript allows a webpage to respond to user actions and process information.

JavaScript can be used for:

- Button interactions
- Form validation
- Calculations
- Dynamic content
- Menus
- Image sliders
- Web applications
- API communication
- Browser storage
- DOM manipulation
- Events

---

# 3. HTML vs CSS vs JavaScript

| Technology | Main Responsibility |
|---|---|
| HTML | Structure |
| CSS | Styling |
| JavaScript | Behavior |

Example:

    HTML → Create a button
    CSS → Style the button
    JavaScript → Respond to button click

---

# 4. JavaScript in Web Development

JavaScript can run inside a web browser.

Typical flow:

    User
      ↓
    Browser
      ↓
    HTML + CSS + JavaScript
      ↓
    Interactive Web Page

JavaScript can interact with the webpage after it has been loaded.

---

# 5. Client-Side JavaScript

When JavaScript runs inside the user's browser, it is called client-side JavaScript.

Examples:

- Changing webpage content
- Validating a form
- Responding to clicks
- Showing or hiding elements
- Changing styles
- Performing calculations

---

# 6. JavaScript Engine

Browsers use JavaScript engines to execute JavaScript code.

Examples:

- Chrome → V8
- Firefox → SpiderMonkey
- Safari → JavaScriptCore

The engine reads and executes JavaScript instructions.

---

# 7. Adding JavaScript to HTML

There are three common approaches.

## Inline JavaScript

JavaScript can be written directly inside an HTML attribute.

Example:

    <button onclick="alert('Hello')">Click</button>

Inline JavaScript is useful for simple demonstrations but is generally avoided in larger projects.

---

## Internal JavaScript

JavaScript can be written inside a `<script>` element.

Example:

    <script>
        console.log("Hello JavaScript");
    </script>

---

## External JavaScript

JavaScript can be placed in a separate `.js` file.

Example:

    <script src="script.js"></script>

External JavaScript is generally preferred for maintainable projects.

---

# 8. The `<script>` Element

The `<script>` element is used to include or write JavaScript.

Example:

    <script>
        console.log("Hello");
    </script>

External file:

    <script src="script.js"></script>

---

# 9. Where Should JavaScript Be Loaded?

A script can be placed in the HTML document.

A common modern approach is:

    <script src="script.js" defer></script>

`defer` tells the browser to download the script while parsing HTML and execute it after the document has been parsed.

---

# 10. JavaScript Syntax

JavaScript has rules for writing instructions.

Example:

    console.log("Hello World");

Important concepts include:

- Keywords
- Identifiers
- Values
- Operators
- Expressions
- Statements
- Functions

---

# 11. Statements

A statement represents an instruction.

Example:

    console.log("Hello");

Another example:

    let score = 90;

Statements are executed by the JavaScript engine.

---

# 12. Semicolon

JavaScript supports semicolons at the end of statements.

Example:

    console.log("Hello");

JavaScript also has Automatic Semicolon Insertion.

However, using semicolons consistently can make code easier to read.

---

# 13. Comments

Comments are ignored during normal execution.

## Single-line comment

    // This is a comment

## Multi-line comment

    /*
       This is a
       multi-line comment
    */

Comments are useful for explaining code.

Avoid unnecessary comments that simply repeat what the code already says.

---

# 14. console.log()

`console.log()` prints information to the browser developer console.

Example:

    console.log("Hello JavaScript");

Another example:

    console.log(10 + 20);

The result can be viewed using browser Developer Tools.

---

# 15. Browser Developer Tools

Developer Tools are important for web development.

To open them in most browsers:

    Right Click → Inspect

or:

    F12

The Console tab can be used to execute JavaScript and view output.

---

# 16. Expressions

An expression produces a value.

Examples:

    10 + 20

    "Hello" + " World"

    5 * 4

Expressions can be used inside statements.

Example:

    console.log(10 + 20);

---

# 17. Values

JavaScript works with different kinds of values.

Examples:

    10
    25.5
    "Hello"
    true
    false

More data types will be studied in detail in the next lessons.

---

# 18. Identifiers

Identifiers are names used for programming elements such as variables and functions.

Examples:

    studentName
    totalMarks
    calculateResult

Good identifiers should be:

- Meaningful
- Clear
- Consistent

JavaScript identifiers are case-sensitive.

These are different:

    studentName
    StudentName

---

# 19. Case Sensitivity

JavaScript is case-sensitive.

Example:

    let name = "Saloni";

`name` and `Name` are different identifiers.

Therefore, consistent naming is important.

---

# 20. JavaScript Execution

A simplified execution process:

    1. Browser loads HTML.
    2. Browser encounters JavaScript.
    3. JavaScript engine processes the code.
    4. Instructions are executed.
    5. Output or changes are produced.

---

# 21. JavaScript Can Modify a Webpage

JavaScript can interact with HTML elements.

For example:

    document.getElementById("title")

This allows JavaScript to find an HTML element.

DOM manipulation will be studied in greater detail later.

---

# 22. JavaScript and Events

An event is an action or occurrence that JavaScript can respond to.

Examples:

- Click
- Input
- Submit
- Mouse movement
- Keyboard input
- Page loading

Example:

    button.addEventListener("click", function () {
        console.log("Button clicked");
    });

Event handling will be studied later.

---

# 23. JavaScript Is Not Java

JavaScript and Java are different programming languages.

They have different:

- Syntax
- Ecosystems
- Runtime environments
- Use cases
- Language designs

The similar names do not mean they are the same language.

---

# 24. JavaScript in MAD 1

JavaScript is important for Modern Application Development because it connects the static frontend with interactive behavior.

Learning sequence:

    JavaScript Basics
          ↓
    Variables & Data Types
          ↓
    Operators
          ↓
    Conditions
          ↓
    Loops
          ↓
    Functions
          ↓
    Arrays & Objects
          ↓
    DOM
          ↓
    Events
          ↓
    Advanced JavaScript
          ↓
    Flask Integration

---

# 25. First JavaScript Program

Example:

    console.log("Hello, JavaScript!");

The message appears in the browser console.

---

# 26. Important Mental Model

Remember:

    HTML = What is on the page?

    CSS = How does it look?

    JavaScript = What does it do?

This is one of the most important concepts in frontend development.

---

# 27. Best Practices

- Use meaningful names.
- Keep JavaScript readable.
- Prefer external JavaScript for larger projects.
- Use `defer` when appropriate.
- Use comments where they add useful context.
- Test code in Developer Tools.
- Avoid unnecessary inline JavaScript.
- Follow consistent naming conventions.
- Use modern JavaScript syntax.

---

# 📌 Day 041 Summary

Today I learned:

- What JavaScript is
- Why JavaScript is used
- HTML vs CSS vs JavaScript
- Client-side JavaScript
- JavaScript engines
- `<script>`
- Inline JavaScript
- Internal JavaScript
- External JavaScript
- JavaScript syntax
- Statements
- Comments
- Expressions
- `console.log()`
- Browser Developer Tools
- Identifiers
- Case sensitivity
- Basic execution flow

Next, I will learn JavaScript variables and data types.