# 📝 Day 054 — DOM Introduction — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 054  
**Topic:** DOM Introduction

---

# 1. What is DOM?

DOM stands for Document Object Model.

When a browser loads an HTML document, it creates an in-memory representation of that document.

JavaScript can interact with this representation through the DOM.

In simple terms:

    HTML
      ↓
    Browser
      ↓
    DOM
      ↓
    JavaScript
      ↓
    Change webpage

---

# 2. Why Do We Need the DOM?

HTML creates the structure of a webpage.

CSS controls presentation.

JavaScript provides behavior and interactivity.

The DOM allows JavaScript to communicate with the HTML document.

For example, JavaScript can:

- Change text
- Change styles
- Change attributes
- Add elements
- Remove elements
- Respond to user actions
- Update webpage content

---

# 3. DOM Tree

The DOM represents a document as a tree-like structure.

Example HTML:

    <html>
        <body>
            <h1>Hello</h1>
            <p>Welcome</p>
        </body>
    </html>

Conceptually:

    Document
       |
      html
       |
      body
      /  \
    h1    p

Each part becomes a node in the DOM.

---

# 4. Document Object

The `document` object represents the loaded HTML document.

JavaScript can use `document` to access and manipulate the webpage.

Example:

    console.log(document);

---

# 5. DOM Nodes

The DOM contains different types of nodes.

Common examples include:

- Document node
- Element node
- Text node
- Comment node

An HTML element such as `<p>` is represented as an element node.

The text inside the element is represented as a text node.

---

# 6. DOM Element

An element is an HTML tag represented as an object.

Example:

    <h1 id="title">Hello</h1>

JavaScript can obtain this element and work with it.

---

# 7. Selecting an Element by ID

`getElementById()` selects an element using its `id`.

Example:

    const title = document.getElementById("title");

If an element with that ID exists, the method returns that element.

---

# 8. Example of getElementById()

HTML:

    <h1 id="title">Hello</h1>

JavaScript:

    const title = document.getElementById("title");

    console.log(title);

---

# 9. querySelector()

`querySelector()` returns the first element matching a CSS selector.

Example:

    const title = document.querySelector("#title");

Class selector:

    const card = document.querySelector(".card");

Element selector:

    const heading = document.querySelector("h1");

---

# 10. querySelectorAll()

`querySelectorAll()` returns all elements matching a CSS selector.

Example:

    const paragraphs = document.querySelectorAll("p");

It returns a NodeList.

---

# 11. getElementById vs querySelector

Example:

    document.getElementById("title");

Equivalent CSS selector:

    document.querySelector("#title");

`getElementById()` is specifically designed for IDs.

`querySelector()` can use any valid CSS selector.

---

# 12. Reading textContent

`textContent` gets or sets the text content of an element.

Example:

    const title = document.querySelector("#title");

    console.log(title.textContent);

---

# 13. Changing textContent

Example:

    const title = document.querySelector("#title");

    title.textContent = "Welcome to MAD 1";

The visible text of the element changes.

---

# 14. innerHTML

`innerHTML` gets or sets the HTML markup inside an element.

Example:

    const box = document.querySelector("#box");

    box.innerHTML = "<strong>Hello</strong>";

The `<strong>` element becomes part of the DOM.

---

# 15. textContent vs innerHTML

`textContent` treats assigned content as text.

Example:

    element.textContent = "<strong>Hello</strong>";

The tags are displayed as text.

`innerHTML` interprets the string as HTML.

Example:

    element.innerHTML = "<strong>Hello</strong>";

The word becomes bold.

Use `textContent` when you only need text, especially for untrusted user input.

Be careful with `innerHTML` because inserting untrusted HTML can create security problems such as cross-site scripting (XSS).

---

# 16. Changing Styles

JavaScript can modify inline styles through the `style` property.

Example:

    const title = document.querySelector("#title");

    title.style.color = "blue";

    title.style.fontSize = "30px";

---

# 17. Multiple Style Changes

Example:

    const box = document.querySelector("#box");

    box.style.backgroundColor = "lightblue";
    box.style.padding = "20px";
    box.style.borderRadius = "10px";

JavaScript changes the element's inline styles.

---

# 18. classList

`classList` provides methods for working with CSS classes.

Common methods:

- `add()`
- `remove()`
- `toggle()`
- `contains()`

Example:

    const box = document.querySelector("#box");

    box.classList.add("active");

---

# 19. classList.remove()

Example:

    box.classList.remove("active");

This removes the class if it exists.

---

# 20. classList.toggle()

Example:

    box.classList.toggle("active");

If the class exists, it is removed.

If it does not exist, it is added.

---

# 21. classList.contains()

Example:

    const active = box.classList.contains("active");

This returns:

    true

or:

    false

---

# 22. Reading Attributes

`getAttribute()` reads an HTML attribute.

Example:

    const image = document.querySelector("img");

    const source = image.getAttribute("src");

---

