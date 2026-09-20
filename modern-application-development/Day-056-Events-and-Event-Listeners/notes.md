# 📚 Day 056 — Events and Event Listeners

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 056  
**Topic:** Events and Event Listeners

---

## 1. What Is an Event?

An event is an action or occurrence detected by the browser.

Examples:

- User clicks a button
- User types in an input
- User submits a form
- Mouse moves over an element
- Keyboard key is pressed
- Page finishes loading

JavaScript can listen for these events and execute code when they occur.

---

## 2. Event Handler

An event handler is JavaScript code that runs when a specific event occurs.

Example:

    button.onclick = function () {
        console.log("Button clicked");
    };

Although event handler properties work, `addEventListener()` is generally preferred for modern applications.

---

## 3. addEventListener()

`addEventListener()` attaches an event listener to an element.

Syntax:

    element.addEventListener("event", function);

Example:

    const button = document.querySelector("#myButton");

    button.addEventListener("click", function () {
        console.log("Button clicked");
    });

The first argument is the event type.

The second argument is the function that should execute.

---

## 4. Common Events

| Event | Meaning |
|---|---|
| `click` | Element is clicked |
| `dblclick` | Element is double-clicked |
| `mouseover` | Pointer moves over an element |
| `mouseout` | Pointer leaves an element |
| `mouseenter` | Pointer enters an element |
| `mouseleave` | Pointer leaves an element |
| `mousedown` | Mouse button is pressed |
| `mouseup` | Mouse button is released |
| `keydown` | Keyboard key is pressed |
| `keyup` | Keyboard key is released |
| `input` | Input value changes while typing |
| `change` | Input value is committed/changed |
| `focus` | Element receives focus |
| `blur` | Element loses focus |
| `submit` | Form is submitted |
| `load` | Resource/page finishes loading |

---

## 5. Event Object

When an event occurs, the browser provides an event object containing information about that event.

Example:

    button.addEventListener("click", function (event) {
        console.log(event);
    });

The event object can provide information such as:

- Event type
- Target element
- Mouse position
- Keyboard key
- Modifier keys

---

## 6. event.target

`event.target` refers to the element where the event originated.

Example:

    button.addEventListener("click", function (event) {
        console.log(event.target);
    });

It is useful when handling events dynamically.

---

## 7. Mouse Events

Common mouse events include:

- `click`
- `dblclick`
- `mousedown`
- `mouseup`
- `mouseenter`
- `mouseleave`
- `mousemove`

Example:

    const box = document.querySelector("#box");

    box.addEventListener("mouseenter", function () {
        box.textContent = "Mouse entered!";
    });

---

## 8. Keyboard Events

Keyboard events include:

- `keydown`
- `keyup`

Example:

    document.addEventListener("keydown", function (event) {
        console.log(event.key);
    });

If the user presses the `Enter` key:

    event.key

can contain:

    Enter

---

## 9. Input Event

The `input` event fires whenever the value of an input changes while the user is interacting with it.

Example:

    const nameInput = document.querySelector("#name");

    nameInput.addEventListener("input", function (event) {
        console.log(event.target.value);
    });

This is useful for:

- Live search
- Character counters
- Live validation
- Previewing user input

---

## 10. Change Event

The `change` event is commonly used with inputs, checkboxes, radio buttons, and select elements.

Example:

    const course = document.querySelector("#course");

    course.addEventListener("change", function () {
        console.log(course.value);
    });

---

## 11. Focus and Blur

`focus` occurs when an element receives focus.

`blur` occurs when an element loses focus.

Example:

    input.addEventListener("focus", function () {
        console.log("Input focused");
    });

    input.addEventListener("blur", function () {
        console.log("Input lost focus");
    });

---

## 12. Form Submit Event

Forms can be handled using the `submit` event.

Example:

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        console.log("Form handled by JavaScript");
    });

---

## 13. preventDefault()

`preventDefault()` prevents the browser's default action for an event.

For example, a form normally submits and may reload/navigate the page.

Example:

    form.addEventListener("submit", function (event) {
        event.preventDefault();
    });

It is commonly used when JavaScript needs to process a form before sending data.

---

## 14. Event Bubbling

Events normally propagate from the target element upward through its ancestors.

Example:

    child → parent → body → document

This behavior is called event bubbling.

Example:

    parent.addEventListener("click", function () {
        console.log("Parent clicked");
    });

    child.addEventListener("click", function () {
        console.log("Child clicked");
    });

Clicking the child can trigger both listeners.

---

## 15. stopPropagation()

`stopPropagation()` stops an event from continuing through the propagation path.

Example:

    child.addEventListener("click", function (event) {
        event.stopPropagation();
    });

Use it only when necessary because unnecessary propagation control can make event behavior harder to understand.

---

## 16. Event Delegation

Event delegation means placing one event listener on a parent element to handle events from its children.

Example:

    list.addEventListener("click", function (event) {
        if (event.target.matches("li")) {
            console.log(event.target.textContent);
        }
    });

Advantages:

- Fewer event listeners
- Works well with dynamically created elements
- Better for large lists

---

## 17. Removing an Event Listener

To remove a listener, the same function reference must be provided.

Example:

    function handleClick() {
        console.log("Clicked");
    }

    button.addEventListener("click", handleClick);

    button.removeEventListener("click", handleClick);

An anonymous function cannot normally be removed by creating another identical anonymous function.

---

## 18. Multiple Event Listeners

An element can have multiple listeners for different events.

Example:

    button.addEventListener("click", handleClick);
    button.addEventListener("mouseenter", handleMouseEnter);

Multiple listeners can also be attached to the same event.

---

## 19. Event Listener Options

`addEventListener()` can accept an options object.

Example:

    button.addEventListener("click", handleClick, {
        once: true
    });

Useful options include:

- `once`
- `capture`
- `passive`

`once: true` causes the listener to run only once.

---

## 20. Inline Event Handlers

HTML can contain inline event handlers.

Example:

    <button onclick="handleClick()">Click</button>

This works, but separating HTML and JavaScript is generally cleaner.

Prefer:

    button.addEventListener("click", handleClick);

---

## 21. Event Listener vs Event Handler Property

Event handler property:

    button.onclick = handleClick;

Event listener:

    button.addEventListener("click", handleClick);

`addEventListener()` is generally preferred because multiple listeners can be attached without overwriting previous listeners.

---

## 22. Common Mistakes

### Mistake 1: Selecting a missing element

    const button = document.querySelector("#missing");

    button.addEventListener("click", handleClick);

If the element does not exist, this can cause an error.

### Mistake 2: Calling the function immediately

Incorrect:

    button.addEventListener("click", handleClick());

Correct:

    button.addEventListener("click", handleClick);

### Mistake 3: Forgetting preventDefault()

When custom form processing is required, forgetting `preventDefault()` may cause an unwanted page navigation or reload.

### Mistake 4: Using too many listeners

Large numbers of unnecessary listeners can make code harder to maintain.

Event delegation can help with repeated elements.

---

## 23. Best Practices

- Prefer `addEventListener()`
- Use meaningful function names
- Keep event handlers small
- Validate user input
- Use `preventDefault()` only when required
- Use event delegation for suitable dynamic lists
- Avoid unnecessary `stopPropagation()`
- Separate HTML, CSS, and JavaScript
- Check that DOM elements exist
- Use accessible interactive elements such as buttons for button actions

---

## 24. Key Takeaway

Events connect user actions with JavaScript behavior.

The basic pattern is:

    select element
    ↓
    add event listener
    ↓
    wait for event
    ↓
    execute callback
    ↓
    update the DOM

The most important method for this topic is:

    element.addEventListener("event", callback);