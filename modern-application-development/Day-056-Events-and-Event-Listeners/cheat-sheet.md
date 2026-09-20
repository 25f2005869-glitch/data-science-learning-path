# ⚡ Day 056 — Events and Event Listeners Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 056  
**Topic:** Events and Event Listeners

---

## 🔹 Basic Syntax

    element.addEventListener("event", callback);

Example:

    button.addEventListener("click", handleClick);

---

## 🔹 Common Events

| Event | Use |
|---|---|
| `click` | Mouse click |
| `dblclick` | Double click |
| `mouseenter` | Mouse enters |
| `mouseleave` | Mouse leaves |
| `mousemove` | Mouse moves |
| `keydown` | Key pressed |
| `keyup` | Key released |
| `input` | Value changes while typing |
| `change` | Value is changed/committed |
| `focus` | Element receives focus |
| `blur` | Element loses focus |
| `submit` | Form submission |
| `load` | Resource/page loaded |

---

## 🔹 Event Object

    element.addEventListener("click", function (event) {
        console.log(event);
    });

Useful properties:

    event.type
    event.target
    event.key
    event.clientX
    event.clientY

---

## 🔹 Input Value

    input.addEventListener("input", function (event) {
        console.log(event.target.value);
    });

---

## 🔹 Form Submission

    form.addEventListener("submit", function (event) {
        event.preventDefault();
    });

---

## 🔹 preventDefault()

Stops the browser's default action.

    event.preventDefault();

---

## 🔹 Event Bubbling

Event flow can move upward:

    child
      ↓
    parent
      ↓
    body
      ↓
    document

---

## 🔹 stopPropagation()

    event.stopPropagation();

Stops further propagation of the event.

---

## 🔹 Event Delegation

Use one listener on a parent:

    list.addEventListener("click", function (event) {
        if (event.target.matches("li")) {
            console.log(event.target.textContent);
        }
    });

---

## 🔹 Remove Listener

    function handleClick() {
        console.log("Clicked");
    }

    button.addEventListener("click", handleClick);

    button.removeEventListener("click", handleClick);

The same function reference is required.

---

## 🔹 One-Time Listener

    button.addEventListener("click", handleClick, {
        once: true
    });

---

## 🔹 Event Handler Property

    button.onclick = handleClick;

Preferred modern approach:

    button.addEventListener("click", handleClick);

---

## 🔹 Important Difference

`onclick`:

- Event handler property
- Can be overwritten

`addEventListener()`:

- Supports multiple listeners
- More flexible
- Preferred for modern JavaScript

---

## 🔹 Common Mistake

Incorrect:

    button.addEventListener("click", handleClick());

Correct:

    button.addEventListener("click", handleClick);

---

## 🧠 Remember

    Event
    ↓
    Listener
    ↓
    Callback
    ↓
    Action

Most important method:

    addEventListener()