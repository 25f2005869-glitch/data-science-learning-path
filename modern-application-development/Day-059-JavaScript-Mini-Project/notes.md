# 📚 Day 059 — JavaScript Mini Project

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 059  
**Topic:** JavaScript Mini Project

---

# 🎓 Student Learning Tracker

## 1. Project Objective

The Student Learning Tracker is an interactive JavaScript application designed to combine the concepts learned throughout the JavaScript section.

The application manages basic student information, courses, marks, learning progress, and browser storage.

---

## 2. JavaScript Concepts Used

The project integrates:

- Variables
- Constants
- Data types
- Operators
- Conditions
- Loops
- Functions
- Arrays
- Objects
- Array methods
- Template literals
- DOM manipulation
- Events
- Form validation
- Error handling
- Web Storage

---

## 3. Application Flow

The basic flow is:

    User enters information
            ↓
    Form validation
            ↓
    JavaScript processes data
            ↓
    Student object is created
            ↓
    Result is calculated
            ↓
    DOM is updated
            ↓
    Data can be saved
            ↓
    localStorage/sessionStorage

---

## 4. Student Object

The application represents a student using an object.

Example:

    const student = {
        name: "Saloni",
        course: "MAD 1",
        marks: 85
    };

Objects allow related information to be grouped together.

---

## 5. Functions

The project uses reusable functions.

Examples of responsibilities:

- Validate student data
- Calculate grade
- Calculate average
- Display student information
- Save data
- Load data
- Update progress

Using functions keeps the code organized and reusable.

---

## 6. Conditional Statements

Conditions are used to calculate grades.

Example logic:

    marks >= 90
        → A+

    marks >= 80
        → A

    marks >= 70
        → B

    marks >= 60
        → C

    marks >= 50
        → D

    otherwise
        → F

The actual project implements this logic through JavaScript conditions.

---

## 7. Arrays

The project maintains a list of courses.

Example:

    const courses = [
        "MAD 1",
        "DBMS",
        "PDSA",
        "MLF"
    ];

Arrays make it possible to:

- Add courses
- Remove courses
- Search courses
- Display courses
- Iterate through courses

---

## 8. Array Methods

Methods such as:

    push()
    filter()
    forEach()
    map()
    includes()

can be used to process course and progress data.

---

## 9. DOM Manipulation

JavaScript selects HTML elements and changes their content.

Examples:

    document.querySelector()

    element.textContent

    element.classList

    document.createElement()

This makes the page interactive without manually editing the HTML after loading.

---

## 10. Event Listeners

The application responds to user actions.

Examples:

    click

    input

    change

    submit

Events connect user interaction with JavaScript logic.

---

## 11. Form Validation

The project validates:

- Student name
- Email
- Course
- Marks

Validation prevents incomplete or invalid information from being processed.

The project uses:

    required

    min

    max

    checkValidity()

    preventDefault()

---

## 12. Grade Calculation

The marks are converted into a grade.

Example:

    function calculateGrade(marks) {
        if (marks >= 90) {
            return "A+";
        }

        if (marks >= 80) {
            return "A";
        }

        if (marks >= 70) {
            return "B";
        }

        if (marks >= 60) {
            return "C";
        }

        if (marks >= 50) {
            return "D";
        }

        return "F";
    }

---

## 13. localStorage

Student information can be saved using:

    localStorage.setItem(
        "student",
        JSON.stringify(student)
    );

Because Web Storage stores strings, `JSON.stringify()` is used for objects.

---

## 14. Reading localStorage

Stored information can be retrieved using:

    const data =
        localStorage.getItem("student");

Then it can be converted back into an object:

    const student =
        JSON.parse(data);

---

## 15. sessionStorage

Temporary session information can be stored using:

    sessionStorage.setItem(
        "currentCourse",
        course
    );

This is useful for information needed only during the current page session.

---

## 16. JSON

JSON is used to convert JavaScript objects into strings and back.

Storage:

    JSON.stringify(object)

Retrieval:

    JSON.parse(string)

---

## 17. Error Handling

Storage data can potentially be invalid.

Therefore, JSON parsing can be protected with:

    try {
        const data = JSON.parse(value);
    } catch (error) {
        console.error(error);
    }

This prevents an invalid stored value from breaking the application.

---

## 18. Theme Preference

The project can store a theme preference.

Example:

    localStorage.setItem(
        "theme",
        "dark"
    );

When the page loads, the saved preference can be read and applied.

---

## 19. Progress Tracking

The project represents learning progress as a percentage.

Example:

    const progress = 65;

The progress bar is updated dynamically using JavaScript.

---

## 20. Dynamic Course Management

The project allows courses to be added dynamically.

The basic flow is:

    User enters course
            ↓
    JavaScript creates element
            ↓
    Element is added to DOM
            ↓
    Course list updates

---

## 21. Reset Functionality

The reset feature clears the form and restores the application to its initial state.

It demonstrates:

- Form reset events
- DOM updates
- Clearing temporary values

---

## 22. Why This Project Is Important

A mini project is different from studying individual concepts separately.

Individual lessons teach:

    Concept → Example

A project requires:

    Multiple concepts
            ↓
    Combined logic
            ↓
    User interaction
            ↓
    Data processing
            ↓
    Working application

This makes the project an important JavaScript practice milestone.

---

## 23. Key Takeaway

The project demonstrates how JavaScript connects:

    HTML
      ↓
    DOM
      ↓
    Events
      ↓
    JavaScript Logic
      ↓
    Validation
      ↓
    Storage
      ↓
    Interactive Application

This is the foundation required for building more advanced web applications.