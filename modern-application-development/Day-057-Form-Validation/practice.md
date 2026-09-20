# 📝 Day 057 — Form Validation Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 057  
**Topic:** Form Validation

---

## 🎯 Practice Goals

Practice:

- HTML5 validation
- JavaScript validation
- Required fields
- Input types
- Length validation
- Range validation
- Pattern validation
- Custom validation
- Form submission
- Constraint Validation API

---

## Part 1 — Basic Questions

### Q1. What is form validation?

### Q2. Why is form validation important?

### Q3. What is client-side validation?

### Q4. What is server-side validation?

### Q5. Why should an application use server-side validation even when client-side validation exists?

---

## Part 2 — HTML Validation

### Task 1

Create a form with a required student name.

### Task 2

Create an email field that uses built-in email validation.

### Task 3

Create a password field requiring at least 8 characters.

### Task 4

Create an age field allowing values from 18 to 60.

### Task 5

Create a username field with:

- Minimum length: 4
- Maximum length: 20

---

## Part 3 — Pattern Validation

### Task 6

Create a student ID field using a suitable pattern.

Example format:

    IITM1234

### Task 7

Create a field that accepts only letters and spaces.

### Task 8

Create a postal code field using an appropriate pattern for your target format.

---

## Part 4 — JavaScript Validation

### Task 9

Create a registration form.

Use JavaScript to check whether the name is empty.

### Task 10

Use `trim()` to prevent whitespace-only names.

### Task 11

Create a password and confirm-password field.

Display an error when the passwords do not match.

### Task 12

Use `setCustomValidity()` for the password confirmation rule.

---

## Part 5 — Constraint Validation API

### Task 13

Use:

    checkValidity()

to check whether an email field is valid.

### Task 14

Use:

    reportValidity()

to display browser validation feedback.

### Task 15

Experiment with:

    validity.valueMissing

    validity.typeMismatch

    validity.tooShort

    validity.rangeUnderflow

    validity.rangeOverflow

---

## Part 6 — Form Events

### Task 16

Use the `submit` event to validate a form.

### Task 17

Use `preventDefault()` when the form is invalid.

### Task 18

Use the `input` event to perform live validation.

### Task 19

Use the `blur` event to validate a field after the user leaves it.

---

## Part 7 — Custom Error Messages

### Task 20

Create a custom error message for an invalid username.

### Task 21

Clear the custom error when the username becomes valid.

### Task 22

Create a password strength message:

- Weak
- Medium
- Strong

---

## 🚀 Mini Challenge — Student Registration Validator

Create a complete **Student Registration Form**.

Fields:

- Full Name
- Email
- Phone Number
- Age
- Student ID
- Password
- Confirm Password
- Course
- Date of Birth
- Terms and Conditions

Requirements:

- Use HTML5 validation.
- Use `required`.
- Use `minlength` and `maxlength`.
- Use `min` and `max`.
- Use suitable input types.
- Use at least one `pattern`.
- Use JavaScript validation.
- Use `checkValidity()`.
- Use `setCustomValidity()`.
- Use `submit` event.
- Use `preventDefault()`.
- Display clear validation feedback.
- Do not submit invalid data.

---

## 🧠 Revision Questions

1. What does `required` do?
2. What is the purpose of `minlength`?
3. What is the purpose of `maxlength`?
4. What is the difference between `min` and `minlength`?
5. What does `pattern` do?
6. What does `checkValidity()` return?
7. What does `reportValidity()` do?
8. What does `setCustomValidity()` do?
9. How do you clear a custom validation error?
10. Why is `trim()` useful during text validation?
11. What does `preventDefault()` do?
12. What is the difference between client-side and server-side validation?
13. Why should client-side validation not be treated as a security mechanism?
14. What is `validity.typeMismatch`?
15. What is `validity.valueMissing`?

---

## ✅ Completion Checklist

- [ ] I understand form validation.
- [ ] I understand client-side validation.
- [ ] I understand server-side validation.
- [ ] I can use `required`.
- [ ] I can use `minlength` and `maxlength`.
- [ ] I can use `min` and `max`.
- [ ] I can use `pattern`.
- [ ] I can validate forms using JavaScript.
- [ ] I understand `checkValidity()`.
- [ ] I understand `reportValidity()`.
- [ ] I understand `setCustomValidity()`.
- [ ] I can prevent invalid submission.
- [ ] I completed the Student Registration Validator.