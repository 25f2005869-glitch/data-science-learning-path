# ⚡ Day 059 — JavaScript Mini Project Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 059  
**Topic:** JavaScript Mini Project

---

## 🔹 Select Element

    const element =
        document.querySelector("#id");

---

## 🔹 Event Listener

    element.addEventListener(
        "click",
        function () {
            // action
        }
    );

---

## 🔹 Read Input

    const value =
        input.value.trim();

---

## 🔹 Update DOM

    element.textContent = "Hello";

---

## 🔹 Create Element

    const item =
        document.createElement("li");

    item.textContent = "MAD 1";

    list.append(item);

---

## 🔹 Array

    const courses = [
        "MAD 1",
        "DBMS",
        "PDSA"
    ];

---

## 🔹 Add Array Item

    courses.push("MLF");

---

## 🔹 Remove Using filter()

    courses = courses.filter(
        course => course !== "DBMS"
    );

---

## 🔹 Object

    const student = {
        name: "Saloni",
        course: "MAD 1",
        marks: 85
    };

---

## 🔹 Template Literal

    `Student: ${student.name}`

---

## 🔹 Function

    function calculateGrade(marks) {
        if (marks >= 90) {
            return "A+";
        }

        if (marks >= 80) {
            return "A";
        }

        return "F";
    }

---

## 🔹 Form Submit

    form.addEventListener(
        "submit",
        function (event) {
            event.preventDefault();
        }
    );

---

## 🔹 Validation

    if (!input.checkValidity()) {
        return;
    }

---

## 🔹 localStorage

Store:

    localStorage.setItem(
        "key",
        "value"
    );

Read:

    localStorage.getItem("key");

Remove:

    localStorage.removeItem("key");

Clear:

    localStorage.clear();

---

## 🔹 Object Storage

Store:

    localStorage.setItem(
        "student",
        JSON.stringify(student)
    );

Read:

    const student =
        JSON.parse(
            localStorage.getItem("student")
        );

---

## 🔹 sessionStorage

    sessionStorage.setItem(
        "course",
        "MAD 1"
    );

    sessionStorage.getItem("course");

---

## 🔹 JSON

Object → String:

    JSON.stringify(object);

String → Object:

    JSON.parse(string);

---

## 🔹 Error Handling

    try {
        const data = JSON.parse(value);
    } catch (error) {
        console.error(error);
    }

---

## 🔹 Grade Logic

    90+ → A+
    80–89 → A
    70–79 → B
    60–69 → C
    50–59 → D
    Below 50 → F

---

## 🔹 Project Flow

    HTML
      ↓
    DOM Selection
      ↓
    Event
      ↓
    Validation
      ↓
    Function
      ↓
    Data Processing
      ↓
    DOM Update
      ↓
    Storage

---

## 🧠 Most Important Concepts

    querySelector()
    addEventListener()
    textContent
    value
    preventDefault()
    checkValidity()
    JSON.stringify()
    JSON.parse()
    localStorage
    sessionStorage