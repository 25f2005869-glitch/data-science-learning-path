# 📝 Day 059 — JavaScript Mini Project Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 059  
**Topic:** JavaScript Mini Project

---

# 🎓 Student Learning Tracker

## 🎯 Project Goal

Build an interactive Student Learning Tracker using the JavaScript concepts learned from Day 041 to Day 058.

---

## Part 1 — Student Profile

Create a form containing:

- Student Name
- Email
- Course
- Marks

Requirements:

- Use suitable input types.
- Use labels.
- Add required validation.

---

## Part 2 — Grade Calculator

Create a function that converts marks into grades.

Use:

- A+
- A
- B
- C
- D
- F

Display the calculated grade on the page.

---

## Part 3 — Pass/Fail

Create a function that determines whether the student passed.

Example rule:

    marks >= 50
        → Passed

    marks < 50
        → Failed

---

## Part 4 — Student Object

Create a student object containing:

- Name
- Email
- Course
- Marks
- Grade
- Result

Display the object information on the page.

---

## Part 5 — Course List

Create an array containing several courses.

Example:

    MAD 1
    DBMS
    PDSA
    MLF

Display the courses dynamically.

---

## Part 6 — Add Course

Create an input and button.

When the button is clicked:

- Read the course name.
- Add it to the array.
- Update the DOM.

---

## Part 7 — Remove Course

Add a remove option for courses.

Use array methods and DOM manipulation.

---

## Part 8 — Progress Tracker

Create a progress value.

Example:

    65%

Display it using a progress bar.

Add buttons:

- Increase Progress
- Decrease Progress
- Reset Progress

---

## Part 9 — Form Validation

Validate:

- Name
- Email
- Course
- Marks

Use:

    required
    min
    max
    checkValidity()

Prevent invalid submission using:

    preventDefault()

---

## Part 10 — localStorage

Add:

    Save Student

Store the student object using:

    JSON.stringify()

Add:

    Load Student

Retrieve the object using:

    JSON.parse()

Add:

    Delete Student

Remove the stored student.

---

## Part 11 — sessionStorage

Store the current course using:

    sessionStorage

Display the current session course.

---

## Part 12 — Theme

Create:

- Light
- Dark

Store the selected theme in `localStorage`.

Restore the theme when the page loads.

---

## Part 13 — Error Handling

Use `try...catch` while parsing stored JSON.

Display a friendly message if stored data is invalid.

---

# 🚀 Final Project Requirements

The completed Student Learning Tracker should contain:

- [ ] Student form
- [ ] Form validation
- [ ] Grade calculator
- [ ] Pass/fail calculator
- [ ] Student object
- [ ] Course array
- [ ] Add course
- [ ] Remove course
- [ ] Progress tracker
- [ ] localStorage
- [ ] sessionStorage
- [ ] JSON.stringify()
- [ ] JSON.parse()
- [ ] Theme preference
- [ ] Error handling
- [ ] Dynamic DOM updates
- [ ] Event listeners
- [ ] Responsive layout

---

# 🧠 Concept Revision

Answer these questions after completing the project:

1. Why are objects useful for student data?
2. Why are arrays useful for courses?
3. Why do we use functions?
4. Why is `preventDefault()` needed for custom form handling?
5. Why does Web Storage require JSON for objects?
6. What is the difference between localStorage and sessionStorage?
7. Why should stored data be parsed carefully?
8. How does an event listener make the page interactive?
9. How does JavaScript manipulate the DOM?
10. How do multiple JavaScript concepts work together in this project?

---

# ✅ Final Checklist

- [ ] HTML structure completed
- [ ] CSS styling completed
- [ ] JavaScript logic completed
- [ ] Form validation completed
- [ ] Grade calculation completed
- [ ] Course management completed
- [ ] Progress tracker completed
- [ ] localStorage completed
- [ ] sessionStorage completed
- [ ] Theme storage completed
- [ ] Error handling completed
- [ ] Tested in browser
- [ ] Tested after page refresh
- [ ] Tested with invalid input
- [ ] Tested storage functionality