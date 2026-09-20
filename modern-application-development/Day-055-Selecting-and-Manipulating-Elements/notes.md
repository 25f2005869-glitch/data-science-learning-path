# 📝 Day 055 — Selecting and Manipulating Elements — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 055  
**Topic:** Selecting and Manipulating Elements

---

# 1. What is DOM Manipulation?

DOM manipulation means using JavaScript to access and modify elements in an HTML document.

A common workflow is:

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

# 2. Selecting Elements

Before manipulating an element, JavaScript usually needs to select it.

Common selection methods include:

- `getElementById()`
- `getElementsByClassName()`
- `getElementsByTagName()`
- `querySelector()`
- `querySelectorAll()`

---

# 3. getElementById()

Selects one element using its ID.

Example:

    const title = document.getElementById("title");

HTML:

    <h1 id="title">Hello</h1>

If no element has that ID, the result is `null`.

---

# 4. getElementsByClassName()

Selects elements using a class name.

Example:

    const cards = document.getElementsByClassName("card");

It returns an `HTMLCollection`.

Unlike `querySelectorAll()`, the returned collection is live.

---

# 5. getElementsByTagName()

Selects elements by their tag name.

Example:

    const paragraphs = document.getElementsByTagName("p");

This returns an `HTMLCollection`.

---

# 6. querySelector()

Returns the first element matching a CSS selector.

Example:

    const title = document.querySelector("#title");

Class:

    const card = document.querySelector(".card");

Tag:

    const paragraph = document.querySelector("p");

Attribute:

    const input = document.querySelector("input[type='email']");

---

# 7. querySelectorAll()

Returns all elements matching a CSS selector.

Example:

    const cards = document.querySelectorAll(".card");

It returns a `NodeList`.

You can commonly use `forEach()` with the returned NodeList.

Example:

    cards.forEach(card => {
        console.log(card.textContent);
    });

---

# 8. Selection Method Comparison

| Method | Selector Type | Result |
|---|---|---|
| `getElementById()` | ID | Element or `null` |
| `getElementsByClassName()` | Class | HTMLCollection |
| `getElementsByTagName()` | Tag | HTMLCollection |
| `querySelector()` | CSS selector | First matching element |
| `querySelectorAll()` | CSS selector | NodeList |

---

# 9. Reading Text

Use `textContent` to read the text of an element.

Example:

    const title = document.querySelector("h1");

    console.log(title.textContent);

---

# 10. Changing Text

`textContent` can also change text.

Example:

    title.textContent = "New Heading";

The visible text is updated.

---

# 11. innerHTML

`innerHTML` reads or writes HTML markup inside an element.

Example:

    const box = document.querySelector("#box");

    box.innerHTML = "<strong>Hello</strong>";

The `<strong>` element is interpreted as HTML.

---

# 12. textContent vs innerHTML

`textContent`:

    element.textContent = "<strong>Hello</strong>";

Displays the tags as text.

`innerHTML`:

    element.innerHTML = "<strong>Hello</strong>";

Interprets the tags as HTML.

Use `textContent` for plain text whenever possible.

Be careful with `innerHTML` and untrusted data because unsafe HTML insertion can cause XSS vulnerabilities.

---

# 13. Changing Inline Styles

The `style` property can change inline CSS.

Example:

    const box = document.querySelector("#box");

    box.style.color = "blue";
    box.style.backgroundColor = "lightgray";
    box.style.padding = "20px";

CSS property names that contain hyphens are written in camelCase.

Example:

    background-color

becomes:

    backgroundColor

---

# 14. classList

`classList` provides methods for managing CSS classes.

Common methods:

- `add()`
- `remove()`
- `toggle()`
- `contains()`

Example:

    box.classList.add("active");

---

# 15. classList.add()

Adds a class.

    element.classList.add("active");

Multiple classes can be added:

    element.classList.add("active", "highlight");

---

# 16. classList.remove()

Removes a class.

    element.classList.remove("active");

---

# 17. classList.toggle()

Adds the class if it does not exist.

Removes it if it already exists.

Example:

    element.classList.toggle("active");

---

# 18. classList.contains()

Checks whether a class exists.

Example:

    const isActive = element.classList.contains("active");

Result:

    true

or:

    false

---

# 19. Reading Attributes

Use `getAttribute()`.

Example:

    const link = document.querySelector("a");

    const url = link.getAttribute("href");

---

# 20. Setting Attributes

Use `setAttribute()`.

Example:

    link.setAttribute("href", "https://example.com");

This creates the attribute if it does not exist or changes it if it already exists.

---

# 21. Removing Attributes

Use `removeAttribute()`.

Example:

    input.removeAttribute("disabled");

---

# 22. Direct Attribute Properties

Many common attributes can also be accessed as properties.

Example:

    const image = document.querySelector("img");

    console.log(image.src);
    console.log(image.alt);

For common DOM properties, direct property access is often convenient.

---

# 23. Creating Elements

Use `document.createElement()`.

Example:

    const paragraph = document.createElement("p");

The new element exists in memory but is not yet visible on the page.

---

# 24. Setting Content of a New Element

Example:

    const paragraph = document.createElement("p");

    paragraph.textContent = "New paragraph";

