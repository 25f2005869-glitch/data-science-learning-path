# 📘 Day 008 - HTML Forms

## What is an HTML Form?

An HTML form is used to collect information from users.

For example:

- Name
- Email
- Password
- Age
- Gender
- Course
- Feedback

A form is created using the `<form>` element.

```html
<form>
    ...
</form>
```

---

# Form Structure

A basic form looks like this:

```html
<form>

    <label for="name">Name:</label>

    <input type="text" id="name" name="name">

    <button type="submit">Submit</button>

</form>
```

---

# Label

The `<label>` element provides a description for a form control.

```html
<label for="email">Email:</label>

<input type="email" id="email" name="email">
```

The `for` attribute should match the input's `id`.

---

# Text Input

Used for normal text.

```html
<input type="text" name="name">
```

---

# Email Input

Used for email addresses.

```html
<input type="email" name="email">
```

The browser can perform basic email-format checking.

---

# Password Input

Used for passwords.

```html
<input type="password" name="password">
```

The entered characters are hidden.

---

# Number Input

Used for numbers.

```html
<input type="number" name="age">
```

---

# Date Input

Used to select a date.

```html
<input type="date" name="dob">
```

---

# Placeholder

Shows a hint inside an input.

```html
<input
    type="text"
    placeholder="Enter your name">
```

Placeholder is only a hint. It should not replace a proper `<label>`.

---

# Required

Makes a field mandatory.

```html
<input
    type="email"
    name="email"
    required>
```

The browser will not allow submission until the required field is filled.

---

# Radio Buttons

Radio buttons allow the user to select one option from a group.

```html
<input
    type="radio"
    name="gender"
    value="male">

<label>Male</label>

<input
    type="radio"
    name="gender"
    value="female">

<label>Female</label>
```

The same `name` groups the radio buttons together.

---

# Checkboxes

Checkboxes allow users to select multiple options.

```html
<input
    type="checkbox"
    name="skill"
    value="html">

<label>HTML</label>

<input
    type="checkbox"
    name="skill"
    value="css">

<label>CSS</label>
```

---

# Textarea

Used for longer text.

```html
<textarea
    name="message"
    rows="5"
    cols="30">
</textarea>
```

Commonly used for:

- Feedback
- Comments
- Messages
- Descriptions

---

# Select and Option

Creates a dropdown menu.

```html
<select name="course">

    <option value="mad">
        MAD
    </option>

    <option value="bdm">
        BDM
    </option>

    <option value="mlt">
        MLT
    </option>

</select>
```

---

# Button

A submit button can be created using:

```html
<button type="submit">
    Submit
</button>
```

Other common button types:

```html
<button type="submit">Submit</button>

<button type="reset">Reset</button>

<button type="button">Click Me</button>
```

---

# Form Attributes

## action

Specifies where form data should be sent.

```html
<form action="/submit">
```

## method

Specifies how the data is submitted.

```html
<form method="post">
```

Common methods:

- GET
- POST

For now, remember the basic difference:

**GET** → data is generally included in the URL.

**POST** → data is sent in the request body.

---

# Important Input Types

```html
text
email
password
number
date
radio
checkbox
file
submit
reset
button
```

---

# Basic Validation

HTML provides built-in validation.

Example:

```html
<input
    type="email"
    required>
```

The browser checks that:

- The field is not empty.
- The input follows the expected type.

Later, JavaScript can be used for more advanced validation.

---

# Best Practices

### 1. Always use labels

```html
<label for="name">Name:</label>
<input id="name" type="text">
```

### 2. Use meaningful names

```html
<input
    type="email"
    name="email">
```

### 3. Use required when necessary

```html
<input
    type="text"
    required>
```

### 4. Group related controls

Use `<fieldset>` and `<legend>` when appropriate.

```html
<fieldset>

    <legend>Gender</legend>

    ...

</fieldset>
```

---

# Summary

Today you learned:

- Forms
- Labels
- Inputs
- Text
- Email
- Password
- Number
- Date
- Radio Buttons
- Checkboxes
- Textarea
- Select
- Option
- Buttons
- Required
- Action
- Method

Congratulations! 🎉
```

---

# 📋 cheat-sheet.md

````md
# 📋 Day 008 - HTML Forms Cheat Sheet

## Form

```html
<form>
    ...
</form>
```

---

## Label

```html
<label for="name">
    Name
</label>
```

---

## Text

```html
<input type="text" name="name">
```

---

## Email

```html
<input type="email" name="email">
```

---

## Password

```html
<input type="password" name="password">
```

---

## Number

```html
<input type="number" name="age">
```

---

## Date

```html
<input type="date" name="dob">
```

---

## Radio

```html
<input
    type="radio"
    name="gender"
    value="male">

<input
    type="radio"
    name="gender"
    value="female">
```

**Remember:** Radio buttons in the same group should have the same `name`.

---

## Checkbox

```html
<input
    type="checkbox"
    name="skill"
    value="html">
```

---

## Textarea

```html
<textarea
    name="message"
    rows="5"
    cols="30">
</textarea>
```

---

## Dropdown

```html
<select name="course">

    <option value="mad">
        MAD
    </option>

    <option value="bdm">
        BDM
    </option>

</select>
```

---

## Submit Button

```html
<button type="submit">
    Submit
</button>
```

---

## Reset Button

```html
<button type="reset">
    Reset
</button>
```

---

## Required

```html
<input
    type="text"
    required>
```

---

## Placeholder

```html
<input
    type="text"
    placeholder="Enter your name">
```

---

## Form Attributes

| Attribute | Purpose |
|---|---|
| action | Destination for form submission |
| method | HTTP submission method |
| name | Identifies form data |
| value | Value submitted |
| required | Makes field mandatory |
| placeholder | Displays input hint |

---

## ⭐ Remember

```text
<form>       → Form
<label>      → Label
<input>      → Input
<textarea>   → Long Text
<select>     → Dropdown
<option>     → Dropdown Option
<button>     → Button
required     → Mandatory Field
```