# 23. Changing Attributes

`setAttribute()` creates or changes an attribute.

Example:

    image.setAttribute("alt", "Student profile image");

Another example:

    link.setAttribute("href", "https://example.com");

---

# 24. Removing Attributes

`removeAttribute()` removes an attribute.

Example:

    element.removeAttribute("disabled");

---

# 25. Creating Elements

JavaScript can create new DOM elements.

Example:

    const paragraph = document.createElement("p");

    paragraph.textContent = "New paragraph";

At this point, the element exists in memory but has not yet been added to the document.

---

# 26. Adding Elements

Use methods such as `append()` to add a new element.

Example:

    const paragraph = document.createElement("p");

    paragraph.textContent = "New paragraph";

    document.body.append(paragraph);

The paragraph is now part of the webpage.

---

# 27. Removing Elements

An element can remove itself from the DOM.

Example:

    const element = document.querySelector("#box");

    element.remove();

---

# 28. DOM Manipulation

DOM manipulation means changing the document using JavaScript.

Common operations include:

    Select
      ↓
    Read
      ↓
    Modify
      ↓
    Create
      ↓
    Insert
      ↓
    Remove

---

# 29. Selecting Multiple Elements

Example:

    const cards = document.querySelectorAll(".card");

You can process the returned NodeList.

Example:

    cards.forEach(card => {
        console.log(card.textContent);
    });

---

# 30. DOM and CSS Selectors

Many CSS selectors can also be used with `querySelector()`.

Examples:

    document.querySelector("#title");

    document.querySelector(".card");

    document.querySelector("p");

    document.querySelector("section p");

    document.querySelector("input[type='email']");

This makes DOM selection familiar if you already understand CSS selectors.

---

# 31. DOM Properties vs Methods

A property stores or provides information.

Examples:

    element.textContent
    element.innerHTML
    element.id

A method performs an operation.

Examples:

    element.remove()
    element.setAttribute()
    element.classList.add()

---

# 32. DOM Selection When Script Loads

If JavaScript tries to select an element before that element has been parsed, the result may be `null`.

Example:

    const title = document.getElementById("title");

If the `<h1 id="title">` has not been parsed yet, the element may not be available.

One solution is placing the script near the end of the body.

Another common solution is using `defer` for an external script.

Example:

    <script src="script.js" defer></script>

---

# 33. null from a Selector

If no matching element is found:

    const element = document.querySelector("#doesNotExist");

The result is:

    null

Trying to access properties on `null` can produce a `TypeError`.

Example:

    element.textContent = "Hello";

This would fail if `element` is `null`.

---

# 34. Checking for an Element

Example:

    const element = document.querySelector("#title");

    if (element) {
        element.textContent = "Hello";
    }

This prevents attempting to manipulate a missing element.

---

# 35. DOM vs HTML

HTML is the markup source.

DOM is the browser's object representation of the document.

JavaScript interacts with the DOM rather than directly editing the original HTML source file.

---

# 36. DOM vs CSSOM

The browser also creates a CSS Object Model (CSSOM) for CSS.

A simplified browser model is:

    HTML
      ↓
    DOM

    CSS
      ↓
    CSSOM

The browser combines information from both to render the webpage.

---

# 37. Browser Developer Tools

The browser Developer Tools are useful for learning and debugging the DOM.

Useful areas include:

- Elements panel
- Console
- Sources
- Network

The Elements panel allows you to inspect the current DOM.

The Console allows you to execute JavaScript.

---

# 38. DOM Example

HTML:

    <h1 id="title">Old Title</h1>

JavaScript:

    const title = document.getElementById("title");

    title.textContent = "New Title";

The browser updates the displayed heading.

---

# 39. Practical DOM Flow

A common DOM workflow is:

    1. Select element
    2. Read information
    3. Change content or attributes
    4. Change classes/styles
    5. Create or remove elements
    6. Update the webpage

---

# 40. Best Practices

- Prefer `textContent` when inserting plain text.
- Be careful when using `innerHTML`.
- Use meaningful IDs and classes.
- Check whether an element exists before manipulating it when necessary.
- Prefer CSS classes for reusable styling rather than excessive inline styles.
- Keep DOM manipulation organized.
- Use `defer` for external scripts when appropriate.
- Use Developer Tools to inspect and debug the DOM.
- Avoid unnecessary DOM operations.

---

# 🧠 Key Takeaways

    DOM
    ↓
    Document Object Model

    document
    ↓
    Represents the current HTML document

    getElementById()
    ↓
    Select by ID

    querySelector()
    ↓
    Select first CSS-selector match

    querySelectorAll()
    ↓
    Select all CSS-selector matches

    textContent
    ↓
    Read/write text

    innerHTML
    ↓
    Read/write HTML markup

    classList
    ↓
    Manage CSS classes

    createElement()
    ↓
    Create an element

    append()
    ↓
    Add content/elements

    remove()
    ↓
    Remove an element