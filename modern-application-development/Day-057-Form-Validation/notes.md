# 📚 Day 057 — Form Validation

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 057  
**Topic:** Form Validation

---

## 1. What Is Form Validation?

Form validation is the process of checking whether user-entered data satisfies the required rules before the form is submitted.

For example:

- Name should not be empty.
- Email should have a valid format.
- Password should have enough characters.
- Age should be within an allowed range.
- A required option should be selected.

Validation helps prevent incorrect or incomplete data from being submitted.

---

## 2. Types of Form Validation

There are two important types:

### Client-Side Validation

Validation performed in the browser before data is sent to the server.

Examples:

- HTML5 validation
- JavaScript validation

Advantages:

- Immediate feedback
- Better user experience
- Reduces unnecessary requests

### Server-Side Validation

Validation performed on the server after the data is submitted.

Server-side validation is essential because client-side validation can be bypassed.

A secure application should not rely only on browser validation.

---

## 3. HTML5 Form Validation

HTML5 provides built-in validation features.

Example:

    <input type="email" required>

The browser automatically checks whether the field:

- Contains a value
- Looks like an email address

---

## 4. required

The `required` attribute makes a field mandatory.

Example:

    <input type="text" required>

If the user leaves the field empty, the browser prevents normal form submission.

---

## 5. Input Type Validation

HTML input types can provide built-in validation.

Examples:

    <input type="email">

    <input type="url">

    <input type="number">

    <input type="date">

For example, an email input expects an email-like value.

---

## 6. minlength

`minlength` specifies the minimum number of characters.

Example:

    <input type="text" minlength="3">

A value shorter than the specified length is invalid.

---

## 7. maxlength

`maxlength` specifies the maximum number of characters.

Example:

    <input type="text" maxlength="50">

This prevents values from exceeding the specified character length.

---

## 8. min and max

For suitable numeric and date-related inputs, `min` and `max` define an allowed range.

Example:

    <input type="number" min="18" max="60">

The value must be within the specified range.

---

## 9. pattern

The `pattern` attribute allows a regular expression to define an expected format.

Example:

    <input
        type="text"
        pattern="[A-Za-z ]+"
    >

This pattern allows letters and spaces.

Patterns are useful for formats such as:

- Student IDs
- Postal codes
- Specific usernames
- Custom codes

---

## 10. placeholder vs Validation

`placeholder` provides a hint to the user.

Example:

    <input
        type="email"
        placeholder="student@example.com"
    >

A placeholder does not validate the input.

It should not be treated as a replacement for a label or validation rule.

---

## 11. disabled vs readonly

### disabled

A disabled control cannot normally be edited or submitted as a successful form control.

Example:

    <input type="text" disabled>

### readonly

A readonly control cannot normally be edited by the user, but its value can still participate in form submission when applicable.

Example:

    <input type="text" readonly value="MAD 1">

---

## 12. JavaScript Form Validation

JavaScript allows custom validation logic.

Example:

    form.addEventListener("submit", function (event) {

        if (nameInput.value.trim() === "") {
            event.preventDefault();
            alert("Name is required.");
        }

    });

JavaScript can check conditions that require application-specific logic.

---

## 13. trim()

`trim()` removes whitespace from the beginning and end of a string.

Example:

    const name = input.value.trim();

This is useful when validating text fields.

For example, a user entering only spaces should generally not be considered a valid name.

---

## 14. checkValidity()

`checkValidity()` checks whether an element satisfies its validation constraints.

Example:

    const input = document.querySelector("#email");

    if (input.checkValidity()) {
        console.log("Valid");
    } else {
        console.log("Invalid");
    }

It returns:

- `true` if valid
- `false` if invalid

---

## 15. reportValidity()

`reportValidity()` checks the validity and asks the browser to display its normal validation feedback when the element is invalid.

Example:

    form.reportValidity();

It returns a boolean indicating whether the form is valid.

---

## 16. Validity State

The browser provides the `validity` property.

Example:

    input.validity

It contains information about different validation conditions.

Useful properties include:

- `valid`
- `valueMissing`
- `typeMismatch`
- `tooShort`
- `tooLong`
- `rangeUnderflow`
- `rangeOverflow`
- `patternMismatch`

---

## 17. Custom Validation

Applications sometimes need custom rules.

Example:

    if (password !== confirmPassword) {
        // passwords do not match
    }

JavaScript can perform these application-specific checks.

---

## 18. setCustomValidity()

