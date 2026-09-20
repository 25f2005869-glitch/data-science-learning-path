# ⚡ Day 054 — DOM Introduction — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 054  
**Topic:** DOM Introduction

---

# 🔹 DOM

DOM = Document Object Model.

It represents an HTML document as objects in a tree structure.

    HTML
      ↓
    DOM
      ↓
    JavaScript
      ↓
    Dynamic Webpage

---

# 🔹 document

The `document` object represents the current HTML document.

    console.log(document);

---

# 🔹 Select by ID

    const title = document.getElementById("title");

Returns the element with the specified ID.

---

# 🔹 querySelector()

Returns the first matching element.

    document.querySelector("#title");

    document.querySelector(".card");

    document.querySelector("p");

---

# 🔹 querySelectorAll()

Returns all matching elements.

    document.querySelectorAll(".card");

Usually returns a NodeList.

---

# 🔹 textContent

Read:

    element.textContent;

Write:

    element.textContent = "Hello";

Use it for plain text.

---

# 🔹 innerHTML

Read:

    element.innerHTML;

Write:

    element.innerHTML = "<strong>Hello</strong>";

It interprets the string as HTML.

Be careful with untrusted input.

---

# 🔹 style

Change inline style:

    element.style.color = "blue";

    element.style.fontSize = "25px";

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

# 🔹 Create Element

    const p = document.createElement("p");

---

# 🔹 Add Element

    document.body.append(p);

---

# 🔹 Remove Element

    element.remove();

---

# 🔹 Check for null

    const element = document.querySelector("#title");

    if (element) {
        element.textContent = "Hello";
    }

---

# 🔹 DOM Selection Summary

| Method | Purpose |
|---|---|
| `getElementById()` | Select by ID |
| `querySelector()` | First CSS-selector match |
| `querySelectorAll()` | All CSS-selector matches |
| `createElement()` | Create element |

---

# 🔹 DOM Manipulation Summary

| Property / Method | Purpose |
|---|---|
| `textContent` | Text |
| `innerHTML` | HTML markup |
| `style` | Inline styles |
| `classList` | CSS classes |
| `getAttribute()` | Read attribute |
| `setAttribute()` | Set attribute |
| `removeAttribute()` | Remove attribute |
| `append()` | Add content |
| `remove()` | Remove element |

---

# 🧠 Remember

    Select → Read → Modify → Create → Add → Remove

---

# ⭐ Important

`textContent` is generally safer for inserting plain text.

`innerHTML` should be used carefully with untrusted data because unsafe HTML insertion can lead to XSS vulnerabilities.

Use CSS classes for reusable styling instead of excessive inline styles.