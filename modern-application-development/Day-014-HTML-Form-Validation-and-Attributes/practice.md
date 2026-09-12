# 🧠 Day 014 — HTML Form Validation and Attributes Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

# Part 1 — Theory Questions

### Q1. What is form validation?

### Q2. Why is form validation important?

### Q3. What does the `required` attribute do?

### Q4. What is the purpose of `minlength`?

### Q5. What is the purpose of `maxlength`?

### Q6. What are `min` and `max` used for?

### Q7. What is the purpose of the `pattern` attribute?

### Q8. What is the difference between `disabled` and `readonly`?

### Q9. What is client-side validation?

### Q10. Why is server-side validation still necessary?

---

# Part 2 — Multiple Choice Questions

### Q1. Which attribute makes an input compulsory?

A. `important`

B. `required`

C. `must`

D. `validate`

**Answer:** B

---

### Q2. Which attribute specifies the minimum number of characters?

A. `min`

B. `minimum`

C. `minlength`

D. `length`

**Answer:** C

---

### Q3. Which attribute specifies the maximum number of characters?

A. `maxlength`

B. `max`

C. `maximum`

D. `textmax`

**Answer:** A

---

### Q4. Which attribute can define a regular-expression pattern?

A. `regex`

B. `pattern`

C. `format`

D. `rule`

**Answer:** B

---

### Q5. Which input type provides email-oriented browser validation?

A. `mail`

B. `email`

C. `text-email`

D. `address`

**Answer:** B

---

### Q6. Which attribute prevents the user from editing a value while allowing it to be submitted?

A. `disabled`

B. `locked`

C. `readonly`

D. `fixed`

**Answer:** C

---

### Q7. Which attribute disables a form control?

A. `disable`

B. `disabled`

C. `inactive`

D. `stop`

**Answer:** B

---

### Q8. Which attribute provides a hint inside an input field?

A. `hint`

B. `placeholder`

C. `message`

D. `help`

**Answer:** B

---

### Q9. Which attribute disables built-in browser validation for a form?

A. `disable-validation`

B. `no-validation`

C. `novalidate`

D. `validate="false"`

**Answer:** C

---

### Q10. Which validation must be trusted for application security?

A. Client-side only

B. Placeholder validation

C. Server-side validation

D. Browser styling

**Answer:** C

---

# Part 3 — Coding Practice

## Exercise 1 — Required Name

Create a name field that:

- Uses `text`
- Is required
- Has a placeholder

---

## Exercise 2 — Email Validation

Create an email field that:

- Uses `type="email"`
- Is required
- Has a placeholder

---

## Exercise 3 — Password Validation

Create a password field that:

- Requires at least 8 characters
- Allows a maximum of 20 characters
- Is required

---

## Exercise 4 — Age Validation

Create a number field where:

- Minimum age = 18
- Maximum age = 100
- Field is required

---

## Exercise 5 — Phone Validation

Create a telephone input that accepts exactly 10 digits using `pattern`.

---

## Exercise 6 — Readonly Field

Create an input containing:

    IIT Madras

Make it readonly.

---

## Exercise 7 — Disabled Field

Create an input containing:

    Not Available

Make it disabled.

---

## Exercise 8 — Dropdown

Create a course dropdown containing:

- Modern Application Development
- Business Data Management
- Machine Learning Techniques

Make the field required.

---

# Part 4 — Mini Challenge

## 🏆 Student Registration Form

Create a complete Student Registration Form using HTML only.

The form should contain:

- Full Name
- Email
- Password
- Age
- Phone Number
- Date of Birth
- Gender
- Course
- Skills
- Address
- Submit button
- Reset button

Apply appropriate validation.

### Requirements

Name:

- Required
- Minimum 3 characters

Email:

- Required
- `type="email"`

Password:

- Required
- Minimum 8 characters

Age:

- Minimum 18
- Maximum 100

Phone:

- Exactly 10 digits

Course:

- Required

Skills:

- Checkbox inputs

Address:

- Required

---

# Part 5 — Debugging Practice

Find the problems in this code:

    <input type="email" required="false">

    <input type="number" minlength="18">

    <input type="text" min="3">

    <input type="text" disabled value="Student">

Think about whether each attribute is appropriate for the input type.

---

# Part 6 — Self Assessment

Rate yourself from 1 to 5.

| Skill | Rating |
|---|---:|
| Form validation | /5 |
| `required` | /5 |
| `minlength` | /5 |
| `maxlength` | /5 |
| `min` and `max` | /5 |
| `pattern` | /5 |
| Input types | /5 |
| Form attributes | /5 |
| Client-side validation | /5 |

---

# 🎯 Final Goal

After completing this practice, you should be able to create an HTML form with useful built-in validation without JavaScript.