# 🧪 Day 054 — DOM Introduction — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 054  
**Topic:** DOM Introduction

---

# 🎯 Practice Objectives

Practice:

- DOM basics
- DOM tree
- Element selection
- `getElementById()`
- `querySelector()`
- `querySelectorAll()`
- `textContent`
- `innerHTML`
- `style`
- `classList`
- Attributes
- Creating elements
- Removing elements

---

# 🟢 Level 1 — Basics

## Q1

What does DOM stand for?

---

## Q2

What is the purpose of the DOM?

---

## Q3

What does the `document` object represent?

---

## Q4

What is a DOM tree?

---

## Q5

Name four common types of DOM nodes.

---

# 🟡 Level 2 — Selection

## Q6

Select the following element by ID:

    <h1 id="title">MAD 1</h1>

---

## Q7

Use `querySelector()` to select the first element with class `card`.

---

## Q8

Use `querySelectorAll()` to select all paragraphs.

---

## Q9

What is the difference between `querySelector()` and `querySelectorAll()`?

---

## Q10

What does a selector return when no matching element is found?

---

# 🟠 Level 3 — Manipulation

## Q11

Change the text of this element:

    <p id="message">Old Message</p>

Use JavaScript.

---

## Q12

Change the color of an `<h1>` using JavaScript.

---

## Q13

Add the class `active` to an element.

---

## Q14

Remove the class `active`.

---

## Q15

Toggle the class `active`.

---

## Q16

Read the `href` attribute of a link.

---

## Q17

Change the `src` attribute of an image.

---

# 🟠 Level 4 — Predict the Result

## Q18

What will happen?

    const title = document.querySelector("#title");

    title.textContent = "Hello";

---

## Q19

What is the difference between these two statements?

    element.textContent = "<strong>Hello</strong>";

    element.innerHTML = "<strong>Hello</strong>";

---

## Q20

What happens if this selector finds no element?

    const box = document.querySelector("#missing");

    console.log(box);

---

## Q21

Why can this cause an error?

    const box = document.querySelector("#missing");

    box.textContent = "Hello";

---

# 🔴 Level 5 — Coding Practice

## Task 1 — Change Heading

Create:

    <h1 id="title">Welcome</h1>

Use JavaScript to change it to:

    Welcome to MAD 1

---

## Task 2 — Dynamic Style

Create a paragraph and use JavaScript to change:

- Color
- Font size
- Background color

---

## Task 3 — Class Toggle

Create a box with a CSS class.

Add a button that toggles another class using:

    classList.toggle()

---

## Task 4 — Attribute Manipulation

Create an image and use JavaScript to:

- Read its `src`
- Change its `alt`
- Change its `src`

---

## Task 5 — Create an Element

Use:

    document.createElement()

to create a new paragraph.

Set its text and append it to the page.

---

## Task 6 — Remove an Element

Create a button that removes a paragraph from the webpage.

---

# 🧠 Conceptual Questions

## Q22

What is the difference between HTML and DOM?

---

## Q23

What is the difference between a DOM node and a DOM element?

---

## Q24

Why is `textContent` generally preferred for plain text?

---

## Q25

Why should `innerHTML` be used carefully with untrusted input?

---

## Q26

Why is `classList` useful?

---

## Q27

Why should you check for `null` before manipulating an element?

---

# ⭐ Final Challenge

Create a small interactive Student Profile.

The page should contain:

- Student name
- Course
- Score
- Skills
- A profile image
- A button to change the name
- A button to change the score
- A button to toggle a CSS class
- A button to add a new skill
- A button to remove an element

Use at least:

- `getElementById()`
- `querySelector()`
- `textContent`
- `classList`
- `setAttribute()`
- `createElement()`
- `append()`
- `remove()`

---

# ✅ Self-Check

Before moving to Day 055, make sure you can explain:

- [ ] DOM
- [ ] DOM tree
- [ ] Nodes
- [ ] Elements
- [ ] `document`
- [ ] `getElementById()`
- [ ] `querySelector()`
- [ ] `querySelectorAll()`
- [ ] `textContent`
- [ ] `innerHTML`
- [ ] `style`
- [ ] `classList`
- [ ] `getAttribute()`
- [ ] `setAttribute()`
- [ ] `createElement()`
- [ ] `append()`
- [ ] `remove()`
- [ ] DOM debugging

---

## 📌 Goal

Learn how JavaScript selects and manipulates HTML elements through the DOM.