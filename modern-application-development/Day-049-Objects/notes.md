# 🧩 Day 049 — Objects — Detailed Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 049  
**Topic:** Objects

---

# 1. What Is an Object?

An object is a JavaScript data structure used to store related information as key-value pairs.

Example:

    const student = {
        name: "Saloni",
        age: 17,
        course: "MAD1"
    };

Here:

- `name` → key
- `"Saloni"` → value
- `age` → key
- `17` → value
- `course` → key
- `"MAD1"` → value

The complete collection is an object.

---

# 2. Why Use Objects?

Objects are useful when different pieces of information belong to the same entity.

For example, a student may have:

- Name
- Age
- Programme
- Course
- Marks

Instead of using separate variables:

    const name = "Saloni";
    const age = 17;
    const course = "MAD1";

We can group them:

    const student = {
        name: "Saloni",
        age: 17,
        course: "MAD1"
    };

---

# 3. Creating an Object

Objects are commonly created using curly braces.

Example:

    const student = {
        name: "Saloni",
        age: 17,
        programme: "IIT Madras BS Degree"
    };

Each property is separated by a comma.

---

# 4. Object Properties

A property consists of a key and a value.

Example:

    const student = {
        name: "Saloni",
        age: 17
    };

Properties:

    name → "Saloni"
    age → 17

Values can have different data types.

Example:

    const student = {
        name: "Saloni",
        age: 17,
        active: true,
        marks: [85, 90, 88]
    };

---

# 5. Accessing Properties — Dot Notation

The most common way to access a property is dot notation.

Example:

    const student = {
        name: "Saloni",
        age: 17
    };

    console.log(student.name);

Output:

    Saloni

Another example:

    console.log(student.age);

Output:

    17

---

# 6. Accessing Properties — Bracket Notation

Properties can also be accessed using square brackets.

Example:

    const student = {
        name: "Saloni",
        age: 17
    };

    console.log(student["name"]);

Output:

    Saloni

Both forms access the same property.

---

# 7. Dot Notation vs Bracket Notation

### Dot notation

    student.name

### Bracket notation

    student["name"]

Bracket notation is especially useful when the property name is stored in a variable.

Example:

    const property = "name";

    console.log(student[property]);

---

# 8. Adding a Property

A new property can be added after object creation.

Example:

    const student = {
        name: "Saloni",
        age: 17
    };

    student.course = "MAD1";

Now the object contains:

    name
    age
    course

---

# 9. Updating a Property

Existing properties can be changed.

Example:

    const student = {
        name: "Saloni",
        marks: 80
    };

    student.marks = 90;

The new value of `marks` is `90`.

---

# 10. Deleting a Property

The `delete` operator removes a property.

Example:

    const student = {
        name: "Saloni",
        age: 17,
        temporaryData: "Remove me"
    };

    delete student.temporaryData;

The property is removed from the object.

---

# 11. Checking a Property

The `in` operator can check whether a property exists.

Example:

    const student = {
        name: "Saloni",
        age: 17
    };

    console.log("name" in student);

Output:

    true

---

# 12. Objects Can Store Arrays

An object property can contain an array.

Example:

    const student = {
        name: "Saloni",
        subjects: ["DBMS", "PDSA", "MLF"]
    };

Access the array:

    console.log(student.subjects);

Access an individual subject:

    console.log(student.subjects[0]);

Output:

    DBMS

---

# 13. Objects Can Store Other Objects

An object can contain another object.

This is called a nested object.

Example:

    const student = {
        name: "Saloni",
        address: {
            city: "Delhi",
            country: "India"
        }
    };

Access nested data:

    console.log(student.address.city);

---

# 14. Object Methods

A function stored inside an object is called a method.

Example:

    const student = {
        name: "Saloni",

        greet: function() {
            return "Hello!";
        }
    };

Call the method:

    student.greet();

---

# 15. Short Method Syntax

Modern JavaScript allows shorter method syntax.

Example:

    const student = {
        name: "Saloni",

        greet() {
            return "Hello!";
        }
    };

This is equivalent to defining a function property.

---

# 16. The `this` Keyword

Inside an object method, `this` commonly refers to the object whose method is being executed.

Example:

    const student = {
        name: "Saloni",

        greet() {
            return `Hello, I am ${this.name}.`;
        }
    };

    console.log(student.greet());

Here:

    this.name

refers to the `name` property of the `student` object.

---

# 17. Object with a Calculation Method

Example:

    const student = {
        marks: [80, 90, 85],

        total() {
            let sum = 0;

            for (let i = 0; i < this.marks.length; i++) {
                sum += this.marks[i];
            }

            return sum;
        }
    };

    console.log(student.total());

The method uses the object's own `marks` property.

---

# 18. Object.keys()

`Object.keys()` returns an array containing the object's property names.

Example:

    const student = {
        name: "Saloni",
        age: 17,
        course: "MAD1"
    };

    console.log(Object.keys(student));

