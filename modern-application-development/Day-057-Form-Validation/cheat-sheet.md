# ⚡ Day 057 — Form Validation Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 057  
**Topic:** Form Validation

---

## 🔹 HTML Validation Attributes

| Attribute | Purpose |
|---|---|
| `required` | Field must have a value |
| `minlength` | Minimum characters |
| `maxlength` | Maximum characters |
| `min` | Minimum numeric/date value |
| `max` | Maximum numeric/date value |
| `pattern` | Regular expression format |
| `type` | Built-in input validation |
| `multiple` | Allows multiple suitable values/files |

---

## 🔹 Common Input Types

    email
    url
    number
    date
    tel
    text
    password

---

## 🔹 Basic Validation

    <input
        type="email"
        required
        minlength="5"
    >

---

## 🔹 JavaScript Validation

    form.addEventListener("submit", function (event) {

        if (input.value.trim() === "") {
            event.preventDefault();
        }

    });

---

## 🔹 checkValidity()

    if (input.checkValidity()) {
        console.log("Valid");
    }

Returns:

    true
    false

---

## 🔹 reportValidity()

    form.reportValidity();

Checks the form and displays browser validation feedback when appropriate.

---

## 🔹 Custom Validation

    input.setCustomValidity(
        "Invalid value."
    );

Clear the custom error:

    input.setCustomValidity("");

---

## 🔹 Validity Properties

    input.validity.valid

    input.validity.valueMissing

    input.validity.typeMismatch

    input.validity.tooShort

    input.validity.tooLong

    input.validity.rangeUnderflow

    input.validity.rangeOverflow

    input.validity.patternMismatch

---

## 🔹 Form Submission

    form.addEventListener("submit", function (event) {
        event.preventDefault();
    });

Use `preventDefault()` when you need to stop the default submission behavior.

---

## 🔹 Real-Time Validation

    input.addEventListener("input", function () {
        // validation logic
    });

---

## 🔹 Password Confirmation

    if (password.value !== confirmPassword.value) {
        confirmPassword.setCustomValidity(
            "Passwords do not match."
        );
    } else {
        confirmPassword.setCustomValidity("");
    }

---

## 🔹 Client vs Server

Client-side:

    Browser
    ↓
    Fast feedback

Server-side:

    Server
    ↓
    Trusted validation

Never rely only on client-side validation for security.

---

## 🔹 Important Difference

`placeholder`:

- Provides a hint
- Does not validate

`required`:

- Makes a field mandatory

`pattern`:

- Defines a required format

---

## 🧠 Remember

    required
    minlength
    maxlength
    min
    max
    pattern
    ↓
    HTML validation

    checkValidity()
    reportValidity()
    setCustomValidity()
    ↓
    JavaScript validation