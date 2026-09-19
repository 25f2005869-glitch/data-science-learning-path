# 📝 Day 049 — Objects — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 049  
**Topic:** Objects

---

# Part A — Basic Questions

1. What is an object?
2. Why are objects useful?
3. What is a property?
4. What is a key?
5. What is a value?
6. How do you create an object?
7. What is dot notation?
8. What is bracket notation?
9. When is bracket notation especially useful?
10. How do you add a property?
11. How do you update a property?
12. How do you delete a property?
13. What is an object method?
14. What does `this` usually refer to inside an object method?
15. What does `Object.keys()` return?
16. What does `Object.values()` return?
17. What does `Object.entries()` return?
18. What is a nested object?
19. What is an array of objects?
20. What is object destructuring?

---

# Part B — Predict the Output

## Question 1

    const student = {
        name: "Saloni",
        age: 17
    };

    console.log(student.name);

Write the output.

---

## Question 2

    const student = {
        name: "Saloni",
        marks: 85
    };

    student.marks = 95;

    console.log(student.marks);

Write the output.

---

## Question 3

    const subjects = {
        first: "DBMS",
        second: "PDSA"
    };

    console.log(subjects["second"]);

Write the output.

---

## Question 4

    const student = {
        name: "Saloni",

        greet() {
            return `Hello ${this.name}`;
        }
    };

    console.log(student.greet());

Write the output.

---

## Question 5

    const student = {
        name: "Saloni",
        age: 17,
        course: "MAD1"
    };

    console.log(Object.keys(student));

Write the result.

---

# Part C — Basic Object Practice

## Task 1

Create a `student` object containing:

- Name
- Age
- Programme
- Course

## Task 2

Print the student's name using dot notation.

## Task 3

Print the student's course using bracket notation.

## Task 4

Add an `email` property.

## Task 5

Update the student's age.

## Task 6

Delete the email property.

## Task 7

Check whether the object contains the `name` property.

---

# Part D — Object Methods

## Task 8

Create a student object with a `greet()` method.

## Task 9

Create a `getDetails()` method that returns the student's name and course.

## Task 10

Create a `isPassed()` method that checks whether marks are at least 40.

## Task 11

Create a method that calculates the average of three marks stored in the object.

---

# Part E — Object and Arrays

Create:

    const student = {
        name: "Saloni",
        subjects: ["DBMS", "PDSA", "MLF"],
        marks: [85, 90, 78]
    };

## Task 12

Print the first subject.

## Task 13

Print the last mark.

## Task 14

Print all subjects using a loop.

## Task 15

Calculate the total marks.

## Task 16

Calculate the average marks.

---

# Part F — Nested Objects

Create:

    const student = {
        name: "Saloni",
        contact: {
            email: "student@example.com",
            city: "Delhi"
        }
    };

## Task 17

Print the email.

## Task 18

Print the city.

## Task 19

Add a phone number inside `contact`.

---

# Part G — Object Methods

## Task 20

Use `Object.keys()` to display all property names.

## Task 21

Use `Object.values()` to display all values.

## Task 22

Use `Object.entries()` to display all key-value pairs.

## Task 23

Use a `for...in` loop to display every property and value.

---

# Part H — Array of Objects

Use:

    const students = [
        { name: "Asha", marks: 85 },
        { name: "Riya", marks: 92 },
        { name: "Neha", marks: 78 },
        { name: "Pooja", marks: 88 }
    ];

## Task 24

Print all student names.

## Task 25

Print all marks.

## Task 26

Find the student with the highest marks.

## Task 27

Find the student with the lowest marks.

## Task 28

Calculate the average marks.

## Task 29

Count students with marks greater than or equal to 80.

---

# Part I — Functions and Objects

## Task 30

Create a function that accepts a student object and returns the student's name.

## Task 31

Create a function that accepts a student object and returns the student's average marks.

## Task 32

Create a function that displays student details using a template literal.

---

# Part J — Destructuring

## Task 33

Create:

    const student = {
        name: "Saloni",
        age: 17,
        course: "MAD1"
    };

Extract `name` and `course` using object destructuring.

## Task 34

Create an object using property shorthand.

---

# Part K — Challenges

## Challenge 1 — Student Profile Object

Create a complete student object containing:

- Name
- Age
- Programme
- Current course
- Skills
- Subjects
- Marks
- Contact information

Create methods to:

- Display profile
- Calculate total
- Calculate average
- Find highest mark
- Check pass/fail

---

## Challenge 2 — Student Database

Create an array of at least five student objects.

Each student should contain:

- Name
- Roll number
- Course
- Marks

Write programs to:

- Display all students.
- Find the highest scorer.
- Find the lowest scorer.
- Calculate class average.
- Count passing students.

---

## Challenge 3 — Course Object

Create a course object containing:

- Course name
- Instructor
- Duration
- Topics
- Progress

Add methods to:

- Display course details.
- Update progress.
- Check whether the course is completed.

---

## Challenge 4 — Product Object

Create product objects containing:

- Name
- Price
- Category
- Quantity

Create functions to:

- Calculate total inventory value.
- Find the most expensive product.
- Display products from a particular category.

---

# 🎯 Revision Checklist

- [ ] I understand objects.
- [ ] I understand key-value pairs.
- [ ] I can create objects.
- [ ] I can access properties.
- [ ] I understand dot notation.
- [ ] I understand bracket notation.
- [ ] I can add, update, and delete properties.
- [ ] I can create object methods.
- [ ] I understand `this`.
- [ ] I can work with nested objects.
- [ ] I can work with arrays of objects.
- [ ] I can use `Object.keys()`.
- [ ] I can use `Object.values()`.
- [ ] I can use `Object.entries()`.
- [ ] I can use objects with functions and loops.