Result:

    ["name", "age", "course"]

---

# 19. Object.values()

`Object.values()` returns an array containing the object's values.

Example:

    console.log(Object.values(student));

Result:

    ["Saloni", 17, "MAD1"]

---

# 20. Object.entries()

`Object.entries()` returns an array containing key-value pairs.

Example:

    console.log(Object.entries(student));

The result contains entries similar to:

    [
        ["name", "Saloni"],
        ["age", 17],
        ["course", "MAD1"]
    ]

---

# 21. Looping Through Object Properties

`Object.keys()` can be combined with a loop.

Example:

    const student = {
        name: "Saloni",
        age: 17,
        course: "MAD1"
    };

    const keys = Object.keys(student);

    for (let i = 0; i < keys.length; i++) {
        const key = keys[i];

        console.log(key, student[key]);
    }

Bracket notation is useful here because `key` is a variable.

---

# 22. for...in Loop

The `for...in` loop can iterate over enumerable property keys of an object.

Example:

    const student = {
        name: "Saloni",
        age: 17,
        course: "MAD1"
    };

    for (const key in student) {
        console.log(key, student[key]);
    }

---

# 23. Array of Objects

A very common data structure is an array containing objects.

Example:

    const students = [
        {
            name: "Asha",
            marks: 85
        },
        {
            name: "Riya",
            marks: 90
        },
        {
            name: "Neha",
            marks: 78
        }
    ];

This structure is useful for representing multiple students.

---

# 24. Accessing an Array of Objects

Example:

    console.log(students[0].name);

Output:

    Asha

Another example:

    console.log(students[1].marks);

Output:

    90

---

# 25. Loop Through an Array of Objects

Example:

    for (let i = 0; i < students.length; i++) {
        console.log(students[i].name);
    }

This visits every student.

---

# 26. Objects as Function Arguments

Objects can be passed to functions.

Example:

    function displayStudent(student) {
        return `Name: ${student.name}, Marks: ${student.marks}`;
    }

    const student = {
        name: "Saloni",
        marks: 90
    };

    console.log(displayStudent(student));

---

# 27. Object Destructuring — Introduction

Destructuring provides a convenient way to extract properties.

Example:

    const student = {
        name: "Saloni",
        age: 17
    };

    const { name, age } = student;

    console.log(name);
    console.log(age);

This is a useful modern JavaScript feature.

---

# 28. Object Property Shorthand

If a variable and property have the same name, shorthand can be used.

Instead of:

    const name = "Saloni";
    const age = 17;

    const student = {
        name: name,
        age: age
    };

We can write:

    const student = {
        name,
        age
    };

---

# 29. Nested Object Access

Example:

    const course = {
        name: "MAD1",
        instructor: {
            name: "CodeWithHarry",
            platform: "Online"
        }
    };

Access:

    course.instructor.name

and:

    course.instructor.platform

---

# 30. Object Comparison

Objects are reference values.

For example:

    const a = { name: "Saloni" };
    const b = { name: "Saloni" };

Even though their contents look the same:

    a === b

is `false` because they are different object references.

Two variables can refer to the same object:

    const a = { name: "Saloni" };
    const b = a;

Now:

    a === b

is `true`.

---

# 31. Object Mutation

Objects declared with `const` can have their properties changed.

Example:

    const student = {
        name: "Saloni"
    };

    student.name = "Asha";

This is valid.

But the variable cannot be reassigned to another object:

    student = {};

That is not allowed because `student` was declared using `const`.

---

# 32. Common Mistakes

### Mistake 1: Wrong property name

    student.nam

is different from:

    student.name

JavaScript property names are case-sensitive.

### Mistake 2: Confusing dot and bracket notation

Correct:

    student.name

Correct:

    student["name"]

If using a variable:

    const key = "name";
    student[key]

### Mistake 3: Forgetting `this`

Inside an object method, use `this.property` when referring to the current object's property.

---

# 33. Important Concepts

- Object → collection of key-value pairs.
- Property → key and its value.
- Dot notation → `object.property`.
- Bracket notation → `object["property"]`.
- `push()` is for arrays, not ordinary objects.
- Properties can be added, updated, and deleted.
- Methods are functions stored on objects.
- `this` can refer to the current object in a method.
- Objects can contain arrays and other objects.
- Arrays of objects are common for structured data.
- `Object.keys()` returns keys.
- `Object.values()` returns values.
- `Object.entries()` returns key-value pairs.

---

# 34. Best Practices

- Use meaningful property names.
- Keep related information inside one object.
- Use `const` when the object variable does not need reassignment.
- Prefer dot notation when the property name is known.
- Use bracket notation for dynamic property names.
- Keep object methods focused.
- Use arrays of objects for collections of similar entities.
- Avoid unnecessarily deeply nested objects.
- Keep object structures consistent.