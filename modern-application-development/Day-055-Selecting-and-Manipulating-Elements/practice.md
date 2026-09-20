# 🧪 Day 055 — Selecting and Manipulating Elements — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 055  
**Topic:** Selecting and Manipulating Elements

---

# 🎯 Practice Objectives

Practice:

- Selecting elements
- Reading content
- Changing content
- Modifying styles
- Managing classes
- Managing attributes
- Creating elements
- Inserting elements
- Removing elements
- Replacing elements
- Basic DOM traversal

---

# 🟢 Level 1 — Selection

## Q1

Select this element using `getElementById()`:

    <h1 id="title">MAD 1</h1>

---

## Q2

Select the first element with class `card`.

Use `querySelector()`.

---

## Q3

Select all paragraphs using `querySelectorAll()`.

---

## Q4

What does `getElementsByClassName()` return?

---

## Q5

What is the difference between `querySelector()` and `querySelectorAll()`?

---

# 🟡 Level 2 — Content

## Q6

Change this text using `textContent`:

    <p id="message">Old Message</p>

---

## Q7

Use `innerHTML` to insert a bold heading inside an element.

---

## Q8

Explain the difference between `textContent` and `innerHTML`.

---

## Q9

Why should `innerHTML` be used carefully with untrusted input?

---

# 🟠 Level 3 — Classes and Styles

## Q10

Add the class `active` to an element.

---

## Q11

Remove the class `active`.

---

## Q12

Toggle the class `active`.

---

## Q13

Check whether an element contains the class `active`.

---

## Q14

Change an element's background color using JavaScript.

---

## Q15

Change an element's font size using JavaScript.

---

# 🟠 Level 4 — Attributes

## Q16

Read the `href` of a link.

---

## Q17

Change an image's `src` attribute.

---

## Q18

Change an input's `placeholder` using `setAttribute()`.

---

## Q19

Remove the `disabled` attribute from a button.

---

# 🔴 Level 5 — Creating Elements

## Q20

Create a new paragraph using:

    document.createElement()

Set its text and append it to the page.

---

## Q21

Create a new `<li>` element and add it to an existing list.

---

## Q22

Create a new `<article>` containing an `<h2>` heading.

---

## Q23

Add a CSS class to a dynamically created element.

---

# 🧠 DOM Traversal

## Q24

How do you access the parent element?

---

## Q25

How do you access all child elements?

---

## Q26

How do you access the first child element?

---

## Q27

How do you access the last child element?

---

## Q28

How do you access the next sibling element?

---

# 💻 Coding Practice

## Task 1 — Student Name

Create a student heading.

Add a button that changes the student's name using `textContent`.

---

## Task 2 — Course Card

Create a course card dynamically using JavaScript.

It should contain:

- Course name
- Course description
- Course status

Use `createElement()` and `append()`.

---

## Task 3 — Skill List

Create an empty `<ul>`.

Add three skills dynamically using JavaScript.

---

## Task 4 — Class Toggle

Create a box with a CSS class.

Create a button that toggles another class using:

    classList.toggle()

---

## Task 5 — Attribute Manipulation

Create an image and use JavaScript to:

- Read its `src`
- Change its `alt`
- Change its `src`

---

## Task 6 — Remove Element

Create a paragraph and a button.

When the button is clicked, remove the paragraph from the DOM.

---

## Task 7 — Replace Element

Create a heading.

Use `replaceWith()` to replace it with another heading.

---

# ⭐ Final Challenge

Create a dynamic Student Dashboard.

The dashboard should contain:

- Student name
- Programme
- Current course
- Skills list
- Project list
- Progress information

Use JavaScript to:

- Select elements
- Change student information
- Toggle a CSS class
- Create a new skill
- Create a new project
- Remove an item
- Change an attribute
- Traverse at least one DOM relationship

Use at least:

- `querySelector()`
- `querySelectorAll()`
- `textContent`
- `classList`
- `setAttribute()`
- `createElement()`
- `append()`
- `remove()`
- `parentElement`
- `children`

---

# ✅ Self-Check

Before moving to Day 056, make sure you can explain:

- [ ] `getElementById()`
- [ ] `getElementsByClassName()`
- [ ] `getElementsByTagName()`
- [ ] `querySelector()`
- [ ] `querySelectorAll()`
- [ ] `textContent`
- [ ] `innerHTML`
- [ ] `style`
- [ ] `classList`
- [ ] `getAttribute()`
- [ ] `setAttribute()`
- [ ] `removeAttribute()`
- [ ] `createElement()`
- [ ] `append()`
- [ ] `prepend()`
- [ ] `before()`
- [ ] `after()`
- [ ] `remove()`
- [ ] `replaceWith()`
- [ ] `parentElement`
- [ ] `children`
- [ ] Basic DOM traversal

---

## 📌 Goal

Become comfortable selecting HTML elements and dynamically changing the webpage using JavaScript.