---

# 25. append()

`append()` adds content at the end of an element.

Example:

    const list = document.querySelector("ul");

    const item = document.createElement("li");

    item.textContent = "DOM";

    list.append(item);

---

# 26. prepend()

`prepend()` adds content at the beginning.

Example:

    list.prepend(item);

---

# 27. before()

`before()` inserts content immediately before an element.

Example:

    heading.before(paragraph);

---

# 28. after()

`after()` inserts content immediately after an element.

Example:

    heading.after(paragraph);

---

# 29. append vs prepend

    append()
        ↓
    Adds at the end

    prepend()
        ↓
    Adds at the beginning

---

# 30. Removing Elements

Use `remove()`.

Example:

    const message = document.querySelector("#message");

    message.remove();

The selected element is removed from the DOM.

---

# 31. replaceWith()

An element can be replaced with another element.

Example:

    const oldElement = document.querySelector("#old");

    const newElement = document.createElement("p");

    newElement.textContent = "New content";

    oldElement.replaceWith(newElement);

---

# 32. Parent Element

`parentElement` gives the parent element.

Example:

    const item = document.querySelector("li");

    console.log(item.parentElement);

---

# 33. children

`children` returns the child elements of an element.

Example:

    const list = document.querySelector("ul");

    console.log(list.children);

It contains element children rather than text nodes.

---

# 34. firstElementChild

Returns the first child element.

Example:

    const first = list.firstElementChild;

---

# 35. lastElementChild

Returns the last child element.

Example:

    const last = list.lastElementChild;

---

# 36. Basic DOM Traversal

DOM traversal means moving between related elements.

Common properties:

    parentElement
    children
    firstElementChild
    lastElementChild
    nextElementSibling
    previousElementSibling

---

# 37. nextElementSibling

Returns the next sibling element.

Example:

    const first = document.querySelector("li");

    console.log(first.nextElementSibling);

---

# 38. previousElementSibling

Returns the previous sibling element.

Example:

    const second = document.querySelectorAll("li")[1];

    console.log(second.previousElementSibling);

---

# 39. Working with Multiple Elements

Example:

    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        card.classList.add("visible");
    });

This applies the same operation to every selected element.

---

# 40. Creating a List Dynamically

Example:

    const list = document.querySelector("#skills");

    const skill = document.createElement("li");

    skill.textContent = "DOM";

    list.append(skill);

The new skill becomes part of the document.

---

# 41. Creating Elements with Classes

Example:

    const card = document.createElement("div");

    card.classList.add("card");

    card.textContent = "New Card";

    document.body.append(card);

---

# 42. Creating Nested Elements

Example:

    const article = document.createElement("article");

    const heading = document.createElement("h2");

    heading.textContent = "DOM";

    article.append(heading);

    document.body.append(article);

---

# 43. Avoiding null Errors

A selector may return `null`.

Example:

    const title = document.querySelector("#missing");

Before manipulating it:

    if (title) {
        title.textContent = "Hello";
    }

This prevents errors caused by manipulating a missing element.

---

# 44. DOM Manipulation and CSS

A better approach for reusable styling is usually to define styles in CSS and use JavaScript to add or remove classes.

Example:

    element.classList.toggle("active");

Instead of repeatedly changing many inline styles.

---

# 45. DOM Performance

Repeated DOM operations can be expensive in large applications.

Prefer:

- Selecting elements once when appropriate
- Reusing references
- Updating only what is necessary
- Avoiding unnecessary repeated queries
- Using efficient DOM operations

---

# 46. textContent Security

For plain user-provided text, prefer:

    element.textContent = userInput;

Be careful with:

    element.innerHTML = userInput;

Untrusted HTML can introduce security vulnerabilities such as XSS.

---

# 47. Practical DOM Workflow

A typical operation looks like:

    1. Select element
    2. Check that it exists
    3. Read current state
    4. Modify content/classes/attributes
    5. Create or remove elements if required
    6. Verify the result

---

# 48. Example — Student Card

Example:

    const card = document.createElement("article");

    card.classList.add("student-card");

    const name = document.createElement("h2");

    name.textContent = "Saloni Tiwari";

    card.append(name);

    document.body.append(card);

---

# 49. Best Practices

- Use meaningful IDs and classes.
- Prefer `querySelector()` and `querySelectorAll()` for flexible CSS selection.
- Use `textContent` for plain text.
- Use `innerHTML` carefully.
- Prefer CSS classes for reusable styles.
- Check for `null` when a selector may fail.
- Reuse DOM references when appropriate.
- Keep DOM manipulation organized.
- Avoid unnecessary DOM operations.

---

# 🧠 Key Takeaways

    getElementById()
        ↓
    Select by ID

    querySelector()
        ↓
    Select first CSS match

    querySelectorAll()
        ↓
    Select all CSS matches

    textContent
        ↓
    Read/write text

    innerHTML
        ↓
    Read/write HTML

    classList
        ↓
    Manage classes

    createElement()
        ↓
    Create element

    append() / prepend()
        ↓
    Insert content

    remove()
        ↓
    Remove element

    parentElement / children
        ↓
    Traverse DOM