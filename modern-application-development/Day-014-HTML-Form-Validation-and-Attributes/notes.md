
## 2. `notes.md`

```markdown
# 📝 Day 014 — HTML Form Validation and Attributes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 1. What is Form Validation?

Form validation means checking whether the data entered by a user is correct and follows the required rules.

For example:

- Name should not be empty.
- Email should have a valid email format.
- Age should be within a specific range.
- Password should have a minimum length.
- A required field must contain a value.

HTML5 provides built-in validation features that allow the browser to perform many basic checks automatically.

---

## 2. Why is Form Validation Important?

Validation helps:

- Prevent incomplete form submissions
- Reduce incorrect data
- Improve user experience
- Guide users while entering information
- Improve data quality
- Reduce unnecessary server requests

However, HTML validation happens on the client side.

Important:

Client-side validation should not be treated as a security mechanism.

Server-side validation is still required when data reaches a backend application.

---

# 3. The `required` Attribute

The `required` attribute makes an input field compulsory.

Example:

    <input type="text" name="name" required>

If the user tries to submit the form without entering a value, the browser displays a validation message.

---

# 4. `minlength`

The `minlength` attribute specifies the minimum number of characters allowed.

Example:

    <input type="password" minlength="8" required>

The password must contain at least 8 characters.

---

# 5. `maxlength`

The `maxlength` attribute specifies the maximum number of characters allowed.

Example:

    <input type="text" maxlength="50">

The user cannot enter more than the specified number of characters.

---

# 6. `min`

The `min` attribute specifies the minimum allowed value.

It is commonly used with number and date inputs.

Example:

    <input type="number" min="18" max="100">

The entered number should be between 18 and 100.

---

# 7. `max`

The `max` attribute specifies the maximum allowed value.

Example:

    <input type="number" min="1" max="100">

The maximum allowed value is 100.

---

# 8. `pattern`

The `pattern` attribute allows us to specify a regular expression that the input value must match.

Example:

    <input type="text" pattern="[A-Za-z]+" required>

This pattern allows alphabetic characters.

Another example:

    <input type="text" pattern="[0-9]{10}" required>

This requires exactly 10 digits.

Note:

The `pattern` attribute is generally used with text-like inputs such as `text`, `tel`, and similar supported input types.

---

# 9. Type-Based Validation

HTML automatically performs certain validation based on the input type.

For example:

    <input type="email">

The browser checks whether the entered value follows an email-like format.

Similarly:

    <input type="url">

checks for a URL-like value.

And:

    <input type="number">

provides number-specific input and validation behavior.

---

# 10. Email Validation

Example:

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

The browser checks that the value resembles an email address.

Example:

    saloni@example.com

---

# 11. URL Validation

Example:

    <input type="url" name="website">

The browser expects a URL-like value.

Example:

    https://example.com

---

# 12. Number Validation

Example:

    <input type="number" name="age" min="18" max="60">

The value should be within the specified range.

---

# 13. `placeholder`

The `placeholder` attribute provides a short hint about what the user should enter.

Example:

    <input type="text" placeholder="Enter your name">

Important:

A placeholder is not a replacement for a `<label>`.

A proper form should still use labels for accessibility and usability.

---

# 14. `disabled`

The `disabled` attribute makes a form control unavailable for user interaction.

Example:

    <input type="text" value="Not Available" disabled>

A disabled control cannot normally be edited or submitted as successful form data.

---

# 15. `readonly`

The `readonly` attribute prevents the user from changing the value.

Example:

    <input type="text" value="IIT Madras" readonly>

The user can usually focus and select the value, but cannot edit it.

Important Difference:

`disabled` → User cannot interact normally and its value is not submitted.

`readonly` → User cannot edit the value, but the value can still be submitted.

---

# 16. `checked`

The `checked` attribute pre-selects a checkbox or radio button.

Example:

    <input type="checkbox" name="html" checked>

The checkbox will initially be selected.

---

# 17. `selected`

The `selected` attribute pre-selects an option in a dropdown.

Example:

    <select name="course">
        <option value="mad" selected>MAD</option>
        <option value="mlt">MLT</option>
    </select>

MAD will be selected initially.

---

# 18. `multiple`

The `multiple` attribute allows multiple values to be selected or entered where supported.

Example with file input:

    <input type="file" name="files" multiple>

The user can select multiple files.

---

# 19. `autocomplete`

The `autocomplete` attribute helps the browser provide previously entered information.

Example:

    <input type="email" name="email" autocomplete="email">

Common values include:

- `on`
- `off`
- `name`
- `email`
- `username`
- `current-password`
- `new-password`

---

# 20. `novalidate`

The `novalidate` attribute disables the browser's built-in validation when the form is submitted.

Example:

    <form action="#" method="post" novalidate>

This can be useful when validation is handled using another mechanism.

Normally, we should not use `novalidate` unless we have a reason to bypass native browser validation.

---

# 21. Client-Side Validation

Client-side validation happens in the user's browser.

Examples:

- `required`
- `min`
- `max`
- `minlength`
- `maxlength`
- `pattern`
- `type="email"`

Advantages:

- Fast feedback
- Better user experience
- No immediate server request needed for basic checks

---

# 22. Server-Side Validation

Server-side validation happens on the backend after the form data is submitted.

For example:

Browser:

    User → Form → Server

The server should validate the received data before storing or processing it.

Important:

Never rely only on HTML validation for security.

A malicious user can bypass client-side validation.

---

# 23. HTML Validation Example

Example:

    <form action="#" method="post">

        <label for="username">Username:</label>
        <input
            type="text"
            id="username"
            name="username"
            minlength="3"
            maxlength="20"
            required>

        <br><br>

        <label for="age">Age:</label>
        <input
            type="number"
            id="age"
            name="age"
            min="18"
            max="100"
            required>

        <br><br>

        <button type="submit">Submit</button>

    </form>

---

# 24. Validation Flow

The basic process is:

    User enters data
            ↓
    Browser checks validation rules
            ↓
    Is the data valid?
         ↙       ↘
       No         Yes
       ↓           ↓
    Show error   Submit form
                   ↓
                Server

---

# 25. Accessibility and Validation

Good forms should:

- Use `<label>` elements
- Use meaningful labels
- Clearly identify required fields
- Provide useful instructions
- Avoid relying only on placeholder text
- Use appropriate input types
- Provide understandable validation messages

Example:

    <label for="email">Email Address:</label>
    <input
        type="email"
        id="email"
        name="email"
        required>

This is better than using only a placeholder.

---

# 26. Important Differences

## `disabled` vs `readonly`

`disabled`:

- Cannot normally be edited
- Cannot normally be focused
- Value is not submitted

`readonly`:

- Cannot be edited
- Can generally be focused
- Value can be submitted

---

## `required` vs `placeholder`

`required`:

- Makes input compulsory

`placeholder`:

- Provides a hint

They serve different purposes.

---

## Client-Side vs Server-Side Validation

Client-side:

- Happens in browser
- Provides quick feedback
- Can be bypassed

Server-side:

- Happens on server
- Must validate submitted data
- Important for application security

---

# 27. Best Practices

1. Use `required` for genuinely required fields.
2. Use the correct input type.
3. Use `min` and `max` for numeric ranges.
4. Use `minlength` and `maxlength` where appropriate.
5. Use `pattern` only when a specific format is required.
6. Always provide labels.
7. Do not use placeholders as labels.
8. Perform server-side validation for submitted data.
9. Keep validation rules understandable.
10. Give users clear feedback when their input is invalid.

---

# 28. Key Takeaways

- HTML5 provides built-in form validation.
- `required` makes a field compulsory.
- `minlength` controls minimum text length.
- `maxlength` controls maximum text length.
- `min` and `max` control allowed ranges.
- `pattern` validates a specific format.
- Input types such as `email` and `url` provide type-specific validation.
- `disabled` and `readonly` are different.
- `placeholder` provides hints but does not replace labels.
- Client-side validation improves user experience.
- Server-side validation is still necessary.