`setCustomValidity()` sets a custom validation message.

Example:

    input.setCustomValidity("Custom error message");

To clear the custom error:

    input.setCustomValidity("");

An important rule is:

- Non-empty message → field is invalid
- Empty message → custom error is cleared

---

## 19. Custom Validation Example

Example:

    confirmPassword.addEventListener("input", function () {

        if (confirmPassword.value !== password.value) {
            confirmPassword.setCustomValidity(
                "Passwords do not match."
            );
        } else {
            confirmPassword.setCustomValidity("");
        }

    });

This combines JavaScript logic with browser validation.

---

## 20. Preventing Form Submission

The `submit` event can be used to control submission.

Example:

    form.addEventListener("submit", function (event) {

        if (!form.checkValidity()) {
            event.preventDefault();
        }

    });

`preventDefault()` prevents the browser's default submission action.

---

## 21. Custom Error Messages

Instead of relying only on browser messages, a page can display its own messages.

Example:

    errorMessage.textContent =
        "Please enter a valid email address.";

Custom messages can provide clearer instructions.

---

## 22. Validation Flow

A typical validation flow is:

    User enters data
            ↓
    Browser validation
            ↓
    JavaScript validation
            ↓
    Show errors if needed
            ↓
    Stop submission if invalid
            ↓
    Submit/process valid data

---

## 23. Real-Time Validation

Validation can also happen while the user types.

Example:

    input.addEventListener("input", function () {
        // validate current value
    });

Real-time validation is useful for:

- Password strength
- Character limits
- Username availability feedback
- Confirm password
- Live formatting checks

Avoid making validation unnecessarily annoying while the user is typing.

---

## 24. Form Validation and Events

Form validation commonly uses events such as:

- `input`
- `change`
- `focus`
- `blur`
- `submit`

Example:

    emailInput.addEventListener("blur", validateEmail);

    form.addEventListener("submit", validateForm);

---

## 25. novalidate

The `novalidate` attribute disables the browser's automatic interactive constraint validation for that form.

Example:

    <form novalidate>

This can be useful when an application wants to completely control validation through JavaScript.

However, disabling built-in validation means the developer must implement appropriate validation logic.

---

## 26. Constraint Validation API

HTML forms provide a browser API for working with validation constraints.

Important methods:

    checkValidity()

    reportValidity()

    setCustomValidity()

Important properties:

    validity

    validationMessage

    willValidate

---

## 27. Accessibility and Validation

Good validation should be accessible.

Best practices:

- Use proper `<label>` elements.
- Clearly identify invalid fields.
- Provide understandable error messages.
- Do not rely only on color.
- Keep error messages near the relevant field.
- Use appropriate input types.
- Preserve keyboard accessibility.
- Do not make error messages unnecessarily complicated.

---

## 28. Client-Side Validation Is Not Security

Client-side validation improves user experience but cannot be trusted as the only security mechanism.

Users can:

- Disable JavaScript
- Modify HTML
- Send requests directly
- Bypass browser validation

Therefore:

    Client-side validation
    +
    Server-side validation

is the safer approach.

---

## 29. Common Mistakes

### Mistake 1: Relying only on placeholder

A placeholder is not a label and does not validate input.

### Mistake 2: Relying only on JavaScript

HTML validation can handle many basic constraints efficiently.

### Mistake 3: Relying only on client-side validation

Server-side validation is still required for submitted data.

### Mistake 4: Forgetting trim()

Whitespace-only input can pass a naive text check.

### Mistake 5: Forgetting to clear custom validity

If `setCustomValidity()` sets an error, remember to clear it when the input becomes valid.

Example:

    input.setCustomValidity("");

### Mistake 6: Using overly strict patterns

A pattern should match realistic valid input instead of unnecessarily rejecting users.

---

## 30. Best Practices

- Use semantic HTML.
- Use appropriate input types.
- Use built-in HTML5 validation when suitable.
- Add JavaScript for custom business rules.
- Provide clear error messages.
- Validate important fields before submission.
- Keep server-side validation in real applications.
- Do not rely on color alone for errors.
- Avoid unnecessarily strict validation.
- Keep validation logic reusable.

---

## 🧠 Key Takeaway

Form validation ensures that user input follows defined rules.

Remember:

    HTML validation
        ↓
    JavaScript validation
        ↓
    Server-side validation

Important tools:

    required
    minlength
    maxlength
    min
    max
    pattern
    checkValidity()
    reportValidity()
    setCustomValidity()