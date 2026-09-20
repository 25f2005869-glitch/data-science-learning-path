# 📝 Day 056 — Events and Event Listeners Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 056  
**Topic:** Events and Event Listeners

---

## 🎯 Practice Goals

Practice:

- Event listeners
- Mouse events
- Keyboard events
- Input events
- Form events
- Event objects
- preventDefault()
- Event bubbling
- Event delegation
- Removing event listeners

---

## Part 1 — Basic Questions

### Q1. What is a JavaScript event?

Write a short definition.

### Q2. What is an event listener?

Explain its purpose.

### Q3. Write the basic syntax of `addEventListener()`.

### Q4. What is the difference between an event and an event listener?

### Q5. Name five common JavaScript events.

---

## Part 2 — Event Listener Practice

### Task 1

Create a button.

When the user clicks it, change its text.

### Task 2

Create a button that changes the background of a container when clicked.

### Task 3

Create a button that counts the number of clicks.

### Task 4

Create two buttons:

- Increase
- Decrease

Display the current value.

---

## Part 3 — Mouse Events

### Task 5

Create a box.

When the mouse enters the box:

- Change its text
- Change its appearance

When the mouse leaves:

- Restore the original text

### Task 6

Use `mouseenter` and `mouseleave` to create a simple hover interaction.

---

## Part 4 — Keyboard Events

### Task 7

Listen for `keydown` on the document.

Display the pressed key.

### Task 8

Create an input field.

Display the last pressed key below it.

### Task 9

Detect when the user presses `Enter`.

Display:

    Enter key pressed

---

## Part 5 — Input Events

### Task 10

Create a name input.

Display the typed name immediately below the input.

### Task 11

Create a character counter.

Display:

    Characters: 0

Update it whenever the user types.

### Task 12

Create a live student profile preview using:

- Name
- Course
- Email

---

## Part 6 — Form Events

### Task 13

Create a registration form.

Handle the `submit` event using JavaScript.

Prevent the browser's default form submission.

### Task 14

Display a success message after valid form submission.

### Task 15

Create a select menu for courses.

Display the selected course using the `change` event.

---

## Part 7 — Event Object

### Task 16

Use the event object to display:

- Event type
- Target element

### Task 17

For a keyboard event, display:

- Key
- Key code information where applicable

---

## Part 8 — Event Bubbling

### Task 18

Create:

- One parent container
- One child button

Attach click listeners to both.

Observe the order in which the listeners execute.

### Task 19

Use `stopPropagation()` and observe the difference.

---

## Part 9 — Event Delegation

### Task 20

Create a list of courses.

Attach one click listener to the parent list.

When any course is clicked, display its name.

### Task 21

Add a new course dynamically.

Verify that event delegation can handle the dynamically added course.

---

## Part 10 — removeEventListener()

### Task 22

Create a button with a click listener.

Add a second button that removes the first button's listener.

### Task 23

Create a listener function separately and use the same function reference with:

    addEventListener()

and:

    removeEventListener()

---

## 🚀 Mini Challenge

Create an interactive **Student Dashboard** containing:

- Student name input
- Course dropdown
- Marks input
- Submit button
- Result display
- Click counter
- Keyboard interaction
- Live character counter
- Course selection event
- Form submission handling

Requirements:

- Use `addEventListener()`
- Use at least five different events
- Use the event object
- Use `preventDefault()`
- Use DOM manipulation
- Keep JavaScript separate from HTML where possible

---

## 🧠 Revision Questions

1. What is an event?
2. What does `addEventListener()` do?
3. What is a callback function?
4. What is the event object?
5. What does `event.target` represent?
6. What is the difference between `input` and `change`?
7. What does `preventDefault()` do?
8. What is event bubbling?
9. What does `stopPropagation()` do?
10. What is event delegation?
11. Why is `addEventListener()` preferred over inline event handlers?
12. How do you remove an event listener?
13. Why must the same function reference be used with `removeEventListener()`?
14. What does the `once` option do?
15. What happens when an event listener is attached to an element that does not exist?

---

## ✅ Completion Checklist

- [ ] I understand JavaScript events.
- [ ] I can use `addEventListener()`.
- [ ] I can handle click events.
- [ ] I can handle keyboard events.
- [ ] I can handle input events.
- [ ] I can handle form submission.
- [ ] I understand the event object.
- [ ] I understand `preventDefault()`.
- [ ] I understand event bubbling.
- [ ] I understand event delegation.
- [ ] I can remove an event listener.
- [ ] I completed the mini challenge.