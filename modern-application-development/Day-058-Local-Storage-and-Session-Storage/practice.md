# 📝 Day 058 — Local Storage and Session Storage Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 058  
**Topic:** Local Storage and Session Storage

---

## 🎯 Practice Goals

Practice:

- `localStorage`
- `sessionStorage`
- `setItem()`
- `getItem()`
- `removeItem()`
- `clear()`
- `key()`
- `length`
- JSON serialization
- JSON parsing
- Storage events
- Persistent preferences
- Temporary session data

---

## Part 1 — Basic Questions

### Q1. What is Web Storage?

### Q2. What is `localStorage`?

### Q3. What is `sessionStorage`?

### Q4. What is the main difference between `localStorage` and `sessionStorage`?

### Q5. What type of values does Web Storage store?

---

## Part 2 — Basic Storage

### Task 1

Store your name in `localStorage`.

### Task 2

Read the stored name and display it on the page.

### Task 3

Update the stored name.

### Task 4

Remove the stored name.

### Task 5

Create three storage entries and display:

    localStorage.length

---

## Part 3 — sessionStorage

### Task 6

Store your current course in `sessionStorage`.

### Task 7

Read the course and display it.

### Task 8

Create a temporary page counter using `sessionStorage`.

---

## Part 4 — Numbers and Booleans

### Task 9

Store a student age.

Retrieve it and convert it back to a number.

### Task 10

Store a boolean value such as:

    true

Retrieve it and convert the string representation back into a boolean.

---

## Part 5 — Objects

### Task 11

Create a student object:

- Name
- Course
- Score

Store it using `JSON.stringify()`.

### Task 12

Retrieve the student object using `JSON.parse()`.

### Task 13

Update the student's score and store the updated object again.

---

## Part 6 — Arrays

### Task 14

Create an array of courses.

Store it in `localStorage`.

### Task 15

Retrieve the array and display every course.

### Task 16

Add another course and save the updated array.

---

## Part 7 — Theme Preference

### Task 17

Create a theme selector:

- Light
- Dark

Store the selected theme in `localStorage`.

### Task 18

When the page loads, read the stored theme and apply it.

---

## Part 8 — Storage Events

### Task 19

Create a `storage` event listener.

Display:

- Changed key
- Old value
- New value

Test it using two same-origin tabs/windows where applicable.

---

## Part 9 — Error Handling

### Task 20

Create a JSON string that contains invalid JSON.

Use `try...catch` around `JSON.parse()`.

Display a friendly error message.

---

## 🚀 Mini Challenge — Student Learning Tracker

Build a **Student Learning Tracker**.

Features:

- Student name
- Current course
- Completed topics
- Progress percentage
- Theme preference
- Save button
- Load button
- Delete button

Requirements:

- Use `localStorage`.
- Store the student information as an object.
- Use `JSON.stringify()`.
- Use `JSON.parse()`.
- Allow updating progress.
- Display saved data.
- Handle missing data.
- Provide a clear-data button.

---

## 🧪 Advanced Challenge

Create a **Study Session Tracker**.

Store:

- Subject
- Study duration
- Current topic
- Start time
- Progress

Use:

- `sessionStorage` for current session information.
- `localStorage` for long-term preferences.

Add buttons:

- Start Session
- Save Progress
- Load Progress
- End Session
- Clear Saved Data

---

## 🧠 Revision Questions

1. What is Web Storage?
2. What is `localStorage`?
3. What is `sessionStorage`?
4. What does `setItem()` do?
5. What does `getItem()` return when a key does not exist?
6. What does `removeItem()` do?
7. What does `clear()` do?
8. What does `key()` do?
9. What does `length` represent?
10. Why are numbers retrieved from storage as strings?
11. Why do we use `JSON.stringify()`?
12. Why do we use `JSON.parse()`?
13. How can you store an array?
14. How can you store an object?
15. What is the `storage` event?
16. Why should sensitive information not be stored in Web Storage?
17. Is Web Storage a replacement for a database?
18. When would you prefer `sessionStorage`?
19. When would you prefer `localStorage`?
20. What happens when an existing key is passed to `setItem()`?

---

## ✅ Completion Checklist

- [ ] I understand Web Storage.
- [ ] I understand `localStorage`.
- [ ] I understand `sessionStorage`.
- [ ] I can store data.
- [ ] I can retrieve data.
- [ ] I can update data.
- [ ] I can remove data.
- [ ] I understand `clear()`.
- [ ] I understand `length` and `key()`.
- [ ] I understand why values are strings.
- [ ] I can store objects using JSON.
- [ ] I can store arrays using JSON.
- [ ] I can use `JSON.stringify()`.
- [ ] I can use `JSON.parse()`.
- [ ] I understand storage events.
- [ ] I understand Web Storage security limitations.
- [ ] I completed the Student Learning Tracker.