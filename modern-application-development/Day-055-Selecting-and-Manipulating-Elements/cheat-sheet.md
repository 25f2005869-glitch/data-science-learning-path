# ⚡ Day 055 — Selecting and Manipulating Elements — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 055  
**Topic:** Selecting and Manipulating Elements

---

# 🔹 Selecting Elements

## By ID

    document.getElementById("title");

## By Class

    document.getElementsByClassName("card");

## By Tag

    document.getElementsByTagName("p");

## First CSS Match

    document.querySelector(".card");

## All CSS Matches

    document.querySelectorAll(".card");

---

# 🔹 Selection Results

| Method | Result |
|---|---|
| `getElementById()` | Element / `null` |
| `getElementsByClassName()` | HTMLCollection |
| `getElementsByTagName()` | HTMLCollection |
| `querySelector()` | First matching element |
| `querySelectorAll()` | NodeList |

---

# 🔹 Text

Read:

    element.textContent;

Write:

    element.textContent = "Hello";

---

# 🔹 HTML

Read:

    element.innerHTML;

Write:

    element.innerHTML = "<strong>Hello</strong>";

Use carefully with untrusted data.

---

# 🔹 Style

    element.style.color = "blue";

    element.style.backgroundColor = "yellow";

---

# 🔹 classList

Add:

    element.classList.add("active");

Remove:

    element.classList.remove("active");

Toggle:

    element.classList.toggle("active");

Check:

    element.classList.contains("active");

---

# 🔹 Attributes

Read:

    element.getAttribute("href");

Set:

    element.setAttribute("href", "https://example.com");

Remove:

    element.removeAttribute("disabled");

---

# 🔹 Create

    const item = document.createElement("li");

---

# 🔹 Insert

End:

    parent.append(item);

Beginning:

    parent.prepend(item);

Before:

    element.before(item);

After:

    element.after(item);

---

# 🔹 Remove

    element.remove();

---

# 🔹 Replace

    oldElement.replaceWith(newElement);

---

# 🔹 Traversal

Parent:

    element.parentElement;

Children:

    element.children;

First child:

    element.firstElementChild;

Last child:

    element.lastElementChild;

Next:

    element.nextElementSibling;

Previous:

    element.previousElementSibling;

---

# 🔹 DOM Workflow

    Select
      ↓
    Check
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

# 🧠 Important Differences

### querySelector()

Returns the first matching element.

### querySelectorAll()

Returns all matching elements as a NodeList.

### textContent

Works with plain text.

### innerHTML

Works with HTML markup.

### append()

Adds at the end.

### prepend()

Adds at the beginning.

---

# ⭐ Golden Rules

1. Select the correct element.
2. Check for `null` when necessary.
3. Prefer `textContent` for plain text.
4. Use `innerHTML` carefully.
5. Prefer CSS classes for reusable styling.
6. Use `classList` for class manipulation.
7. Use `createElement()` for dynamic elements.
8. Use `append()` and `prepend()` for insertion.
9. Use `remove()` to delete elements.
10. Keep DOM operations simple and organized.