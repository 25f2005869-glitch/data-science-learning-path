# ⚡ Day 049 — Objects — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 049  
**Topic:** Objects

---

## 🧩 Create Object

    const student = {
        name: "Saloni",
        age: 17,
        course: "MAD1"
    };

---

## 🔑 Dot Notation

    student.name

---

## 🔑 Bracket Notation

    student["name"]

Dynamic property:

    const key = "name";
    student[key]

---

## ➕ Add Property

    student.email = "example@email.com";

---

## ✏️ Update Property

    student.age = 18;

---

## ❌ Delete Property

    delete student.email;

---

## 🔍 Check Property

    "name" in student

---

## 🔧 Object Method

    const student = {
        name: "Saloni",

        greet() {
            return `Hello ${this.name}`;
        }
    };

    student.greet();

---

## 🎯 this

    const student = {
        name: "Saloni",

        showName() {
            return this.name;
        }
    };

`this.name` refers to the object's `name` property in this method call.

---

## 🔑 Object.keys()

    Object.keys(student);

Returns property names.

---

## 💎 Object.values()

    Object.values(student);

Returns property values.

---

## 🔗 Object.entries()

    Object.entries(student);

Returns key-value pairs.

---

## 🔁 for...in

    for (const key in student) {
        console.log(key, student[key]);
    }

---

## 📦 Nested Object

    const student = {
        name: "Saloni",
        address: {
            city: "Delhi"
        }
    };

Access:

    student.address.city

---

## 📚 Array of Objects

    const students = [
        { name: "Asha", marks: 85 },
        { name: "Riya", marks: 90 }
    ];

Access:

    students[0].name

---

## 📊 Array of Objects Loop

    for (let i = 0; i < students.length; i++) {
        console.log(students[i].name);
    }

---

## 📥 Destructuring

    const { name, age } = student;

---

## ✨ Property Shorthand

    const name = "Saloni";
    const age = 17;

    const student = {
        name,
        age
    };

---

## 🧠 Important

| Concept | Syntax |
|---|---|
| Property access | `student.name` |
| Bracket access | `student["name"]` |
| Add property | `student.email = "..."` |
| Update property | `student.age = 18` |
| Delete property | `delete student.age` |
| Keys | `Object.keys(student)` |
| Values | `Object.values(student)` |
| Entries | `Object.entries(student)` |

---

## 📌 Remember

- Object = key-value pairs.
- Keys are property names.
- Values can be any JavaScript value.
- Dot notation is simple and common.
- Bracket notation is useful for dynamic keys.
- Methods are functions inside objects.
- `this` can access the current object's properties.
- Arrays of objects are widely used for structured data.