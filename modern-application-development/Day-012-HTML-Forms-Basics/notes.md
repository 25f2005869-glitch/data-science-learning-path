
### `notes.md`

```markdown
# 📝 Day 012 — HTML Forms Basics Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Modern Application Development (MAD 1)

---

# 1. Introduction to HTML Forms

HTML Forms are used to collect information from users.

Examples include:

- Login forms
- Registration forms
- Contact forms
- Feedback forms
- Search forms
- Application forms

A form can contain different controls such as text fields, email fields, password fields, buttons and more.

---

# 2. The `<form>` Element

The `<form>` element defines a form.

Basic structure:

    <form>
        ...
    </form>

Form controls are placed inside the `<form>` element.

---

# 3. Basic Form

A simple form can contain a label, input and button.

Example:

    <form>

        <label for="name">Name:</label>

        <input
            type="text"
            id="name"
            name="name">

        <button type="submit">
            Submit
        </button>

    </form>

---

# 4. The `<label>` Element

The `<label>` element provides a text description for a form control.

Example:

    <label for="name">
        Full Name:
    </label>

The `for` attribute should normally match the `id` of the related input.

Example:

    <label for="name">Name:</label>

    <input
        type="text"
        id="name">

Here:

    label for="name"
    
matches:

    input id="name"

This creates a relationship between the label and the input.

---

# 5. The `<input>` Element

The `<input>` element creates an input control.

Example:

    <input type="text">

The appearance and behavior of an input depend on its `type`.

---

# 6. Text Input

`type="text"` is used for general text.

Example:

    <input
        type="text"
        name="name">

It can be used for:

- Name
- City
- Username
- Subject
- Other short text

---

# 7. Email Input

`type="email"` is used for email addresses.

Example:

    <input
        type="email"
        name="email">

Browsers can provide basic validation for email input.

For example, a value should generally resemble an email address.

---

# 8. Password Input

`type="password"` is used for password fields.

Example:

    <input
        type="password"
        name="password">

The entered characters are visually hidden by the browser.

Important:

A password input alone does not make a complete secure authentication system.

Security also depends on server-side handling and other measures.

---

# 9. Number Input

`type="number"` is used for numerical input.

Example:

    <input
        type="number"
        name="age">

It can also use attributes such as:

    min
    max
    step

Example:

    <input
        type="number"
        name="age"
        min="1"
        max="100">

---

# 10. Date Input

`type="date"` provides a date input.

Example:

    <input
        type="date"
        name="dob">

The browser may provide a date picker depending on the browser and device.

---

# 11. The `id` Attribute

The `id` attribute uniquely identifies an element within a page.

Example:

    <input
        type="text"
        id="username">

The `id` is especially useful for connecting a `<label>` with an input.

Example:

    <label for="username">
        Username:
    </label>

    <input
        type="text"
        id="username">

---

# 12. The `name` Attribute

The `name` attribute identifies a form control when form data is submitted.

Example:

    <input
        type="text"
        name="username">

The `name` attribute is important when sending form data to a server.

A useful distinction is:

    id   → Identifies the element in the page
    name → Identifies the form field in submitted data

---

# 13. The `placeholder` Attribute

The `placeholder` attribute provides a short hint inside an input.

Example:

    <input
        type="text"
        placeholder="Enter your name">

The placeholder is a hint, not a replacement for a label.

A label should still be provided for important form fields.

---

# 14. The `required` Attribute

The `required` attribute indicates that a field must be filled before the form can normally be submitted.

Example:

    <input
        type="email"
        name="email"
        required>

If the user leaves the field empty, the browser can prevent normal form submission and display validation feedback.

---

# 15. The `disabled` Attribute

The `disabled` attribute makes a form control unavailable for user interaction.

Example:

    <input
        type="text"
        value="Not Available"
        disabled>

A disabled control cannot normally be edited or focused by the user.

Disabled controls are also generally not included in submitted form data.

---

# 16. The `readonly` Attribute

The `readonly` attribute prevents the user from editing the value.

Example:

    <input
        type="text"
        value="IIT Madras"
        readonly>

Unlike a disabled control, a readonly input can generally still be focused and its value can be submitted.

---

# 17. The `value` Attribute

The `value` attribute specifies an initial value for a form control.

Example:

    <input
        type="text"
        name="course"
        value="MAD 1">

The input initially contains:

    MAD 1

---

# 18. Submit Button

A submit button submits the form.

Example:

    <button type="submit">
        Submit
    </button>

Another common form is:

    <input type="submit" value="Submit">

The `<button>` element is often more flexible because it can contain text or other permitted content.

---

# 19. Reset Button

A reset button resets form controls to their initial values.

Example:

    <button type="reset">
        Reset
    </button>

This is useful when a user wants to clear or restore the form.

---

# 20. The `action` Attribute

The `action` attribute specifies where form data should be sent when the form is submitted.

Example:

    <form action="/submit">

        ...

    </form>

In a real web application, this destination can be handled by a backend server.

---

# 21. The `method` Attribute

The `method` attribute specifies how form data is submitted.

Two common methods are:

    GET
    POST

Example:

    <form
        action="/submit"
        method="post">

        ...

    </form>

---

# 22. GET Method

The GET method is commonly used when the submitted data is intended to be part of a request for a resource.

Example:

    <form
        action="/search"
        method="get">

        ...

    </form>

Form values submitted with GET can appear in the URL as query parameters.

Example concept:

    /search?query=html

GET is commonly useful for search and retrieval operations.

---

# 23. POST Method

The POST method is commonly used when submitting data to a server for processing.

Example:

    <form
        action="/register"
        method="post">

        ...

    </form>

POST data is sent in the request body rather than being appended to the URL in the same way as GET.

However, using POST does not by itself make sensitive data secure.

HTTPS and proper server-side security are still required.

---

# 24. Basic Form Validation

HTML provides some built-in validation features.

For example:

    <input
        type="email"
        required>

This provides basic browser-level validation.

Other useful attributes include:

    required
    min
    max
    minlength
    maxlength
    pattern

HTML validation improves the user experience, but server-side validation is still necessary for real applications.

---

# 25. Example of a Basic Registration Form

A simple registration form can contain:

    Name
    Email
    Password
    Age
    Date of Birth
    Submit Button

The logical structure is:

    <form>

        Name Input

        Email Input

        Password Input

        Age Input

        Date Input

        Submit Button

    </form>

---

# 26. Form Controls and Their Purpose

    text     → General text
    email    → Email address
    password → Password
    number   → Number
    date     → Date
    submit   → Submit form
    reset    → Reset form

---

# 27. Labels and Inputs

A good form should associate labels with their controls.

Example:

    <label for="email">
        Email:
    </label>

    <input
        type="email"
        id="email"
        name="email">

The `for` and `id` values match.

---

# 28. Why Labels Matter

Labels improve:

- Usability
- Accessibility
- Form clarity

A user can understand what information should be entered into each field.

Assistive technologies can also use the label relationship to provide useful information to users.

---

# 29. Form Structure

A simple form can be visualized as:

    <form>
        │
        ├── <label>
        ├── <input>
        │
        ├── <label>
        ├── <input>
        │
        └── <button>
    </form>

---

# 30. Complete Basic Form

A basic form can look like:

    <form action="#" method="post">

        <label for="name">
            Full Name:
        </label>

        <input
            type="text"
            id="name"
            name="name"
            placeholder="Enter your name"
            required>

        <br><br>

        <label for="email">
            Email:
        </label>

        <input
            type="email"
            id="email"
            name="email"
            placeholder="Enter your email"
            required>

        <br><br>

        <label for="password">
            Password:
        </label>

        <input
            type="password"
            id="password"
            name="password"
            required>

        <br><br>

        <button type="submit">
            Submit
        </button>

        <button type="reset">
            Reset
        </button>

    </form>

---

# 31. Common Mistakes

## Mistake 1 — Missing Label Association

Incorrect:

    <label>Name:</label>

    <input
        type="text"
        id="name">

Better:

    <label for="name">
        Name:
    </label>

    <input
        type="text"
        id="name">

---

## Mistake 2 — Using Placeholder Instead of Label

A placeholder is only a hint.

Do not rely on:

    placeholder="Enter your name"

as the only identification of the field.

Use a proper label as well.

---

## Mistake 3 — Forgetting `name`

If form data needs to be submitted, form controls generally need meaningful `name` attributes.

Example:

    <input
        type="text"
        name="username">

---

## Mistake 4 — Using the Wrong Input Type

Choose an input type based on the data.

Examples:

    Email → email
    Password → password
    Age → number
    Date of Birth → date

---

# 32. Important Difference: `id` vs `name`

Remember:

    id
    ↓
    Identifies the element in the webpage

    name
    ↓
    Identifies the form field during submission

Both can have the same value, but they serve different purposes.

Example:

    <input
        type="text"
        id="username"
        name="username">

---

# 33. Important Difference: `disabled` vs `readonly`

### disabled

- User cannot interact normally.
- Disabled controls are generally not submitted.

### readonly

- User cannot edit the value.
- The control can generally still be focused.
- Its value can generally be submitted.

---

# 34. HTML Form Data Flow

A simplified form submission flow is:

    User enters data
            ↓
    Form is submitted
            ↓
    Browser creates the request
            ↓
    GET or POST
            ↓
    Server receives the data
            ↓
    Server processes the request

Backend technologies such as Flask can later be used to process submitted form data.

---

# 35. Day 012 Summary

In Day 012, I learned the basics of HTML Forms.

Important concepts include:

- `<form>`
- `<label>`
- `<input>`
- `<button>`
- Input types
- `id`
- `name`
- `value`
- `placeholder`
- `required`
- `disabled`
- `readonly`
- `action`
- `method`

I also learned the basic difference between GET and POST and the importance of labels and form validation.

---

# 🎯 Key Takeaways

    <form>     → Creates a form
    <label>    → Describes a form control
    <input>    → Creates an input control
    <button>   → Creates a button

    type="text"     → General text
    type="email"    → Email
    type="password" → Password
    type="number"   → Number
    type="date"     → Date

    id          → Identifies element
    name        → Identifies submitted form field
    placeholder → Input hint
    required    → Field is required
    disabled    → Control unavailable
    readonly    → Value cannot be edited

    GET  → Data commonly represented in URL
    POST → Data sent in request body

---

# ⭐ Final Learning Goal

By the end of Day 012, I should be able to create a basic HTML form from scratch and explain the purpose of its main elements and attributes.

---

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Modern Application Development (MAD 1)